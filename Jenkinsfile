pipeline {
    agent any

    stages {

        stage('Update Code') {
            steps {
                sh '''
                cd /opt/streamlit-app

                git reset --hard
                git pull origin main
                '''
            }
        }

        stage('Restart Streamlit') {
            steps {
                sh '''
                cd /opt/streamlit-app

                pkill -f streamlit || true

                nohup venv/bin/streamlit run app.py \
                --server.address 0.0.0.0 \
                --server.port 8501 \
                > streamlit.log 2>&1 &
                '''
            }
        }

    }
}