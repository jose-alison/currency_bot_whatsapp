pipeline {
    agent any

    stages {
        stage ('Pull Image') {
            steps {
                script {
                    sh 'git pull origin main'
                }
            }
        }
        stage('Build Image') {
            steps {
                script {
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run Project') {
            steps {
                script {
                    sh '. venv/bin/activate && python main.py'
                }
            }
        }
    }
}