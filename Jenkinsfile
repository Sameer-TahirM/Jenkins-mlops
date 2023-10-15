pipeline {
    agent {
        docker {
            image 'ubuntu' // Use an Ubuntu image or any other Linux distribution
        }
    }
    
    stages {
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
