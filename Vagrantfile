Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.provision "shell", inline: <<-SHELL
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
    sed -i 's/PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config
    systemctl restart sshd
    echo -e "strongpassword\nstrongpassword" | (passwd vagrant)
    echo -e "strongpassword\nstrongpassword" | (passwd root)
  SHELL

 
# region one controller node
# eno1 is public nic of physical server, eno2 is internal mgmt nic and connect to baremetal ipmi
  config.vm.define "controller-01" do |t|
    t.vm.provision "shell", inline: <<-SHELL
      sleep 5 && ip r del 0.0.0.0/0 via 10.0.2.2
      ip r add 0.0.0.0/0 via 78.41.207.1
  SHELL
    t.vm.hostname = "controller-01"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "public_network", ip: "192.168.56.10", bridge: "eno2"
    t.vm.network "public_network", bridge: "eno1", auto_config: false
    t.vm.network "public_network", ip: "78.41.207.231", bridge: "eno1"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "controller-01"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end
 
# region one compute nodes 
  config.vm.define "compute-01" do |t|
    t.vm.hostname = "compute-01"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "public_network", ip: "192.168.56.11", bridge: "eno2"
    t.vm.network "public_network", bridge: "eno1", auto_config: false
    t.vm.provider "virtualbox" do |vb|
      vb.name = "compute-01"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end

  config.vm.define "compute-02" do |t|
    t.vm.hostname = "compute-02"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "public_network", ip: "192.168.56.12", bridge: "eno2"
    t.vm.network "public_network", bridge: "eno1", auto_config: false
    t.vm.provider "virtualbox" do |vb|
      vb.name = "compute-02"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end

# region two controller node
  config.vm.define "controller-02" do |t|
    t.vm.provision "shell", inline: <<-SHELL
      sleep 5 && ip r del 0.0.0.0/0 via 10.0.2.2
      ip r add 0.0.0.0/0 via 78.41.207.1
  SHELL
    t.vm.hostname = "controller-02"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    #openstack service mgmt network nic,enp0s8
    t.vm.network "public_network", ip: "192.168.56.20", bridge: "eno2"
    # used for provider network nic,enp0s9
    t.vm.network "public_network", bridge: "eno1", ip: "0.0.0.0", netmask: "255.255.255.255"
    # used for provider network nic,enp0s10
    t.vm.network "public_network", bridge: "eno1", ip: "0.0.0.0", netmask: "255.255.255.255"
    # used for controller public service api endpoint, enp0s16
    t.vm.network "public_network", ip: "78.41.207.232", bridge: "eno1"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "controller-02"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc4", "allow-all"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end

  config.vm.define "compute-03" do |t|
    t.vm.hostname = "compute-03"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "public_network", ip: "192.168.56.21", bridge: "eno2"
    # used for provider network nic,enp0s9
    t.vm.network "public_network", bridge: "eno1", ip: "0.0.0.0", netmask: "255.255.255.255"
    # used for provider network nic,enp0s10
    t.vm.network "public_network", bridge: "eno1", ip: "0.0.0.0", netmask: "255.255.255.255"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "compute-03"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc4", "allow-all"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end
  config.vm.define "compute-04" do |t|
    t.vm.hostname = "compute-04"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "public_network", ip: "192.168.56.22", bridge: "eno2"
    # used for provider network nic,enp0s9
    t.vm.network "public_network", bridge: "eno1", ip: "0.0.0.0", netmask: "255.255.255.255"
    # used for provider network nic,enp0s10
    t.vm.network "public_network", bridge: "eno1", ip: "0.0.0.0", netmask: "255.255.255.255"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "compute-04"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
      vb.customize ["modifyvm", :id, "--nicpromisc4", "allow-all"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end
end
