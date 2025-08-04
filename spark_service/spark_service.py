from flask import Flask, request, Response, jsonify
import subprocess
import os
import time
import glob
import logging
from datetime import datetime

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/flask-service.log'),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)

def cleanup_output_directory(output_dir):
    """Nettoie le répertoire de sortie des fichiers précédents"""
    pattern = os.path.join(output_dir, "part-*.json")
    cleaned_files = 0
    
    try:
        for f in glob.glob(pattern):
            os.remove(f)
            cleaned_files += 1
        
        if cleaned_files > 0:
            logging.info(f"Nettoyé {cleaned_files} fichiers de sortie précédents")
        
        return True
    except Exception as e:
        logging.error(f"Erreur lors du nettoyage : {str(e)}")
        return False

def wait_for_output_files(output_dir, timeout=120):
    """Attend l'apparition des fichiers de sortie avec timeout configurable"""
    pattern = os.path.join(output_dir, "part-*.json")
    
    logging.info(f"Attente des fichiers de sortie dans {output_dir}")
    
    for i in range(timeout):
        files = glob.glob(pattern)
        if files:
            logging.info(f"Trouvé {len(files)} fichier(s) de sortie après {i+1}s")
            return files
        time.sleep(1)
    
    logging.error(f"Timeout après {timeout}s - aucun fichier de sortie trouvé")
    return []

def read_and_concatenate_json_files(files):
    """Lit et concatène les fichiers JSON de sortie"""
    concatenated = ""
    total_lines = 0
    
    try:
        for file_path in sorted(files):
            logging.info(f"Lecture du fichier : {file_path}")
            
            with open(file_path, "r", encoding='utf-8') as f:
                content = f.read().strip()
                
                if content:
                    lines_in_file = content.count('\n') + 1
                    total_lines += lines_in_file
                    
                    if not content.endswith("\n"):
                        content += "\n"
                    concatenated += content
        
        logging.info(f"Concaténation terminée : {total_lines} lignes JSON au total")
        return concatenated
        
    except Exception as e:
        logging.error(f"Erreur lors de la lecture des fichiers : {str(e)}")
        raise

def get_spark_logs():
    """Récupère les logs Spark pour le diagnostic d'erreurs"""
    try:
        with open("/tmp/spark.log", "r", encoding='utf-8') as log_file:
            return log_file.read()
    except Exception as e:
        logging.warning(f"Impossible de lire les logs Spark : {str(e)}")
        return "Logs Spark non disponibles"

