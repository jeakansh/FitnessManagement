pipeline {
    agent any

    environment {
        IMAGE_NAME = "aceest-fitness"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        
        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh "docker run --rm $IMAGE_NAME:$IMAGE_TAG pytest"
            }
        }

        stage('Load Image into Minikube') {
            steps {
             sh '/usr/local/bin/minikube image load $IMAGE_NAME:$IMAGE_TAG'
            }
        }

         stage('Deploy to Kubernetes') {
            steps {
                sh """
                kubectl set image deployment/fitness-app \
                fitness-container=$IMAGE_NAME:$IMAGE_TAG \
                || kubectl apply -f k8s/
                """
            }
        }

        stage('Verify Deployment') {
            steps {
                sh "kubectl rollout status deployment/fitness-app"
            }
        }
    }
}