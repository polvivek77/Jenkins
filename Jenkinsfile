pipeline {
    agent any

    stages {

        stage('Deploy') {
            steps {
                sh '''
                echo "Python version:"
                which python3
                python3 -m pip show flask || true

                echo "Stopping app..."
                PID=$(lsof -t -i:5000 || true)
                [ ! -z "$PID" ] && kill -9 $PID || true

                echo "Starting Flask..."

                nohup python3 app.py > app.log 2>&1 &

                sleep 5

                echo "---- LOG ----"
                cat app.log || true

                echo "---- PORT CHECK ----"
                lsof -i:5000 || true
                '''
            }
        }
    }
}