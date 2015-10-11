wget http://bootstrap.pypa.io/get-pip.py
sudo python get-pip.pyp
sudo pip install virtualenv
sudo pip install virtualenvwrapper
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

#https://pypi.python.org/pypi/pycountry/
pip install pycountry



# jenkins - cli
wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
echo deb http://pkg.jenkins-ci.org/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
sudo apt-get update
sudo apt-get install jenkins
# jenkins 安装不了的插件，点击连接后下载插件，然后通过高级选项面板上传安装
# 安装 git client/ShiningPanda/Xvfb 三个插件

#sudo apt-get install git firefox python3 python-virtualenv xvfb
