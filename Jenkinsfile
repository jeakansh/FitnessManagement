pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
             agent {
                docker {
                    image 'python:3.11'
                }
            }
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fitness-app .'
            }
        }
    }
}