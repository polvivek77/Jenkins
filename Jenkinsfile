pipeline {
    agent any

    stages {

        stage('Deploy') {
            steps {
                sh '''
                echo "Stopping old app..."

                PID=$(lsof -t -i:5000 || true)
                [ ! -z "$PID" ] && kill -9 $PID || true

                echo "Starting Flask using VENV python..."

                nohup /Jenkins/jenenv/bin/python app.py > app.log 2>&1 &

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