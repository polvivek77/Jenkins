pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/polvivek77/Jenkins.git'
            }
        }

        stage('Deploy Flask App') {
            steps {
                sh '''
                echo "Stopping old Flask app if running..."
                pkill -f app.py || true

                echo "Starting new Flask app..."
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}