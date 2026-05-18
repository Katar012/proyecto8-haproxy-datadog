#!/bin/bash

apt update

apt install -y \
  openssh-server \
  nginx

systemctl enable ssh
systemctl restart ssh

systemctl enable nginx
systemctl restart nginx

mkdir -p /sftp/uploads

useradd -m sftpuser

echo "sftpuser:1234" | chpasswd

chown root:root /sftp
chmod 755 /sftp

chown sftpuser:sftpuser /sftp/uploads
