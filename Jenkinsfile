pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
		pollSCM '* * * * *'
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
                cd app
                python3 app.py
                python3 app.py --name=Endra
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