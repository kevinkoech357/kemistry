pipeline {
    agent any
    
    triggers {
        pollSCM '*/5 * * * *'
    }
      
    tools {
        jdk 'jdk17'
    }
    
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }
    
    stages {
        stage('Git Pull Source Code') {
            steps {
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/kevinkoech357/kemistry'
            }
        }
        
        stage('OWASP Scan') {
            steps {
                dependencyCheck additionalArguments: '--scan ./', odcInstallation: 'OWASP Check'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
        
        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=Kemistry \
                        -Dsonar.java.binaries=. \
                        -Dsonar.projectKey=Kemistry \
                        -Dsonar.coverage.exclusions='**/*' \
                        -Dsonar.cpd.exclusions='**/*' '''
                }
            }
        }
    }
}