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
                    bat 'python -m venv entorno1'
                    bat '.\\entorno1\\Scripts\\activate'
                    bat '.\\venv\\Scripts\\invoke test'
                }
            }
        }
    }
}