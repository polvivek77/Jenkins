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
                echo "Stopping old app..."
                PID=$(lsof -t -i:5000 || true)
                [ ! -z "$PID" ] && kill -9 $PID || true
                sleep 2

                echo "Starting Flask app..."
                nohup /Jenkins/jenenv/bin/python /var/lib/jenkins/workspace/Flask-app/app.py > /var/lib/jenkins/workspace/Flask-app/app.log 2>&1 &

                sleep 5

                echo "===== LOG ====="
                cat /var/lib/jenkins/workspace/Flask-app/app.log || true

                echo "===== PORT CHECK ====="
                lsof -i:5000 || true
                '''
            }
        }
    }
}