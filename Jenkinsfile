pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                /Jenkins/jenenv/bin/pip install -r requirements.txt --quiet
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Restarting Flask service..."
                sudo systemctl restart flask-app
                sleep 3
                sudo systemctl status flask-app
                '''
            }
        }
    }
}