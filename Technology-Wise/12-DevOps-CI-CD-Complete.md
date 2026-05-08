# DEVOPS CI/CD - COMPREHENSIVE INTERVIEW Q&A

## Jenkins, GitLab CI/CD, Ansible

---

## Q1: Jenkins Pipeline Overview

**A:** Automation server for CI/CD pipelines.

### Declarative Pipeline Example:
```groovy
pipeline {
    agent any
    
    options {
        timestamps()
        timeout(time: 1, unit: 'HOURS')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'prod'], description: 'Target env')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh '''
                    echo "Building application..."
                    mvn clean compile
                '''
            }
        }
        
        stage('Test') {
            when {
                expression { params.RUN_TESTS == true }
            }
            steps {
                sh '''
                    echo "Running tests..."
                    mvn test
                    mvn verify
                '''
            }
            post {
                always {
                    junit '**/target/surefire-reports/*.xml'
                    jacoco(
                        execFilePattern: 'target/jacoco.exec',
                        classPattern: 'target/classes'
                    )
                }
            }
        }
        
        stage('Quality Analysis') {
            steps {
                sh '''
                    mvn sonar:sonar \
                        -Dsonar.projectKey=my-app \
                        -Dsonar.host.url=http://sonarqube:9000 \
                        -Dsonar.login=${SONAR_TOKEN}
                '''
            }
        }
        
        stage('Package') {
            steps {
                sh '''
                    mvn clean package -DskipTests
                    docker build -t my-registry/my-app:${BUILD_NUMBER} .
                    docker tag my-registry/my-app:${BUILD_NUMBER} my-registry/my-app:latest
                '''
            }
        }
        
        stage('Push to Registry') {
            steps {
                withDockerRegistry([credentialsId: 'docker-credentials']) {
                    sh '''
                        docker push my-registry/my-app:${BUILD_NUMBER}
                        docker push my-registry/my-app:latest
                    '''
                }
            }
        }
        
        stage('Deploy to ${ENVIRONMENT}') {
            steps {
                sh '''
                    kubectl set image deployment/my-app \
                        my-app=my-registry/my-app:${BUILD_NUMBER} \
                        -n ${ENVIRONMENT}
                    kubectl rollout status deployment/my-app -n ${ENVIRONMENT}
                '''
            }
        }
        
        stage('Smoke Test') {
            steps {
                sh '''
                    sleep 10
                    curl -f http://my-app.${ENVIRONMENT}.svc.cluster.local:8080/actuator/health
                    echo "Service is healthy"
                '''
            }
        }
    }
    
    post {
        failure {
            emailext (
                subject: "Build ${env.BUILD_NUMBER} FAILED",
                body: "Check console: ${env.BUILD_URL}",
                to: "team@example.com"
            )
            slackSend(color: 'danger', message: "Build failed: ${env.BUILD_URL}")
        }
        success {
            slackSend(color: 'good', message: "Build succeeded")
        }
        always {
            cleanWs()
        }
    }
}
```

### Shared Library (Reusable Pipeline Code):
```groovy
// vars/deploy.groovy
def call(String environment) {
    sh '''
        kubectl set image deployment/my-app \
            my-app=my-registry/my-app:${BUILD_NUMBER} \
            -n ${environment}
        kubectl rollout status deployment/my-app -n ${environment}
    '''
}

// Usage in pipeline
@Library('shared-library') _
pipeline {
    stages {
        stage('Deploy') {
            steps {
                deploy('prod')
            }
        }
    }
}
```

---

## Q2: GitLab CI/CD Pipeline

**A:** Built-in CI/CD with GitLab.

### .gitlab-ci.yml Configuration:
```yaml
stages:
  - build
  - test
  - quality
  - package
  - deploy

variables:
  REGISTRY: "my-registry"
  IMAGE_NAME: "my-app"
  JAVA_OPTS: "-Xms256m -Xmx512m"

build:
  stage: build
  image: maven:3.8-openjdk-17
  cache:
    paths:
      - ~/.m2/repository
  script:
    - mvn clean compile
  artifacts:
    paths:
      - target/
    expire_in: 1 hour

test:
  stage: test
  image: maven:3.8-openjdk-17
  cache:
    paths:
      - ~/.m2/repository
  script:
    - mvn test verify
  coverage: '/TOTAL.*?([0-9]{1,3})%/'
  artifacts:
    reports:
      junit: target/surefire-reports/TEST-*.xml
      coverage_report:
        coverage_format: cobertura
        path: target/site/cobertura/coverage.xml

sonarqube:
  stage: quality
  image: maven:3.8-openjdk-17
  cache:
    paths:
      - ~/.m2/repository
  script:
    - mvn sonar:sonar
        -Dsonar.projectKey=my-app
        -Dsonar.host.url=$SONAR_HOST_URL
        -Dsonar.login=$SONAR_TOKEN
  only:
    - merge_requests
    - master

package:
  stage: package
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - docker login -u $REGISTRY_USER -p $REGISTRY_PASSWORD $REGISTRY
  script:
    - docker build -t $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA .
    - docker push $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA
    - docker tag $REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA $REGISTRY/$IMAGE_NAME:latest
    - docker push $REGISTRY/$IMAGE_NAME:latest

deploy_staging:
  stage: deploy
  image: alpine/k8s:latest
  environment:
    name: staging
    kubernetes:
      namespace: staging
  script:
    - kubectl config use-context my-cluster
    - kubectl set image deployment/my-app my-app=$REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA -n staging
    - kubectl rollout status deployment/my-app -n staging
  only:
    - develop

deploy_production:
  stage: deploy
  image: alpine/k8s:latest
  environment:
    name: production
    kubernetes:
      namespace: production
  script:
    - kubectl config use-context my-cluster
    - kubectl set image deployment/my-app my-app=$REGISTRY/$IMAGE_NAME:$CI_COMMIT_SHA -n production
    - kubectl rollout status deployment/my-app -n production
  when: manual  # Require manual approval
  only:
    - master
```

