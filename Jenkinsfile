pipeline {
    agent any

    stages {

        stage('Deploy') {
            steps {
                sh '''
                echo "Stopping app on port 5000..."

                PID=$(lsof -t -i:5000 || true)

                if [ ! -z "$PID" ]; then
                    kill -9 $PID || true
                fi

                echo "Starting Flask app..."

                nohup python3 app.py > app.log 2>&1 &
                
                sleep 3

                lsof -i:5000 || echo "App failed to start"
                '''
            }
        }
    }
}