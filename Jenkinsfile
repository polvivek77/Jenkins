pipeline {
    agent any

    stages {

        stage('Deploy') {
            steps {
                sh '''
                set -e

                echo "Stopping old app..."
                PID=$(lsof -t -i:5000 || true)
                [ ! -z "$PID" ] && kill -9 $PID || true

                echo "Starting Flask..."
                cd $WORKSPACE

                nohup python3 app.py > app.log 2>&1 &

                sleep 5

                echo "---- LOGS ----"
                tail -50 app.log || true

                echo "---- CHECK PORT ----"
                lsof -i:5000 || true
                '''
            }
        }
    }
}