##  Windows Dockerized Airflow Setup Guide
### Prerequisites
Before proceeding with the installation, make sure you have installed Docker Desktop on your machine. If you have not installed it already, you can download it from here.

### Installation
1. Download the docker.zip file and extract it to the following path: **'C:\Users\[YOUR_USER_NAME]\docker'**

2. Once you have extracted the zip file, navigate to **'C:\Users\[YOUR_USER_NAME]\docker\airflow'** folder and run the following command:
`docker-compose up airflow-init`

3. After the initialization process completes, run the following command to start the Airflow webserver:
`docker-compose up`

4. Wait for Airflow to start. Once it's up and running, navigate to **localhost:8080** or **127.0.0.1:8080** from your browser to access the Airflow UI.

5. Login to the Airflow UI using the following credentials:
`Username: airflow
Password: airflow`

6. Once you are logged in to the Airflow UI, run the sample job to load the sample data and export it to the output folder given in **C:\Users\[YOUR_USER_NAME]\docker\airflow\dags\includes\py_scripts\output**.

Congratulations! You have successfully installed and set up Dockerized Airflow on your machine.
