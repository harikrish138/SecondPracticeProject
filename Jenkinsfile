pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code from GitHub"
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Running sample build step"
                sh 'echo Hello from Jenkins pipeline!'
            }
        }

        stage('Test') {
            steps {
                echo "Running sample tests"
                sh 'echo No real tests yet...'
            }
        }
    }
}
