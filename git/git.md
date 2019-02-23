`作区 --add--> 缓存区 --commit-->  * 本地库区1 --push--> 远程库区`    
git是分布式版本控制系统，我们只要有一个原始的git版本仓库，就可以让其他主机克隆这个原始版本仓库，从而使一个git版本仓库可以被同时分布到不同的主机之上，并且每台主机的版本库都是一样的，没有主次之分，极大的保证了数据安全性。并使得用户能够自主选择向哪个git服务器推送文件。
linxu安装git
#安装git
yum install git -y
#配置全局用户以及邮箱
git config --global user.name "zyx"
git config --global user.email "im@zyx.com"
git config --global color.ui true
#检查git相关配置
git config --list
user.name=liuliya
user.email=im@liuliya.com
color.ui=true
git版本升级
查看git版本：
git --version
git 1.7.1
#卸载git版本
yum remove git
#安装依赖包
查看安装依赖包
rpm -qa curl-devel expat-devel gettext-devel openssl-devel zlib-devel asciidoc gcc perl-ExtUtils-MakeMaker xmlto
#yum安装
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel asciidoc gcc perl-ExtUtils-MakeMaker xmlto
确认：libiconv安装
　　安装libiconv过程：
wget http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.14.tar.gz
tar xf libiconv-1.14.tar.gz
cd libiconv-1.14
./configure --prefix=/usr/local/libiconv
make && make install
下载git2.2.1并将git添加到环境变量中
wget https://github.com/git/git/archive/v2.2.1.tar.gz
tar xf v2.2.1.tar.gz
cd git-2.2.1
make configure
./configure --prefix=/usr/local/git --with-iconv=/usr/local/libiconv
make all doc
make install install-doc install-html
echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/bashrc
source /etc/bashrc
报错：
/bin/sh: line 1: xmlto: command not found
make[1]: *** [git-add.1] Error 127
make[1]: Leaving directory `/server/software/git-2.1.2/Documentation'
make: *** [doc] Error 2
[root@node1 git-2.1.2]# 
解决：
yum install xmlto
#查看git版本号
git --version
git version 2.2.1
