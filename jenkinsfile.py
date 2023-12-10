opipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    git clone 'git@github.com:Nuver2/jenkins-python-test.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate'
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

        stage('Deploy') {
            steps {
                script {
                    
                }
            }
        }
    }
}
