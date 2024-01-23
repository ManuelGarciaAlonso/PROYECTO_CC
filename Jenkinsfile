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

        stage('Test') {
            steps {
                script {
                    bat 'pip3 --install --upgrade pip'
                    bat 'pip3 install numpy pytest'
                    bat 'pip install -r requirements.txt'  
                    bat 'C:\\Users\\manga\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\invoke test'
                    }
            }
        }
    }
}