#!/bin/bash

apt update

apt install -y \
  docker.io \
  docker-compose

systemctl enable docker
systemctl start docker

usermod -aG docker vagrant
