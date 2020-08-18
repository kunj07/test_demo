pipeline {
	agent any
	stages {
		stage('CheckOut Stage') {
			steps {
				echo 'Updates files in the working tree to match the version in the index or the specified tree.'
				checkout scm
			}
		}
		stage ('Build Stage') {
			steps {
				echo 'first step is to install python'
				sh 'sudo yum install python3'
				echo 'Creating a virtual environment'
				sh 'sudo yum install python-virtualenv'
				sh 'virtualenv myvirtualenv'
				sh 'source myvirtualenv/bin/activate'
				echo 'Running the unit test case file'
				sh 'python test_employee.py'
				
			}
		}
	}
}
