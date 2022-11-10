pipeline{
  agent any
  stages{
    stage('version'){
      steps{
        bat 'docker build -t python_app .'
        bat 'docker run -it --rm --name myapp python_app'
      }
    }
  
  }




}
