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

id -u sftpuser >/dev/null 2>&1 || useradd -m sftpuser

echo "sftpuser:1234" | chpasswd

chown root:root /sftp
chmod 755 /sftp

chown sftpuser:sftpuser /sftp/uploads

cat >> /etc/ssh/sshd_config <<EOF

Match User sftpuser
    ChrootDirectory /sftp
    ForceCommand internal-sftp
    PasswordAuthentication yes
    AllowTcpForwarding no
    X11Forwarding no

EOF

systemctl restart ssh
