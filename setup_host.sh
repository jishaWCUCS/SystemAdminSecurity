#!/bin/bash

apt update
apt install -y nfs-common
mkdir -p /var/nfs/keys

while [ ! -f /var/nfs/keys/id_rsa ]; do
  mount 192.168.1.1:/var/nfs/keys /var/nfs/keys
  sleep 10
done

cp /var/nfs/keys/id_rsa* /users/Jisha/.ssh/
chown Jisha: /users/Jisha/.ssh/id_rsa*
runuser -u Jisha -- cat /users/Jisha/.ssh/id_rsa.pub >> /users/Jisha/.ssh/authorized_keys
