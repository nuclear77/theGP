// Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git '*'
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
                    playbook: 'ansible/playbook.yml',
                    inventory: 'ansible/inventory.yml'
                )
            }
        }
    }
}