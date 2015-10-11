sudo apt-get install sysv-rc-conf
sudo sysv-rc-conu

# 温度监控 
sudo apt-get install lm-sensors

echo "export PS1='[\u@\h \W]$'" >> ~/.bashrc
source ~/.bashrc
cd ~/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb 
sudo apt-get install pdftk

# ab benchmark tools of apache
sudo apt-get install apache2-utils
sudo apt-get install siege
sudo add-apt-repository ppa:ubuntu-wine/ppa
sudo apt-get update& sudo apt-get install wine1.7
