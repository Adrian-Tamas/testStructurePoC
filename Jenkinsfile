pipeline {
  agent any

  parameters {
    string(name: 'FOLDER', defaultValue: 'my-folder', description: 'Folder to build from')
    string(name: 'VERSION', defaultValue: '1.0.0', description: 'Library version')
  }

  environment {
    PYPI_REPO_URL = "<private pypi repo url>"
    PYPI_USERNAME = "<pypi username>"
    PYPI_PASSWORD = "<pypi password>"
  }

  stages {
//     stage('Checkout') {
//       steps {
//         checkout scm
//       }
//     }

    stage('Checkout') {
      steps {
        // Use the FOLDER parameter to set the path to the folder to build from
        // substitute url and credentials id for checkout
        checkout([$class: 'GitSCM', branches: [[name: 'dev']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'git@github.com:myuser/myrepo.git', credentialsId: 'my-ssh-key']], changelog: true, poll: true, scmName: 'origin', scriptPath: '', gitTool: 'Default', submoduleRecursion: 'none', reference: '', sparseCheckoutPaths: [[path: "${params.FOLDER}/"]]])
      }
    }

    stage('Install dependencies') {
      steps {
//         sh 'cd ${params.FOLDER}'
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Update version') {
      steps {
        // Use the VERSION parameter to update the version number in setup.py
        sh "sed -i 's/__version__=\"[0-9]*.[0-9]*.[0-9]*\"/__version__=\"$VERSION\"/g' version.py"
      }
    }

    stage('Build package') {
      steps {
        sh 'python setup.py sdist bdist_wheel'
      }
    }

    stage('Upload to PyPI') {
      steps {
        withCredentials([
          usernamePassword(credentialsId: 'pypi-credentials', usernameVariable: 'PYPI_USERNAME', passwordVariable: 'PYPI_PASSWORD')
        ]) {
          sh 'twine upload --repository-url $PYPI_REPO_URL dist/*'
        }
      }
    }
  }
}