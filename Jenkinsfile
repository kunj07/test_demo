pipeline {
	agent any
	stages {
		stage ('CleanUp Stage') {
			steps {
				echo 'CleanUp of existing code and folder in jenkins'
				cleanWs()
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
				echo 'first step is to install python'
				sh 'sudo su'
				sh 'sudo yum install python3'
				echo 'Install all the python packages'
				sh 'sudo pip install pylint'
				sh 'sudo pip install unittest2'
				echo 'Creating a virtual environment'
				sh 'source myvirtualenv/bin/activate'
				echo 'Running the pylint package'
				sh 'pylint employee.py'
				echo 'Running the unit test case file'
				sh 'python test_employee.py'
				
			}
		}
	}
}
