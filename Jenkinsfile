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
            script{
            bat 'pip3 --install --upgrade pip'
            bat 'pip3 install numpy pytest'
            bat 'python -m pytest test.py'
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