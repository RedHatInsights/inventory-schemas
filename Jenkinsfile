#!/usr/bin/env groovy

/*
 * Not using https://github.com/marketplace/actions/spectral-linting
 * because of https://github.com/stoplightio/spectral-action/issues/200.
 */

node('nodejs') {

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
