pipeline {
    agent any

     stages {
        stage('Clone Repo') {
            steps {
             git branch :master, url = "https://github.com/Sameer-TahirM/Jenkins-mlops.git"  
            }
        }

    
    stages {
        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

      
     
        stage('Test with pytest') {
            steps {
                bat 'pytest'
            }
        }
    }
}
