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
                    bat 'cd tests && C:\\Users\\manga\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pytest.exe'
                    bat 'C:\\Users\\manga\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pytest.exe && python -m venv entorno1 && .\\entorno1\\Scripts\\activate && .\\venv\\Scripts\\invoke test'
                    }
            }
        }
    }
}