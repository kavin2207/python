pipeline{
  agent any
  stages{
    stage('version'){
      steps{
        bat 'docker build -t pythonApp .'
        bat 'docker run -it --rm --name myApp pythonApp'
      }
    }
  
  }




}
