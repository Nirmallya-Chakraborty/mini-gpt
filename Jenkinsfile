pipeline {
    agent any

    environment {
        KUBECONFIG = "/var/lib/jenkins/kubeconfig"

        IMAGE_BACKEND = "nirmallyachakraborty/mini-gpt-backend:latest"
        IMAGE_FRONTEND = "nirmallyachakraborty/mini-gpt-frontend:latest"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Nirmallya-Chakraborty/mini-gpt.git'
            }
        }

        stage('Build Images') {
            steps {
                sh '''
                set -e

                echo "Building backend image..."
                docker build -t $IMAGE_BACKEND ./backend

                echo "Building frontend image..."
                docker build -t $IMAGE_FRONTEND ./frontend
                '''
            }
        }

        stage('Push Images') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    set -e

                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                    echo "Pushing backend image..."
                    docker push $IMAGE_BACKEND

                    echo "Pushing frontend image..."
                    docker push $IMAGE_FRONTEND
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                set -e

                echo "Applying Kubernetes manifests..."
                kubectl apply -f k8s/ --validate=false

                echo "Restarting deployments..."
                kubectl rollout restart deployment backend || true
                kubectl rollout restart deployment frontend || true
                kubectl rollout restart deployment ollama || true

                echo "Waiting for backend rollout..."
                kubectl rollout status deployment backend || true

                echo "Waiting for frontend rollout..."
                kubectl rollout status deployment frontend || true
                '''
            }
        }

        stage('Verify Cluster') {
            steps {
                sh '''
                echo "========= NODES ========="
                kubectl get nodes -o wide

                echo "========= PODS ========="
                kubectl get pods -o wide

                echo "========= SERVICES ========="
                kubectl get svc -o wide
                '''
            }
        }
    }

    post {

        success {
            echo "?? Mini GPT deployed successfully!"
        }

        failure {
            echo "? Pipeline failed — check logs"
        }
    }
}