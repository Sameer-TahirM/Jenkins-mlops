pipeline {
    agent any

    stages {
        stage('Checkout code') {
            steps {
                script {
                    // Equivalent to 'actions/checkout@v2'
                    checkout scm
                }
            }
        }

        stage('Install dependancies') {
            steps {
                script {
                    // Equivalent to 'install'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test with pytest') {
            steps {
                script {
                    // Equivalent to 'pytest'
                    sh 'pytest'
                }
            }
        }
    }
    
    post {
        success {
            // Add any post-success steps or notifications if needed
        }
    }
}