---

## Q3: Ansible Infrastructure Automation

**A:** Infrastructure as Code (IaC) for configuration management.

### Inventory File (hosts.ini):
```ini
[webservers]
web1.example.com ansible_user=ec2-user ansible_ssh_private_key_file=/path/to/key.pem
web2.example.com ansible_user=ec2-user

[databases]
db1.example.com ansible_user=ubuntu
db2.example.com ansible_user=ubuntu

[all:vars]
ansible_connection=ssh
ansible_port=22
```

### Playbook Example:
```yaml
---
- name: Deploy Spring Boot Application
  hosts: webservers
  become: yes  # Run as root
  
  vars:
    app_version: "1.0.0"
    app_user: "appuser"
    app_home: "/opt/myapp"
  
  tasks:
    - name: Update system packages
      yum:
        name: "*"
        state: latest
      when: ansible_os_family == "RedHat"
    
    - name: Install Java 17
      yum:
        name: java-17-openjdk-devel
        state: present
    
    - name: Create application user
      user:
        name: "{{ app_user }}"
        shell: /bin/nologin
        home: "{{ app_home }}"
    
    - name: Create application directory
      file:
        path: "{{ app_home }}"
        owner: "{{ app_user }}"
        group: "{{ app_user }}"
        mode: '0755'
        state: directory
    
    - name: Copy JAR file
      copy:
        src: "builds/myapp-{{ app_version }}.jar"
        dest: "{{ app_home }}/app.jar"
        owner: "{{ app_user }}"
        group: "{{ app_user }}"
        mode: '0755'
    
    - name: Copy environment config
      template:
        src: application.properties.j2
        dest: "{{ app_home }}/application.properties"
        owner: "{{ app_user }}"
        group: "{{ app_user }}"
        mode: '0600'
    
    - name: Create systemd service
      template:
        src: myapp.service.j2
        dest: /etc/systemd/system/myapp.service
        mode: '0644'
    
    - name: Enable and start service
      systemd:
        name: myapp
        daemon_reload: yes
        enabled: yes
        state: restarted
    
    - name: Configure firewall
      firewalld:
        port: 8080/tcp
        permanent: yes
        state: enabled
    
    - name: Wait for service to be ready
      wait_for:
        port: 8080
        delay: 5
        timeout: 60
    
    - name: Health check
      uri:
        url: "http://{{ inventory_hostname }}:8080/actuator/health"
        method: GET
        status_code: 200
      register: health_check
      failed_when: health_check.status != 200
    
    - name: Print health check result
      debug:
        msg: "Service is healthy: {{ health_check.json }}"
```

### Ansible Variables:
```yaml
# group_vars/all.yml
ansible_user: ec2-user
ansible_ssh_private_key_file: /path/to/key.pem

# group_vars/webservers.yml
java_version: 17
app_port: 8080

# host_vars/web1.example.com.yml
server_name: web1
environment: staging
```

### Roles (Organized Playbooks):
```
roles/
├── common/
│   ├── tasks/
│   │   └── main.yml
│   ├── handlers/
│   │   └── main.yml
│   ├── templates/
│   ├── defaults/
│   │   └── main.yml
│   └── vars/
│       └── main.yml
├── java/
└── application/
```

### Running Playbooks:
```bash
# Run playbook
ansible-playbook deploy.yml

# Run with specific inventory
ansible-playbook -i production deploy.yml

# Run specific tags
ansible-playbook deploy.yml --tags "deploy,restart"

# Run in check mode (dry-run)
ansible-playbook deploy.yml --check

# Limit to specific hosts
ansible-playbook deploy.yml --limit "web1"
```

---

## Q4: Multiple Environment Deployments

### Environment-Specific Configuration:
```groovy
def deployTo(environment) {
    def config = [
        'dev':     [url: 'http://dev-k8s', namespace: 'dev'],
        'staging': [url: 'http://staging-k8s', namespace: 'staging'],
        'prod':    [url: 'http://prod-k8s', namespace: 'production']
    ]
    
    def env_config = config[environment]
    
    sh '''
        kubectl config set-cluster ${environment} --server=${env_config.url}
        kubectl set image deployment/my-app \\
            my-app=registry/my-app:${BUILD_NUMBER} \\
            -n ${env_config.namespace}
    '''
}
```

---

## Q5: Best Practices

✅ **Pipeline Design:**
- Fail fast (run tests before build)
- Parallel stages when possible
- Clear success/failure notifications
- Automated rollback on deployment failure

✅ **Security:**
- Use credentials plugin for secrets
- Don't log sensitive data
- Restrict deployment permissions
- Enable audit logging

✅ **Performance:**
- Cache dependencies
- Use build artifacts
- Minimize Docker layer size
- Parallel testing

✅ **Monitoring:**
- Log all deployments
- Set up alerts
- Track deployment frequency
- Monitor error rates

---

**Last Updated:** May 8, 2026


