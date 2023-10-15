pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test with pytest') {
            steps {
                script {
                    sh 'pytest'
                }
            }
        }
    }
}
