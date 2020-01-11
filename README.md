# Ansible Linux based Heketi role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-heketi.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-heketi.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-heketi)
[![Galaxy Role Downloads](https://img.shields.io/ansible/role/d/45449.svg?style=flat)](https://galaxy.ansible.com/jetune/heketi)

Ansible role used to install Heketi on Linux based Operating System.

<a href="https://www.kube-cloud.com/"><img width="200" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="150" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>
<a href="https://www.gluster.org/"><img width="150" src="https://www.gluster.org/wp-content/uploads/2016/03/gluster-ant.png" /></a>
<a href="https://github.com/heketi/heketi"><img width="150" src="https://avatars3.githubusercontent.com/u/12890374?s=400&v=4" /></a>

# Supported Version

* Heketi 7+

# Supported OS

* CentOS 6/7
* RedHat 6/7
* Ubuntu Xenial/Bionic

# Usage

* Install Role ``` ansible-galaxy install jetune.heketi ```
* use in your playbook
```
---
- hosts: all

  roles:
   
   - role: jetune.heketi
     vars:
      heketi_install: true
      heketi_install_from_repo: false
      heketi_install_arch: "amd64"
      heketi_install_version: "9.0.0"
      heketi_install_dir: "/etc/sds/heketi"
      heketi_install_client_dir: "/etc/sds/heketi-client"
      heketi_install_command_link: "/usr/bin/heketi"
      heketi_configure: true
      heketi_config_dir: "/appli/hkt/param/conf"
      heketi_config_client_dir: "/appli/hkt/param/conf"
      heketi_config_filename: "heketi.json"
      heketi_config_client_filename: "heketi-client.json"
      heketi_node_executor: "ssh"
      heketi_service_unit_description: "SDS Provisioning Server [Heketi]"
      heketi_service_working_dir: "/appli/hkt/var/lib"
      heketi_service_user: "root"
      heketi_service_pid_file: "/var/run/heketi.pid"
      heketi_node_source_ssh_keyfile: "keys/heketi_rsa"
      heketi_node_ssh_keyfile: "/etc/ssh/heketi_rsa"
      heketi_node_ssh_user: "root"
      heketi_node_ssh_command_sudo: false
      heketi_node_xfs_sw: 10
      heketi_node_xfs_su: 10
      heketi_node_brick_max_size_gb: 1024
      heketi_node_brick_min_size_gb: 1
      heketi_node_max_bricks_per_volume: 33
      heketi_config_topology_nodes:
       - zone: 1
         manage_host_names:
          - "192.168.1.1"
         storage_host_names:
          - "172.16.1.1"
         devices:
          - name: "/dev/sdb"
            destroydata: false
       - zone: 2
         manage_host_names:
          - "192.168.1.2"
         storage_host_names:
          - "172.16.1.2"
         devices:
          - name: "/dev/sdb"
            destroydata: false
       - zone: 3
         manage_host_names:
          - "192.168.1.3"
         storage_host_names:
          - "172.16.1.3"
         devices:
          - name: "/dev/sdb"
            destroydata: false

```
