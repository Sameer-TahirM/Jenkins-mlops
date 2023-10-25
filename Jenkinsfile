pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                script {
                    // Checkout the 'master' branch from the specified Git repository
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/Sameer-TahirM/Jenkins-mlops.git']]])
                }
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test with pytest') {
            steps {
                sh 'pytest'
            }
        }
    }
}
