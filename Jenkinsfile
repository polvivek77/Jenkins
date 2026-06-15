pipeline {
    agent any

    stages {

        stage('Deploy') {
            steps {
                sh '''
                echo "Stopping app on port 5000..."

                PID=$(lsof -t -i:5000 || true)
                if [ -n "$PID" ]; then
                    kill -9 $PID || true
                fi

                echo "Starting new Flask app..."
                nohup python3 app.py > app.log 2>&1 &
                '''
                }
            }
    }
}