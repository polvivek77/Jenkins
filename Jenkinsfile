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
                /var/lib/jenkins/workspace/Flask-app/jenenv/bin/pip install -r requirements.txt --quiet
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Stopping old app..."
                PID=$(lsof -t -i:5000 || true)
                [ ! -z "$PID" ] && kill -9 $PID || true
                sleep 2

                echo "Starting Flask app..."
                nohup /var/lib/jenkins/workspace/Flask-app/jenenv/bin/python app.py > app.log 2>&1 &

                sleep 5

                echo "===== LOG ====="
                cat app.log || true

                echo "===== PORT CHECK ====="
                lsof -i:5000 || true
                '''
            }
        }
    }
}