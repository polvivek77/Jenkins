pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                deleteDir()
                git branch: 'main',
                    url: 'https://github.com/polvivek77/Jenkins.git'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cp -r . /var/lib/jenkins/workspace/Flask-app/
                bash restart.sh
                '''
            }
        }
    }
}