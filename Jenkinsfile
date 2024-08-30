pipeline {
    agent any

    stages {
        stage ('Pull Image') {
            steps {
                script {
                    sh 'git fetch'
                    sh 'git pull'
                }
            }
        }
        stage('Build Image') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run Project') {
            steps {
                script {
                    sh '. venv/bin/activate && python3 main.py'
                }
            }
        }
    }
}