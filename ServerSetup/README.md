# Setting Up the UWPC Backend

Welcome to the setup guide for the University of Windsor Programming Competition (UWPC) backend. This comprehensive guide is designed to assist you in establishing a robust backend to manage the competition effectively. The backend infrastructure includes routing, auto-grading, and website management for the event.

## Hardware Requirements

For a successful setup, you will need:

- A capable computer - the more cores, the better for handling multiple requests and operations.
  - For demonstration purposes, we're using a DL180 G6 server equipped with dual Xeon X5670 processors and 112GB of RAM. While this may seem excessive, it ensures smooth operation throughout the competition.
- Two Ethernet ports on the computer - one will be used temporarily during the initial setup, while the other will be dedicated to the competition network.
- A reliable Access Point - a model that supports VLANs is preferable for enhanced security and network management during the competition. VLANs will allow you to segregate the competition network from the staff network efficiently.
  - In this example, we're using the Unifi U6 Lite for its robust performance and VLAN capabilities.
- Ethernet Cables - ensure you have enough cables for all connections, with some spares just in case.

## Software Requirements

The following software solutions will be utilized:

- **[Proxmox](https://www.proxmox.com/en/)** - an open-source virtualization management platform, which will host our virtual machines (VMs) for the competition.
- **[pfSense](https://www.pfsense.org/)** - a free and open-source firewall and router that also features full-fledged security functions.
- **[DOMjudge](https://www.domjudge.org/)** - a system for hosting programming competitions, managing the submission of solutions, and the automatic judging of these solutions.
- **[DevDocs](https://devdocs.io/)** - a comprehensive documentation platform that provides a unified interface for multiple programming languages and libraries.

## Setting Up Proxmox

Proxmox will serve as the foundation of our backend, providing a virtual environment for pfSense and DOMjudge.

### Installation

1. Download the Proxmox VE ISO from the official [Proxmox website](https://www.proxmox.com/proxmox-ve).
2. Create a bootable USB drive with the Proxmox VE ISO. Tools like Rufus for Windows or dd for Linux can be used for this purpose.
3. Insert the bootable USB into the server and boot from it.
4. Follow the on-screen instructions to install Proxmox VE onto your server. You will need to allocate storage and configure network settings during the installation. Make sure to note down the IP address assigned to Proxmox for future access.
5. Once installed, remove the installation media and reboot the server.

### Initial Configuration

1. Access the Proxmox web interface using the IP address from the installation, followed by the port `8006` (e.g., `https://192.168.1.100:8006`). You will likely encounter a security warning due to the self-signed SSL certificate, this is normal and can be bypassed.
2. Log in using the credentials set during the installation process.
3. Create the necessary network bridges for your competition network. This will depend on your network setup, but you will likely need a bridge for the competition network and another for the staff network. If you're using VLANs, you may need to create a bridge for each VLAN.

## pfSense
### Creating Virtual Machines

1. Click on the "Create VM" button in the upper right corner of the Proxmox interface.
2. Assign a name to the VM, such as "pfSense" and select the ISO for [pfSense](https://www.pfsense.org/) as the boot medium.
3. Follow the wizard to allocate CPU cores, memory, and disk space to the VM. For pfSense, 1-2 cores and 2GB of RAM should suffice.
4. Complete the VM creation process and start the VMs.

### Setting Up 
1. Install pfSense from the VM console.
2. Configure network routing, firewall, and VLANs.
   1. WLAN will need to be setup for installing DOMjudge.
   2. LAN will need to be setup for the competition network. This could be a VLAN depending on the network setup.
   3. A separate VLAN for the staff network can be created as well.
   4. Ensure that the firewall rules are set up to allow traffic to and from the necessary networks. This way the competition network can not access the internet and the staff network can access the competition network.

An example of the network setup can be found [here](config-pfSense.home.arpa-20230714081839.xml)

## DOMjudge
### Creating Virtual Machines
Note: Use a VM for DOMjudge as it requires, and not a container, because it requires user permissions that are not available in a container.
1. Click on the "Create VM" button in the upper right corner of the Proxmox interface.
2. Assign a name to the VM, such as "DOMjudge" and select the ISO for such as [Ubuntu Server](https://ubuntu.com/download/server) as the boot medium.
3. DOMjudge requirements will vary based on expected usage.
4. Complete the VM creation process and start the VMs.

### Setting Up
1. Install Ubuntu Server from the VM console.
2. Install Docker and Docker Compose. That can be done by following the instructions [here](https://docs.docker.com/engine/install/ubuntu/) and [here](https://docs.docker.com/compose/install/).
3. There will be 3 services that need to be set up for DOMjudge. The judgehost, the web server, and the database.
    #### MariaDB (Database)
    `docker run -it -d --restart=always --name dom-mariadb -e MYSQL_ROOT_PASSWORD=CompSciSoc -e MYSQL_USER=user -e MYSQL_PASSWORD=css -e MYSQL_DATABASE=domjudge -p 13306:3306 mariadb --max-connections=1000 --max-allowed-packet=268435456 --innodb_log_file_size=536870912`

    #### DOMjudge Web Server
    `docker run -d --restart=always --link dom-mariadb:mariadb -it -e MYSQL_HOST=mariadb -e MYSQL_USER=user -e MYSQL_DATABASE=domjudge -e MYSQL_PASSWORD=css -e MYSQL_ROOT_PASSWORD=CompSciSoc -p 12345:80 -e FPM_MAX_CHILDREN=40 -e WEBAPP_BASEURL=/ -e CONTAINER_TIMEZONE=America/Detroit --name domserver domjudge/domserver:latest`
    The initial passwords for the **admin** and **judgehost** users *should be printed when starting the domserver*, but if not, you can use the following commands to retrieve them:
    ```
    docker exec -it domserver cat /opt/domjudge/domserver/etc/initial_admin_password.secret 
    docker exec -it domserver cat /opt/domjudge/domserver/etc/restapi.secret
    ```
    You can view the webserver by going to [http://localhost:12345/](http://localhost:12345/)

    #### DOMjudge Judgehost
    `docker run -it -d --restart=always --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro --name judgehost-dom --link domserver:domserver --hostname judgedaemon-dom -e DAEMON_ID=0 -e JUDGEDAEMON_PASSWORD=xptZ59T+Z9VYj0EqGf5aHlRPHnoe4tMl -e CONTAINER_TIMEZONE=America/Detroit domjudge/judgehost:latest`
    **THIS WILL CHANGE ON EACH SETUP**
    Make sure you change 
    `JUDGEDAEMON_PASSWORD=PASSWORD`
    to the password acquired in the Web Server setup.
    ```
    default http://localhost//api   judgehost       xptZ59T+Z9VYj0EqGf5aHlRPHnoe4tMl

    admin
    YFku36tSyJ0EmmZt
    ```

## DevDocs
### Setting Up
To set up DevDocs, make sure you have setup DOMjudge as we will be using the docker instance of DOMjudge to host DevDocs. The container can be found [here](https://hub.docker.com/r/devdocs/devdocs).
1. Run the following command to start the container:
    `docker run -d --restart=always --name devdocs -p 12346:80 devdocs/devdocs`
2. You can view the webserver by going to [http://localhost:12346/](http://localhost:12346/)

Keep in mind that this will download all the documentation for the languages and libraries that DevDocs supports. This can take a while and a lot of space. It is possible to only download the documentation for the languages and libraries that you will be using. Please refer to the [DevDocs Docker Documentation](https://hub.docker.com/r/devdocs/devdocs) for more information.

## Networking Configuration
1. Connect the server to the Access Point via Ethernet.
2. Configure VLANs if necessary.
3. Validate that competition machines can reach DOMjudge VM.

### Finalizing the Setup
1. Conduct a trial run to verify functionality.
2. Document all configurations for maintenance and troubleshooting.

By completing these steps, your UWPC backend setup will be optimized for DOMjudge, ensuring a smooth and efficient competition experience.

## Extra Resources
 - [Proxmox Documentation](https://pve.proxmox.com/pve-docs/pve-admin-guide.html)
 - [pfSense Documentation](https://docs.netgate.com/pfsense/en/latest/index.html)
 - [DOMjudge Documentation](https://www.domjudge.org/documentation)

If you would like to try a different judging web interface, you can try [DMOJ](https://github.com/DMOJ/online-judge) though its a bit more complex to set up.

For competition problems, you can use
 - [open.kattis.com](https://open.kattis.com/)
 - [dmoj.ca/problems](https://dmoj.ca/problems/)
 - [Ratndeepk/Competitive-Programming](https://github.com/Ratndeepk/Competitive-Programming/tree/master)
 - [csestack.org](https://www.csestack.org/competitive-coding-questions/)
 - [kunal-kushwaha/Competitive-Programming-Resources](https://github.com/kunal-kushwaha/Competitive-Programming-Resources)
 - [CSGames-Archive](https://github.com/orgs/CSGames-Archive/repositories?type=all)
 - [CSgames](https://github.com/csgames)