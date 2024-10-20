pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your-django-app:latest'
        DOCKER_REGISTRY = 'your-docker-registry-url'
        EC2_HOST = 'your-ec2-public-ip'
        EC2_USER = 'ec2-user'  // Update based on your EC2 instance's username (e.g., ubuntu for Ubuntu instances)
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/your-django-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").inside {
                        sh 'python manage.py test'
                    }
                }
            }
        }

        stage('Push to Docker Registry') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-credentials-id') {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    // SSH into the EC2 instance and run deployment commands
                    sshagent(credentials: ['ec2-ssh-credentials-id']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} '
                        docker pull ${DOCKER_REGISTRY}/${DOCKER_IMAGE} &&
                        docker stop django-app || true &&
                        docker rm django-app || true &&
                        docker run -d --name django-app -p 8000:8000 ${DOCKER_REGISTRY}/${DOCKER_IMAGE}
                        '
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker image prune -f'
        }
        success {
            echo 'Pipeline succeeded. Application deployed to EC2!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for more details.'
        }
    }
}
