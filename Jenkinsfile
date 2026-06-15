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

        stage('Deploy Flask App') {
            steps {
                sh '''
                echo "Stopping old Flask app..."

                if [ -f app.pid ]; then
                    kill $(cat app.pid) || true
                    rm -f app.pid
                fi

                echo "Starting new Flask app..."

                nohup python3 app.py > app.log 2>&1 &
                echo $! > app.pid
                '''
            }
        }
    }
}