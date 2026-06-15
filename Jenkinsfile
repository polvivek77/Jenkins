pipeline {
    agent any

    stages {

        stage('Clean') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/polvivek77/Jenkins.git'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                mkdir -p /var/www/html

                cp index.html /var/www/html/index.html
                '''
            }
        }
    }
}