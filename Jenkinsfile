pipeline {
    agent any

     stages {
        stage('Clone Repo') {
            steps {
             git branch :master, url = "https://github.com/Sameer-TahirM/Jenkins-mlops.git"  
            }
        }


         
    
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }}
        

      
     
        stage('Test with pytest') {
            steps {
                sh 'pytest'
            }
        }
}
