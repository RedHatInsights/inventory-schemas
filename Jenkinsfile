#!/usr/bin/env groovy

/*
 * Not using https://github.com/marketplace/actions/spectral-linting
 * because of https://github.com/stoplightio/spectral-action/issues/200.
 */

podLabel = UUID.randomUUID().toString()

podTemplate(label: podLabel, slaveConnectTimeout: 120, cloud: 'openshift', containers: [
    containerTemplate(
        name: 'jnlp',
        image: 'registry.access.redhat.com/openshift3/jenkins-agent-nodejs-8-rhel7',
        args: '${computer.jnlpmac} ${computer.name}',
        resourceRequestCpu: '200m',
        resourceLimitCpu: '500m',
        resourceRequestMemory: '128Mi',
        // This does not really need to be 2Gi. However, for containers with memory limit < 2Gi our Jenkins
        // uses i386 JVM which in turn makes it impossible to resolve a nodejs installation (no longer supports i386)
        // https://github.com/jenkinsci/nodejs-plugin/blob/master/src/main/java/jenkins/plugins/nodejs/tools/pathresolvers/LatestInstallerPathResolver.java#L94
        resourceLimitMemory: '2Gi'
    )
]) {
    node(podLabel) {

        env.NODEJS_HOME = "${tool 'node-10'}"
        env.PATH="${env.NODEJS_HOME}/bin:${env.PATH}"

        checkout scm

        stage('Install Spectral') {
            sh 'npm i -g @stoplight/spectral'
        }

        stage('Lint') {
            sh 'spectral lint schemas/system_profile/v1.yaml'
        }
    }
}