@app.route('/start-job', methods=['POST'])
def start_job():
    """Démarre un job Spark et retourne les résultats JSON"""
    
    job_start_time = datetime.now()
    logging.info(f"Démarrage d'un nouveau job Spark à {job_start_time}")
    
    output_dir = "/data/shared/json_output"
    
    # Vérification que le répertoire de sortie existe
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            logging.info(f"Création du répertoire de sortie : {output_dir}")
        except Exception as e:
            logging.error(f"Impossible de créer le répertoire de sortie : {str(e)}")
            return jsonify({
                "error": "Impossible de créer le répertoire de sortie",
                "details": str(e)
            }), 500
    
    # Nettoyage du répertoire de sortie
    if not cleanup_output_directory(output_dir):
        return jsonify({
            "error": "Erreur lors du nettoyage du répertoire de sortie"
        }), 500
    
    # Vérification de l'existence du script Spark
    spark_script = "/app/spark.sh"
    if not os.path.exists(spark_script):
        logging.error(f"Script Spark non trouvé : {spark_script}")
        return jsonify({
            "error": f"Script Spark non trouvé : {spark_script}"
        }), 500
    
    # Vérification des permissions d'exécution
    if not os.access(spark_script, os.X_OK):
        logging.error(f"Script Spark non exécutable : {spark_script}")
        return jsonify({
            "error": f"Script Spark non exécutable : {spark_script}"
        }), 500
    
    try:
        # Lancement du script Spark
        logging.info("Lancement du script Spark...")
        
        result = subprocess.run(
            ["./spark.sh"], 
            check=True, 
            capture_output=True, 
            text=True,
            cwd="/app",
            timeout=1800  # Timeout de 30 minutes
        )
        
        logging.info("Script Spark terminé avec succès")
        
    except subprocess.TimeoutExpired as e:
        logging.error("Timeout du script Spark (30 minutes)")
        return jsonify({
            "error": "Timeout du script Spark",
            "details": "Le traitement a pris plus de 30 minutes",
            "spark_log": get_spark_logs()
        }), 504
        
    except subprocess.CalledProcessError as e:
        logging.error(f"Erreur d'exécution du script Spark : {e}")
        
        return jsonify({
            "error": "Erreur pendant l'exécution de spark.sh",
            "details": str(e),
            "return_code": e.returncode,
            "stdout": e.stdout if e.stdout else "",
            "stderr": e.stderr if e.stderr else "",
            "spark_log": get_spark_logs()
        }), 500
    
    except Exception as e:
        logging.error(f"Erreur inattendue : {str(e)}")
        return jsonify({
            "error": "Erreur inattendue lors de l'exécution",
            "details": str(e),
            "spark_log": get_spark_logs()
        }), 500
    
    # Attente des fichiers de sortie
    files = wait_for_output_files(output_dir, timeout=60)
    
    if not files:
        return jsonify({
            "error": "Timeout : aucun fichier de sortie trouvé après 60s",
            "spark_log": get_spark_logs()
        }), 504
    
    # Lecture et concaténation des fichiers JSON
    try:
        concatenated = read_and_concatenate_json_files(files)
        
        if not concatenated.strip():
            logging.warning("Fichiers de sortie vides")
            return jsonify({
                "error": "Fichiers de sortie vides",
                "spark_log": get_spark_logs()
            }), 500
        
        job_duration = datetime.now() - job_start_time
        logging.info(f"Job terminé avec succès en {job_duration}")
        
        return Response(
            concatenated, 
            mimetype="application/json",
            headers={
                'X-Job-Duration': str(job_duration.total_seconds()),
                'X-Files-Count': str(len(files))
            }
        )
        
    except Exception as e:
        logging.error(f"Erreur lors de la lecture des fichiers : {str(e)}")
        return jsonify({
            "error": f"Erreur de lecture des fichiers : {str(e)}",
            "spark_log": get_spark_logs()
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de vérification de santé du service"""
    
    checks = {
        "service": "running",
        "spark_script": os.path.exists("/app/spark.sh"),
        "output_dir": os.path.exists("/data/shared/json_output"),
        "input_dir": os.path.exists("/data/shared/xml_input"),
        "timestamp": datetime.now().isoformat()
    }
    
    all_healthy = all(checks.values()) if isinstance(list(checks.values())[0], bool) else True
    status_code = 200 if all_healthy else 503
    
    return jsonify(checks), status_code

@app.route('/logs', methods=['GET'])
def get_logs():
    """Endpoint pour récupérer les logs Spark"""
    
    logs = {
        "spark_log": get_spark_logs(),
        "flask_log": "Voir les logs du conteneur Flask"
    }
    
    return jsonify(logs)

@app.route('/')
def index():
    """Endpoint racine avec informations sur l'API"""
    return jsonify({
        "message": "API Spark Service is running",
        "version": "1.0",
        "endpoints": {
            "POST /start-job": "Lance un job Spark et retourne les résultats JSON",
            "GET /health": "Vérification de santé du service",
            "GET /logs": "Récupération des logs Spark",
            "GET /": "Informations sur l'API"
        },
        "timestamp": datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint non trouvé",
        "message": "Vérifiez l'URL et la méthode HTTP utilisées"
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "error": "Méthode non autorisée",
        "message": "Vérifiez la méthode HTTP utilisée pour cet endpoint"
    }), 405

@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Erreur interne du serveur : {str(error)}")
    return jsonify({
        "error": "Erreur interne du serveur",
        "message": "Consultez les logs pour plus de détails"
    }), 500

# ✅ CORRECTION : Utilisation correcte de __name__
if __name__ == '__main__':
    logging.info("Démarrage du service Flask Spark")
    app.run(host="0.0.0.0", port=5000, debug=False)