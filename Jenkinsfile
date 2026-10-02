pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh '''
                pip3 install -r sam-app/hello_world/requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh "pytest"
            }
        }

        stage('Build') {
            steps {
                sh "sam build -t sam-app/template.yaml"
            }
        }

        stage('Deploy') {
            environment {
                AWS_DEFAULT_REGION = 'eu-north-1'
                AWS_ACCESS_KEY_ID = credentials('aws-access-key')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
            }

            steps {
                sh "sam deploy -t sam-app/template.yaml --no-confirm-changeset --no-fail-on-empty-changeset"
            }
        }
    }
}