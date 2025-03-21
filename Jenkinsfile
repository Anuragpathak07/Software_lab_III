pipeline {
    agent any
    environment {
        IMAGE_NAME = 'anuragpathak07/studentproject'
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
                sh "docker build -t ${env.IMAGE_NAME} ."
            }
        }

    stage('Login to Docker Hub') {
            steps {
                   withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                   sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
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
