pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-fitness .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh 'docker run --rm aceest-fitness pytest'
            }
        }
    }
}