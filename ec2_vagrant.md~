### Creación de los archivos Vagrantfile y Ansible

**Nota**: Usuario por el cual se conectará por ssh, por defecto es **ubuntu** en EC2.

 - Nuestro VangrantFile tendrá la siguiente estructura:


```
#-*- mode: ruby -*-
#vi: set ft=ruby :

Vagrant.require_plugin 'vagrant-aws'
Vagrant.require_plugin 'vagrant-omnibus'


Vagrant.configure('2') do |config|
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    config.vm.hostname = "Tiendas"

    config.vm.provider :aws do |aws, override|
        aws.access_key_id = ENV['ACCESS_KEY_ID']
        aws.secret_access_key = ENV['SECRET_ACCESS_KEY']
        override.ssh.private_key_path = ENV['PRIVATE_KEY_PATH']
        aws.keypair_name = "credenciales"
        aws.region = "us-west-2"
        aws.tags = {
          'Name' => 'Tiendas',
          'Team' => 'Tiendas',
          'Status' => 'active'
        }
        override.ssh.username = "ubuntu"

        aws.region_config "us-west-2" do |region|
          region.ami = 'ami-35143705'
          region.instance_type = 't2.micro'
          region.keypair_name = "credenciales"
          region.security_groups = "launch-wizard-3"
        end

        config.vm.provision "ansible" do |ansible|
          ansible.sudo = true
          ansible.playbook = "iv.yml"
          ansible.verbose = "v"
          ansible.host_key_checking = false
        end
    end
end


```
Por partes:

 - Los datos del archivo **.csv** :

```
aws.access_key_id

aws.secret_access_key

```

 - Localización de nuestro sistema operativo:

```
aws.ami

```

 - Regíon de nuestra instancia:

```
aws.region
```

 - El nombre de nuestro archivo **.pem**:

```
keypair_name

```

 - El **security_groups** que se encargará de atender nuestras peticiones:

```
security_groups

```

 - El tipo de nuestra instancia:

```
instance_type

```
 - El nombre del usuario de nuestra máquina:

```
override.ssh.username

```


Para posibles dudas consultar este [enlace](https://github.com/mitchellh/vagrant-aws).


 - Desplegamos la aplicación usando **ansible**, que instalará todos los paquetes necesarios, descargará nuestra aplicación de nuestro repositorio y la ejecuta.
El archivo **.yml**  que hemos usado es el siguiente:

```
- hosts: localhost
  sudo: yes
  remote_user: vagrant
  tasks:
  - name: Actualizar sistema
    apt: update_cache=yes upgrade=dist
  - name: Instalar python-setuptools
    apt: name=python-setuptools state=present
  - name: Instalar build-essential
    apt: name=build-essential state=present
  - name: Instalar pip
    apt: name=python-pip state=present
  - name: Instalar git
    apt: name=git state=present
  - name: Ins Pyp
    apt: pkg=python-pip state=present
  - name: Instalar python-dev
    apt: pkg=python-dev state=present
  - name: Instalar libpq-dev
    apt: pkg=libpq-dev state=present
  - name: Obtener aplicacion de git
    git: repo=https://github.com/javiexfiliana7/submodulo-javi.git  dest=submodulo-javi clone=yes force=yes
  - name: Permisos de ejecucion
    command: chmod -R +x submodulo-javi
  - name: Instalar requisitos
    command: sudo pip install -r submodulo-javi/requirements.txt
  - name: ejecutar
    command: nohup sudo python submodulo-javi/manage.py runserver 0.0.0.0:80

```

---
### Despliegue de la aplicación
---

Aprovechando la posibilidad que nos da **Vagrant** de pasar parámetros al archivo, usaremos **ENV['NOMBRE-PRIMITIVA']** para introducir los credenciales de **Amazon**. 
Estas variables se introducen cuando creemos o destruyamos la instancia.
Tienen la siguiente sintaxis:

**--provider**: indica el proveedor.

```
variable n=valor vagrant up/destroy --provider=aws
----------------------------------------------------
//Referencia en Vagrantfile

ENV['n']

```

- Podemos ver como la aplicación está desplegada y funciona correctamente:

![desplegada]()
