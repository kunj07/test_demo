pipeline {
	agent any
	stages {
		stage ('CleanUp Stage') {
			steps {
				echo 'CleanUp of existing code and folder in jenkins'
				//cleanWs()
			}
		}
		stage('CheckOut Stage') {
			steps {
				echo 'Updates files in the working tree to match the version in the index or the specified tree.'
				checkout scm
			}
		}
		stage ('Build Stage') {
			steps {
				sh 'sudo su'
				sh 'sudo yum update'
				echo 'Creating a virtual environment'
				sh 'sudo yum install python-virtualenv'
				sh 'virtualenv myvirtualenv'
				sh 'source myvirtualenv/bin/activate'
				echo 'Installing python and other packages'
				sh 'sudo yum install python3'
				echo 'Running the unit test case file'
				sh 'python test_employee.py'
			}
		}
		stage ('Deploy Stage') {
			steps {
				sh "sudo scp -i  '$WORKSPACE/Q20908-new.pem' -o StrictHostKeyChecking=no -r employee.py ec2-user@54.162.194.92:/home/ec2-user"
				sh "sudo scp -i  '$WORKSPACE/Q20908-new.pem' -o StrictHostKeyChecking=no -r test_employee.py ec2-user@54.162.194.92:/home/ec2-user"
				sh '''sudo ssh -i "Q20908-new.pem" -o StrictHostKeyChecking=no ec2-user@ec2-54-162-194-92.compute-1.amazonaws.com 
				echo "Hello world" 
				sudo yum install python3
				sudo yum install python-virtualenv
				virtualenv env
				source env/bin/activate
				sudo pip3 install unittest2
				python3 test_employee.py
				sudo pip3 install pylint
				python3 -m pylint employee.py
				<<EOT'''
				echo 'Hello'
			}
		}
	}
}
