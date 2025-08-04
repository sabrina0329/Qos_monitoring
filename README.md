<<<<<<< HEAD
# Qos_monitoring
<<<<<<< HEAD
Built with: Apache NiFi, Apache Spark , Elasticsearch, and Kibana — powering an automated, end-to-end ETL pipeline for real-time KPI monitoring and visualization in mobile networks.
=======



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/mlops6983803/qos_monitoring.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/mlops6983803/qos_monitoring/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/user/project/merge_requests/auto_merge/)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
<<<<<<< HEAD
>>>>>>> d955836 (Initial commit)
=======
=======
<h1>Intelligent QoS Management & Predictive Analytics for Telecom Networks</h1>

<p>An end-to-end data pipeline using Apache NiFi, Apache Spark, Elasticsearch, and Kibana to provide AI-driven Quality of Service (QoS) monitoring, forecasting, and anomaly detection for telecommunication networks. This project was developed as a Final Year Project in collaboration with Orange Tunisie.</p>

<p align="center">
  <img src="path/to/your/architecture_diagram.png" alt="High-Level Architecture" width="800">
  <br>
  <em><b>Note:</b> You must create and link your own architecture diagram here.</em>
</p>

<hr>

<h2> Features</h2>

<ul>
  <li><b>Automated Data Pipeline:</b> Ingests raw QoS data files using <b>NiFi</b>, processes them in a distributed manner with <b>Spark</b>, and indexes them into <b>Elasticsearch</b>.</li>
  <li><b>AI-Powered Insights:</b>
    <ul>
      <li><b>Time Series Forecasting:</b> Utilizes models like ARIMA, SARIMA, Prophet, and LSTM to predict key KPIs such as user load.</li>
      <li><b>Unsupervised Anomaly Detection:</b> Employs Isolation Forest and Autoencoders to identify unusual patterns and potential network faults.</li>
    </ul>
  </li>
  <li><b>Experiment Tracking:</b> Leverages <b>MLflow</b> for rigorous tracking of all AI model experiments, including parameters, metrics, and artifacts.</li>
  <li><b>Interactive Visualization:</b>
    <ul>
      <li><b>Kibana:</b> Operational dashboards for real-time QoS monitoring, KPI trends, and geospatial analysis.</li>
      <li><b>Streamlit:</b> Dedicated dashboards for in-depth analysis and comparison of AI model performance, directly loading artifacts from MLflow.</li>
    </ul>
  </li>
  <li><b>Containerized & Automated Deployment:</b> The entire stack is containerized with <b>Docker</b> and orchestrated with <b>Docker Compose</b>. A <code>start-stack.sh</code> script automates the entire startup process, including dynamic Kibana token generation.</li>
</ul>

<hr>

<h2>️ Technology Stack</h2>

<table width="100%">
  <thead>
    <tr>
      <th>Category</th>
      <th>Technologies & Tools</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Data Ingestion & Flow</b></td>
      <td>Apache NiFi</td>
    </tr>
    <tr>
      <td><b>Distributed Processing</b></td>
      <td>Apache Spark (PySpark)</td>
    </tr>
    <tr>
      <td><b>Data Storage & Indexing</b></td>
      <td>Elasticsearch</td>
    </tr>
    <tr>
      <td><b>Visualization & Reporting</b></td>
      <td>Kibana, Streamlit, Matplotlib, Seaborn</td>
    </tr>
    <tr>
      <td><b>AI / Machine Learning</b></td>
      <td>Scikit-learn, TensorFlow/Keras, Statsmodels, Prophet, Pandas, NumPy</td>
    </tr>
    <tr>
      <td><b>MLOps & Deployment</b></td>
      <td>MLflow, Docker, Docker Compose, Bash Scripting</td>
    </tr>
    <tr>
      <td><b>API & Backend</b></td>
      <td>Flask</td>
    </tr>
    <tr>
      <td><b>Version Control</b></td>
      <td>Git, GitHub</td>
    </tr>
  </tbody>
</table>

<hr>

<h2> Project Structure</h2>

<pre><code>.
├── docker-compose.yml          # Main Docker Compose configuration
├── start-stack.sh              # Primary script to start the entire stack
├── .env                        # (Auto-generated by start-stack.sh for Kibana token)
├── data/                       # Host directory for persistent data
│   ├── staging/
│   ├── landing/
│   ├── processed/
│   └── ...
├── init/                       # Docker context for Elasticsearch index creation
├── kibana-init/                # Docker context for Kibana dashboard import
│   └── kibana-objects.ndjson   # <-- IMPORTANT: Your exported Kibana objects go here
├── nifi-init/                  # Docker context for custom NiFi setup
├── spark_service/              # Docker context for the PySpark Flask application
└── ...
</code></pre>

