pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'eu-north-1'
        AWS_ACCESS_KEY_ID = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        AWS_SAM_STACK_NAME = 'jenkins-lambda-deployment'
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                python3 -m venv .venv
                .venv/bin/pip install --upgrade pip
                .venv/bin/pip install -r sam-app/hello_world/requirements.txt
                '''
            }
        }

        stage('Unit Test') {
            steps {
                sh ".venv/bin/python -m pytest sam-app/tests/unit"
            }
        }

        stage('Build') {
            steps {
                sh "sam build -t sam-app/template.yaml"
            }
        }

        stage('Deploy') {

            steps {
                sh "sam deploy -t sam-app/template.yaml --no-confirm-changeset --no-fail-on-empty-changeset"
            }
        }

        stage('Integration Test') {
            steps {
                sh '''
                    .venv/bin/python -m pytest sam-app/tests/integration
                '''
            }
        }
    }
}