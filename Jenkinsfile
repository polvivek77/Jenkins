pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/polvivek77/Jenkins.git'
            }
        }

        stage('Deploy Streamlit') {
            steps {
                sh '''

                python3 -m venv venv

                ./venv/bin/pip install -r requirements.txt

                nohup ./venv/bin/streamlit run app.py \
                --server.address 0.0.0.0 \
                --server.port 8501 \
                > streamlit.log 2>&1 &
                '''
            }
        }
    }
}