# Brave Installer linux
This is a installer for Brave Browser on linux. It can easily install Brave on any major linux distro with a very simple and colorful user interface . What are you waiting for clone the repo now .

## How to install ?
First you need to clone this repository. Type
```bash
git clone https://github.com/DevXurde/brave-installer-linux.git
```
Now inside the brave-installer-linux folder you will see install.py file and some .sh files. These are the two ways to install brave via this installer. 
- install.py
- .sh files

### Option 1 - install.py
To install via the install.py . Open up your terminal and type
```bash
cd brave-installer-linux
```
```bash
sudo python3 install.py
```
When you will run the install.py file then you'll see somthing like this
```bash
            MENU            
----------------------------
1.Arch Based Distributions
2.Debian 9+, Ubuntu 16.04+ and Mint 18+
3.Fedora 28+, CentOS/RHEL 8+
4.OpenSUSE 15+
5.Exit

Enter Your Distribution (Eg: 1) : 
```
Choose which you are Example I am on Arch so I typed 1 and pressed enter.
Then it will install brave browser on your machine


### Option 2 - .sh files
To install via .sh file type the following commads in your terminal
```bash
cd brave-installer-linux
```
For Arch based distro
```bash
chmod a+x brave-arch.sh
sudo ./brave-arch.sh
```

For Debian based distro
```bash
chmod a+x brave-debian.sh
sudo ./brave-debian.sh
```

For Fedora based distro
```bash
chmod a+x brave-fedora.sh
sudo ./brave-fedora.sh
```

For OpenSuse
```bash
chmod a+x brave-opensuse.sh
sudo ./brave-opensuse.sh
```
This will install Brave Browser on your machine.



 **I hope it worked out for you**


# Thank you for using
