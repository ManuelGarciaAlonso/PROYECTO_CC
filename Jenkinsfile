pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'gaalm/imagen_proyecto_cc:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup'){
        steps{
            bat 'pip install -r requirements.txt'  
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'C:\\Users\\manga\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\invoke test'
                    }
            }
        }
    }
}