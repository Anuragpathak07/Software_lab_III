pipeline {
    agent any
    environment {
        IMAGE_NAME = 'Anuragpathak07/studentproject'
    }
    stages {
        stage('Clone Repository') {
    steps {
        checkout([$class: 'GitSCM', 
            branches: [[name: '*/main']], 
            userRemoteConfigs: [[url: 'https://github.com/Anuragpathak07/Software_lab_III.git']]
        ])
       }
    }

    stage('Build Docker Image') {
        steps {
            sh '/usr/bin/docker build -t $IMAGE_NAME .'
        }
    }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-credentials', variable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u Anuragpathak07 --password-stdin'
                }
            }
        }
        stage('Push Image to Docker Hub') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }
    }
}
