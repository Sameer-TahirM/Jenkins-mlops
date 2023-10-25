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
                sh 'python3 -m venv venv' // Create a virtual environment
                sh 'source venv/bin/activate' // Activate the virtual environment
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
