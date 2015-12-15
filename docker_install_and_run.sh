#!/bin/bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo docker pull javiexfiliana/submodulo-javi
sudo docker run -i -t javiexfiliana/submodulo-javi /bin/bash
