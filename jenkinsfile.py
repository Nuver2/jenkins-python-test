pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    git 'https://github.com/Nuver2/jenkins-python-test.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'python setup.py sdist'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python -m pytest'
                }
            }
        }
    }
}
