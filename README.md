<p align="center">
  <img width="340" height="300" src="./images/Alarm_Clock.png">
</p>

# pyArmClock

- [pyArmClock](#AlarmClock)
  - [Features](#Features)
  - [Hosting](#Hosting)
  - [Installing/Running](#Installing)
  - [ToDo](#ToDo)
  - [Platform Availability](#Platform-Availability)
      
A quick and dirty python based alarm clock with a GUI and alarm saving functionality. Allows for choosing of song/audio that you wake up to and can speak the time before playing the audio. Works great on a raspberry pi as well as other linux based OS's with automated setup using ansible.

## Features
- Alarm Functionality
- Song Choice
- Setup Automation
- 10 Min Snooze (Custom Snooze Duration Coming Soon)
- Nice GUI (Custom Themes will be implemented in future)

## Hosting


## Installing/Running

#### There's two options for install - Manual and Automated with Ansible
I recommend the automated install

#### **Raspberry Pi Automated Install:**


Update!
```
sudo apt update
```
Install Ansible
```
sudo apt install ansible
```
Now, pull the Git repo
```
git clone https://github.com/madeofpendletonwool/pyArmClock.git
```
cd into the pulled folder
```
cd pyArmClock/
```
Lastly, run the playbook to set everything up
```
ansible-playbook setup.yaml
```
Reboot!
```
sudo reboot 0
```

#### **x86 Computer Install:**
The intention here is that you can install the alarm clock on anything, regardless of platform or architechture. I may add more options down the road as well for CPU architecture. The instructure are almost the same as with raspberry pi. Just a different playbook. 

Also note that while I tried to make this agnostic of distro, package names vary, and you may need to install some packages manaully/change the playbook. Some basic ansible knowledge might be helpful. 

First, Install ansible - I assume you can handle this based on your distro package management.

Now, pull the Git repo
```
git clone https://github.com/madeofpendletonwool/pyArmClock.git
```
cd into the pulled folder
```
cd pyArmClock/
```
Use your editor of choice to open vars.yml and edit the user to reflect yourself.
```
user_name: your_user_name
```
Lastly, run the playbook to set everything up
```
ansible-playbook x86setup.yaml
```
Reboot!
```
sudo reboot 0
```

#### **Manual Install:**

*Seriously I don't recommend this. It's kinda awful with all the commands needed*

*Instructions for this method a work in progress*

## ToDo

 - [x] Create Code that can set off Alarms using a time module
 - [x] Snooze funtionality
 - [ ] Custom Snooze Duration
 - [x] Deploy via ansible and fully setup using raspberry pi
 - [ ] Easy setup with package management
 - [ ] Allow for saving of alarms after reboot
 - [ ] Display a big clock on the screen at all times
 - [ ] Dockerize (Probably?)
 - [x] Create alarm clock gui
 - [ ] Custom GUI Themes
 - [ ] arm it. Need it to run on a raspberry pi
 - [ ] Voice function to tell actual time
 - [x] Sound function
 - [x] Allow you to choose music/sound to play
 - [x] import of music from a location of choice 

## Platform Availability

Raspberry Pi and x86 Systems 