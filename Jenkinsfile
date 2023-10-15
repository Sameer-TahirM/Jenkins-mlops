pipeline {
    agent any



    environment {
       PATH = "/usr/bin:$PATH"
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
