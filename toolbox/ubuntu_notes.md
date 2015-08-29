# Ubuntu 14

## 小的配置

- 终端提示符显示调整

    vi .bashrc
    source .bashrc

在最后一行加入，你可以自己调整，\u显示用户名、\h显示主机名，\W当前文件夹，非全路径

    export PS1='[\u@\h \W]$'

## 服务管理

    sudo apt-get install sysv-rc-conf
    sudo sysv-rc-conu

## unzip

解决zip文件解压编码问题

	unzip -O CP936 xxx.zip (用GBK, GB18030也可以)

有趣的是unzip的manual中并无这个选项的说明, unzip --help对这个参数有一行简单的说明。

## Firefox extensions

- baidu search
- firebug
- firesizer(Install 'The Addon Bar' first)
- firepath
- flashgot
- hackbar
- live http headers
- modify headers
- nimbus screen capture

## wireshark
<http://jingyan.baidu.com/album/c74d60009d992f0f6a595de6.html>
sudo apt-get install wireshark
sudo groupadd wireshark
sudo chgrp wireshark /usr/bin/dumpcap
# 让wireshark用户组有root权限使用dumpcap
sudo chmod 4755 /usr/bin/dumpcap
# Adding user min to group wireshark
sudo gpasswd -a min wireshark
wireshark

## Ubuntu终端快捷键
Ctrl-a Move to the start of the line.
Ctrl-e Move to the end of the line.
Alt-] x Moves the cursor forward to the next occurrence of x.
Alt-Ctrl-] x Moves the cursor backwards to the previous occurrence of x.
Ctrl-u Delete from the cursor to the beginning of the line.
Ctrl-k Delete from the cursor to the end of the line.
Ctrl-w Delete from the cursor to the start of the word.
Ctrl-y Pastes text from the clipboard.
Ctrl-l Clear the screen leaving the current line at the top of the screen.
Ctrl-x Ctrl-u Undo the last changes. Ctrl-_
Alt-r Undo all changes to the line.
Alt-Ctrl-e Expand command line.
Ctrl-r Incremental reverse search of history.
Alt-p Non-incremental reverse search of history.
!! Execute last command in history
!abc Execute last command in history beginning with abc
!n Execute nth command in history
^abc^xyz Replace first occurrence of abc with xyz in last command and execute it
:wq
## softwares

## Google Chrome

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb


## haroopad

markdown 编辑器

## 软件

**录屏软件vokoscreen**

    sudo apt-get install vokoscreen

**视频编解码软件transmageddon**

    sudo apt-get install transmageddon

**pdftk**

    sudo apt-get install pdftk
    pdftk --help
