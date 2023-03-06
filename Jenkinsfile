pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
		pollSCM '*/5 * * * *'
	}
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd app
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 app.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}