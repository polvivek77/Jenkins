pipeline {

    agent any

    stages {

        stage('Setup Python Environment') {

            steps {

                sh '''
                python3 -m venv venv

                . venv/bin/activate

                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy Streamlit') {

            steps {

                sh '''
                pkill -f streamlit || true

                nohup ./venv/bin/streamlit run app.py \
                --server.address 0.0.0.0 \
                --server.port 8501 \
                > streamlit.log 2>&1 &
                '''
            }
        }

    }

}