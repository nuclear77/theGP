// Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/nuclear77/theGP.git'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest app/tests/'
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook(
                    playbook: 'playbook.yml',
                    inventory: 'inventory.yml'
                )
            }
        }
    }
}