<hr>

<h2>⚙️ Setup and Installation</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Docker & Docker Compose</li>
  <li>Git</li>
  <li>A Bash-compatible shell (Linux, macOS, Git Bash on Windows)</li>
  <li><code>curl</code> utility</li>
</ul>

<h3>1. Clone the Repository</h3>
<pre><code>git clone <your_repository_url>
cd <your_repository_directory>
</code></pre>

<h3>2. Prepare Kibana Objects (Mandatory)</h3>
<p>You must export your dashboards, visualizations, and data views from your development Kibana instance.</p>
<ul>
  <li>Save the exported file as <code>kibana-init/kibana-objects.ndjson</code>.</li>
  <li><b>Ensure you include all related objects during the export.</b></li>
</ul>

<h3>3. Set Host Directory Permissions</h3>
<p>For Docker containers to write to the <code>./data</code> directory on your host, you may need to set permissions. The <code>start-stack.sh</code> script will attempt to do this.</p>
<pre><code># This is handled by the start script, but can be run manually if needed
sudo chmod -R 777 ./data
</code></pre>
<p><i>Note: This is for development convenience. The <code>docker-compose.yml</code> also uses the <code>:z</code> flag for SELinux compatibility.</i></p>

<hr>

<h2>▶️ Running the Stack</h2>

<p>The <code>start-stack.sh</code> script automates the entire startup sequence, including generating the dynamic Kibana token.</p>

<p><b>1. Make the script executable:</b></p>
<pre><code>chmod +x start-stack.sh
</code></pre>

<p><b>2. Run the script:</b></p>
<pre><code>./start-stack.sh
</code></pre>

<hr>

<h2> Accessing Services</h2>

<p>Once the stack is running, services can be accessed at the following URLs:</p>
<ul>
  <li><b>NiFi UI:</b> <code>https://localhost:8443/nifi</code></li>
  <li><b>Kibana UI:</b> <code>http://localhost:5601</code></li>
  <li><b>Elasticsearch API:</b> <code>http://localhost:9200</code></li>
  <li><b>Spark Master UI:</b> <code>http://localhost:8081</code></li>
  <li><b>Spark Application UI (for active jobs):</b> <code>http://localhost:4041</code></li>
  <li><b>MLflow UI (if running as a service):</b> <code>http://localhost:5000</code> (or configured port)</li>
  <li><b>Streamlit Dashboards:</b> <code>http://localhost:8501</code> / <code>http://localhost:8502</code> (depending on how you run them)</li>
</ul>

<hr>

<h2>⏹️ Stopping the Stack</h2>

<p>To stop all services and remove the containers:</p>
<pre><code>docker-compose down
</code></pre>

<p>To perform a full cleanup, including removing named volumes (<b>WARNING:</b> deletes Elasticsearch data, NiFi state, etc.):</p>
<pre><code>docker-compose down -v
rm -f .env # Also remove the auto-generated environment file
</code></pre>

<hr>

<h2> Key AI System Components</h2>
<ul>
  <li><b>Comparative Model Evaluation:</b> The project includes scripts to train and evaluate multiple forecasting (ARIMA, Prophet, LSTM) and anomaly detection (Isolation Forest, Autoencoder) models on a per-governorate basis.</li>
  <li><b>MLflow Tracking:</b> All experiments are tracked in MLflow, logging parameters, metrics (RMSE), and artifacts (models, plots, prediction files).</li>
  <li><b>Streamlit Dashboards for Analysis:</b> Interactive dashboards allow for the visual comparison of AI model performance by loading artifacts directly from MLflow.</li>
</ul>

<hr>

<h2> Future Work</h2>
<ul>
  <li>Operationalize the AI Inference Service to write live predictions back to Elasticsearch.</li>
  <li>Implement a real-time alerting module based on AI insights.</li>
  <li>Transition the pipeline to a streaming architecture for lower latency.</li>
  <li>Mature MLOps practices with automated model retraining and drift detection.</li>
</ul>
>>>>>>> 216607d ( premier commit)
>>>>>>> 38b021f ( premier commit)
