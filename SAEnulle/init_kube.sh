#!/bin/bash

sudo kubeadm reset --force

sudo swapoff -a

# Initialize Kubernetes master
sudo kubeadm init --apiserver-advertise-address=192.168.56.101 --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=Mem,FileExisting-socat

# Set up kubeconfig for vagrant user
mkdir -p /home/vagrant/.kube
sudo cp -i /etc/kubernetes/admin.conf /home/vagrant/.kube/config
sudo chown vagrant:vagrant /home/vagrant/.kube/config

# Install Calico network plugin
kubectl apply -f https://docs.projectcalico.org/v3.16/manifests/calico.yaml

# Generate join command
kubeadm token create --print-join-command > /vagrant/kubeadm_join.sh