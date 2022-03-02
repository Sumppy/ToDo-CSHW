pipeline {
  agent any
  options {
    ansiColor('xterm')
  }

  environment {
    /*---AWS ECR Credentials---*/
    REGISTRY = '012723603030.dkr.ecr.eu-central-1.amazonaws.com'  // An existing ECR registry name where images will be pushed
    REGISTRY_CREDENTIAL = 'jenkins-AWS-access'                 // Jenkins credentialsID for AWS access
    ECR_REPOSITORY = 'cshw'                            // ECR repository name
    ECR_REGION = 'eu-central-1'                                   // AWS region

    /*---Docker Build configuration---*/
    VERSION = 'latest'

    /*---Github Config---*/
    BRANCH_NAME = 'main'
    SCM_CREDENTIALS = 'Github-SSH-key'                                 // Credentials ID stored in Jenkins
    REPOSITORY_URL = 'git@github.com:Sumppy/ToDo-CSHW.git'
  }

  stages {
    stage('Source'){
      steps {
        git branch: "${BRANCH_NAME}",
            credentialsId: "${SCM_CREDENTIALS}",
            url: "${REPOSITORY_URL}"
      }
    }

    stage('Build') {
      steps {
        sh """
          docker info
          docker build -t ${ECR_REPOSITORY}:${BUILD_NUMBER} .
          docker tag ${ECR_REPOSITORY}:${BUILD_NUMBER} ${REGISTRY}/${ECR_REPOSITORY}:${VERSION}
          docker images
        """
      }
    }

    stage('Deploy') {
      steps {
        sh "echo \033[33m Deploy ${ECR_REPOSITORY}:${BUILD_NUMBER} to AWS ECR \033[0m"
        script {
          docker.withRegistry("https://${REGISTRY}", "ecr:${ECR_REGION}:${REGISTRY_CREDENTIAL}") {
              docker.image("${REGISTRY}/${ECR_REPOSITORY}").push("${VERSION}")
          }
        }
      }
    }
  }

  post {
    success {
      sh "echo \033[32m Successfully builded docker image and pushed it to ECR." 
    }
    failure {
      sh 'echo \033[31m Failed \033[0m'
    }
  }
}