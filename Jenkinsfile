pipeline {
	agent any
	stages {
		stage('CheckOut Stage') {
			steps {
				echo 'Updates files in the working tree to match the version in the index or the specified tree.'
				sh 'git checkout -b master'
			}
		}
		stage ('Build Stage') {
			steps {
				echo 'Hi, this is the build stage'
			}
		}
	}
}
