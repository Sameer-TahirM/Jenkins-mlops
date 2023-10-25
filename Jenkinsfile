pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/Sameer-TahirM/Jenkins-mlops.git']])
                }
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt' // Install Python packages
            }
        }

        stage('Test with pytest') {
            steps {
                sh 'pytest'
            }
        }
    }
}
