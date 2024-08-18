# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.ssh.insert_key = false

  # Obtener el valor del DNI y la dificultad de las variables de entorno.
  dni = ENV['DNI']
  dificultad = ENV['SELECCION']

  # Obtenemos el valor de las IPs de las variables de entorno.
  ip_vm1 = ENV['IP_VM1']
  ip_vm2 = ENV['IP_VM2']
  ip_vm3 = ENV['IP_VM3']
  ip_vm4 = ENV['IP_VM4']
  ip_vm5_1 = ENV['IP_VM5_1']
  ip_vm5_2 = ENV['IP_VM5_2']
  ip_vm6 = ENV['IP_VM6']
  ip_vm7 = ENV['IP_VM7']
  ip_vm8 = ENV['IP_VM8']
  ip_vm9_1 = ENV['IP_VM9_1']
  ip_vm9_2 = ENV['IP_VM9_2']
  ip_vm10 = ENV['IP_VM10']

  # Generamos un string con la dificultad asociada.
  if dificultad == '1' then
    dif = "difFacil"
  elsif dificultad == '2' then
    dif = "difMedia"
  elsif dificultad == '3' then
    dif = "difAvanzada"
  end

############################################################################################################################################################################################################################################

  # Machine1 - setup
  config.vm.define "vm1_#{dni}_#{dif}" do |vm1|
    # Virtualbox vm1 Vagrant-Box configuration
    vm1.vm.box = "vm1_#{dni}_#{dif}"
    # Hostname configuration
    vm1.vm.hostname = "vm1-KaliLinux-Atacante-#{dni}-#{dif}"
    # Virtualbox vm1 machine configuration 
    vm1.vm.provider "virtualbox" do |vb_vm1|
      vb_vm1.gui = true
      vb_vm1.memory = 4096
      vb_vm1.cpus = 4
      vb_vm1.customize ["modifyvm", :id,"--name", "vm1-KaliLinux-Atacante_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm1.vm.box_check_update = false
    # Configuración de SSH
    vm1.ssh.insert_key = false
    vm1.ssh.verify_host_key = false
    # Network configuration
    vm1.vm.network "private_network", ip: ip_vm1, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRUEBAS"
    # Port configuration
    vm1.vm.network "forwarded_port", guest: 22, host: 2220 #SSH
    # Shared Folders
    vm1.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine2 - setup
  config.vm.define "vm2_#{dni}_#{dif}" do |vm2|
    # Virtualbox vm2 Vagrant-Box configuration
    vm2.vm.box = "vm2_#{dni}_#{dif}"
    # Hostname configuration
    vm2.vm.hostname = "vm2-WebServer-#{dni}-#{dif}"
    # Virtualbox vm2 machine configuration 
    vm2.vm.provider "virtualbox" do |vb_vm2|
      vb_vm2.gui = false
      vb_vm2.memory = 1024
      vb_vm2.cpus = 1
      vb_vm2.customize ["modifyvm", :id,"--name", "vm2-WebServer_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm2.vm.box_check_update = false
    # Configuración de SSH
    vm2.ssh.insert_key = false
    vm2.ssh.verify_host_key = false
    # Network configuration
    vm2.vm.network "private_network", ip: ip_vm2, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRUEBAS"
    # Port configuration
    vm2.vm.network "forwarded_port", guest: 22, host: 2221 #SSH
    vm2.vm.network "forwarded_port", guest: 80, host: 8080 #HTTP
    # Shared Folders
    vm2.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine3 - setup
  config.vm.define "vm3_#{dni}_#{dif}" do |vm3|
    # Virtualbox vm3 Vagrant-Box configuration
    vm3.vm.box = "vm3_#{dni}_#{dif}"
    # Hostname configuration
    vm3.vm.hostname = "vm3-WebServer-#{dni}-#{dif}"
    # Virtualbox vm3 machine configuration 
    vm3.vm.provider "virtualbox" do |vb_vm3|
      vb_vm3.gui = false
      vb_vm3.memory = 1024
      vb_vm3.cpus = 1
      vb_vm3.customize ["modifyvm", :id,"--name", "vm3-WebServer_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm3.vm.box_check_update = false
    # Configuración de SSH
    vm3.ssh.insert_key = false
    vm3.ssh.verify_host_key = false
    # Network configuration
    vm3.vm.network "private_network", ip: ip_vm3, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRUEBAS"
    # Port configuration
    vm3.vm.network "forwarded_port", guest: 22, host: 2248 #SSH
    vm3.vm.network "forwarded_port", guest: 80, host: 8081 #HTTP
    # Shared Folders
    vm3.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine4 - setup
  config.vm.define "vm4_#{dni}_#{dif}" do |vm4|
    # Virtualbox vm4 Vagrant-Box configuration
    vm4.vm.box = "vm4_#{dni}_#{dif}"
    # Hostname configuration
    vm4.vm.hostname = "vm4-Client1-#{dni}-#{dif}"
    # Virtualbox vm4 machine configuration 
    vm4.vm.provider "virtualbox" do |vb_vm4|
      vb_vm4.gui = false
      vb_vm4.memory = 1024
      vb_vm4.cpus = 1
      vb_vm4.customize ["modifyvm", :id,"--name", "vm4-Client1_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm4.vm.box_check_update = false
    # Configuración de SSH
    vm4.ssh.insert_key = false
    vm4.ssh.verify_host_key = false
    # Network configuration
    vm4.vm.network "private_network", ip: ip_vm4, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRUEBAS"
    # Port configuration
    vm4.vm.network "forwarded_port", guest: 22, host: 2224 #SSH
    # Shared Folders
    vm4.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine5 - setup
  config.vm.define "vm5_#{dni}_#{dif}" do |vm5|
    # Virtualbox vm5 Vagrant-Box configuration
    vm5.vm.box = "vm5_#{dni}_#{dif}"
    # Hostname configuration
    vm5.vm.hostname = "vm5-Client2-#{dni}-#{dif}"
    # Virtualbox vm5 machine configuration 
    vm5.vm.provider "virtualbox" do |vb_vm5|
      vb_vm5.gui = false
      vb_vm5.memory = 1024
      vb_vm5.cpus = 1
      vb_vm5.customize ["modifyvm", :id,"--name", "vm5-Client2_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm5.vm.box_check_update = false
    # Configuración de SSH
    vm5.ssh.insert_key = false
    vm5.ssh.verify_host_key = false
    # Network configuration
    vm5.vm.network "private_network", ip: ip_vm5_1, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRUEBAS"
    vm5.vm.network "private_network", ip: ip_vm5_2, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRE_PRODUCCION"
    # Port configuration
    vm5.vm.network "forwarded_port", guest: 22, host: 2223 #SSH
    # Shared Folders
    vm5.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine6 - setup
  config.vm.define "vm6_#{dni}_#{dif}" do |vm6|
    # Virtualbox vm6 Vagrant-Box configuration
    vm6.vm.box = "vm6_#{dni}_#{dif}"
    # Hostname configuration
    vm6.vm.hostname = "vm6-FTPServer-#{dni}-#{dif}"
    # Virtualbox vm6 machine configuration 
    vm6.vm.provider "virtualbox" do |vb_vm6|
      vb_vm6.gui = false
      vb_vm6.memory = 1024
      vb_vm6.cpus = 1
      vb_vm6.customize ["modifyvm", :id,"--name", "vm6-FTPServer_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm6.vm.box_check_update = false
    # Configuración de SSH
    vm6.ssh.insert_key = false
    vm6.ssh.verify_host_key = false
    # Network configuration
    vm6.vm.network "private_network", ip: ip_vm6, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRE_PRODUCCION", gw: "192.168.56.97"
    # Port configuration
    vm6.vm.network "forwarded_port", guest: 21, host: 5678 #FTP
    vm6.vm.network "forwarded_port", guest: 22, host: 2225 #SSH
    vm6.vm.network "forwarded_port", guest: 80, host: 8083 #HTTP
    # Shared Folders
    vm6.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine7 - setup
  config.vm.define "vm7_#{dni}_#{dif}" do |vm7|
    # Virtualbox vm7 Vagrant-Box configuration
    vm7.vm.box = "vm7_#{dni}_#{dif}"
    # Hostname configuration
    vm7.vm.hostname = "vm7-Client3-#{dni}-#{dif}"
    # Virtualbox vm7 machine configuration 
    vm7.vm.provider "virtualbox" do |vb_vm7|
      vb_vm7.gui = false
      vb_vm7.memory = 1024
      vb_vm7.cpus = 1
      vb_vm7.customize ["modifyvm", :id,"--name", "vm7-Client3-#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm7.vm.box_check_update = false
    # Configuración de SSH
    vm7.ssh.insert_key = false
    vm7.ssh.verify_host_key = false
    # Network configuration
    vm7.vm.network "private_network", ip: ip_vm7, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRE_PRODUCCION"
    # Port configuration
    vm7.vm.network "forwarded_port", guest: 22, host: 2228 #SSH
    # Shared Folders
    vm7.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine8 - setup
  config.vm.define "vm8_#{dni}_#{dif}" do |vm8|
    # Virtualbox vm8 Vagrant-Box configuration
    vm8.vm.box = "vm8_#{dni}_#{dif}"
    # Hostname configuration
    vm8.vm.hostname = "vm8-Client4-#{dni}-#{dif}"
    # Virtualbox vm8 machine configuration 
    vm8.vm.provider "virtualbox" do |vb_vm8|
      vb_vm8.gui = false
      vb_vm8.memory = 1024
      vb_vm8.cpus = 1
      vb_vm8.customize ["modifyvm", :id,"--name", "vm8-Client4_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm8.vm.box_check_update = false
    # Configuración de SSH
    vm8.ssh.insert_key = false
    vm8.ssh.verify_host_key = false
    # Network configuration
    vm8.vm.network "private_network", ip: ip_vm8, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRE_PRODUCCION"
    # Port configuration
    vm8.vm.network "forwarded_port", guest: 22, host: 2227 #SSH
    # Shared Folders
    vm8.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine9 - setup
  config.vm.define "vm9_#{dni}_#{dif}" do |vm9|
    # Virtualbox vm9 Vagrant-Box configuration
    vm9.vm.box = "vm9_#{dni}_#{dif}"
    # Hostname configuration
    vm9.vm.hostname = "vm9-WebServer-#{dni}-#{dif}"
    # Virtualbox vm9 machine configuration 
    vm9.vm.provider "virtualbox" do |vb_vm9|
      vb_vm9.gui = false
      vb_vm9.memory = 1024
      vb_vm9.cpus = 1
      vb_vm9.customize ["modifyvm", :id,"--name", "vm9-WebServer_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm9.vm.box_check_update = false
    # Configuración de SSH
    vm9.ssh.insert_key = false
    vm9.ssh.verify_host_key = false
    # Network configuration
    vm9.vm.network "private_network", ip: ip_vm9_1, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRE_PRODUCCION"
    vm9.vm.network "private_network", ip: ip_vm9_2, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRODUCCION"
    # Port configuration
    vm9.vm.network "forwarded_port", guest: 22, host: 2226 #SSH
    vm9.vm.network "forwarded_port", guest: 80, host: 8084 #HTTP
    # Shared Folders
    vm9.vm.synced_folder '.', '/vagrant', disabled: true
  end

############################################################################################################################################################################################################################################

  # Machine10 - setup
  config.vm.define "vm10_#{dni}_#{dif}" do |vm10|
    # Virtualbox vm10 Vagrant-Box configuration
    vm10.vm.box = "vm10_#{dni}_#{dif}"
    # Hostname configuration
    vm10.vm.hostname = "vm10-DNSServer-#{dni}-#{dif}"
    # Virtualbox vm10 machine configuration
    vm10.vm.provider "virtualbox" do |vb_vm10|
      vb_vm10.gui = false
      vb_vm10.memory = 1024
      vb_vm10.cpus = 1
      vb_vm10.customize ["modifyvm", :id,"--name", "vm10-DNSServer_#{dni}_#{dif}"]
    end
    # Desactivación de la verificación de actualización de la Vagrant-Box
    vm10.vm.box_check_update = false
    # Configuración de SSH
    vm10.ssh.insert_key = false
    vm10.ssh.verify_host_key = false
    # Network configuration
    vm10.vm.network "private_network", ip: ip_vm10, :netmask => "255.255.255.248", virtualbox__intnet: "RED_PRODUCCION"
    # Port configuration
    vm10.vm.network "forwarded_port", guest: 22, host: 2227 #SSH
    # Shared Folders
    vm10.vm.synced_folder '.', '/vagrant', disabled: true
  end

end