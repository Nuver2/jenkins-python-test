pipeline {
    agent any
    
    stages {
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
