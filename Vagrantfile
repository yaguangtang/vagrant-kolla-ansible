Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
 
# region one controller node
  config.vm.define "controller1" do |t|
    t.vm.hostname = "controller1"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "private_network", ip: "192.168.56.10"
    t.vm.network "private_network", ip: "192.168.57.10"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "controller1"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end
 
# region one compute nodes 
  config.vm.define "compute-01" do |t|
    t.vm.hostname = "compute-01"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "private_network", ip: "192.168.56.11"
    t.vm.network "private_network", ip: "192.168.57.11"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "compute-01"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end

  config.vm.define "compute-02" do |t|
    t.vm.hostname = "compute-02"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "private_network", ip: "192.168.56.12"
    t.vm.network "private_network", ip: "192.168.57.12"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "compute-02"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end

# region two controller node
  config.vm.define "controller2" do |t|
    t.vm.hostname = "controller2"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "private_network", ip: "192.168.56.20"
    t.vm.network "private_network", ip: "192.168.57.20"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "controller2"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end

  config.vm.define "compute-03" do |t|
    t.vm.hostname = "compute-03"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "private_network", ip: "192.168.56.12"
    t.vm.network "private_network", ip: "192.168.57.12"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "compute-03"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end
  config.vm.define "compute-04" do |t|
    t.vm.hostname = "compute-04"
    t.vm.disk :disk, size: "100GB", primary: true
    t.vm.disk :disk, size: "100GB", name: "ceph"
    t.vm.network "private_network", ip: "192.168.56.12"
    t.vm.network "private_network", ip: "192.168.57.12"
    t.vm.provider "virtualbox" do |vb|
      vb.name = "compute-04"
      vb.gui = false
      vb.customize ["modifyvm", :id, "--nested-hw-virt", "on"]
      vb.memory = "16384"
      vb.cpus = "8"
    end
  end
end
