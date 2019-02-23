我的本地git仓库在 ~/git    
把ssh的公钥复制到github中，如果主机改名字就需要重新复制公钥    
使用visual staudio code下载markdown插件进行markdown编辑。还有预览功能，可以进行markdown编辑。



首先确认自己的本地git配置：    
`zyx:git zyx$ git config --list
credential.helper=osxkeychain
user.name=zyx
user.email=411235298@qq.com
color.ui=true
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
remote.origin.url=git@github.com:zhouyaxiong/zyx-website.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master`
***
>Git会时刻的追踪目录内文件的改动     
git add readme.txt #git添加文件至暂存区    
git status #再次查看状态    
git commit -m “the first commit” #git cmmit提交暂存取文件至git版本仓库。-m后面的额注释必须添加    
git push -u  origin master#将本地版本仓库，推送到指定的远端仓库 git push也可以     
git push -u origin master#推送至github中访问，以后再本地修改之后就可以直接git push 
git clone git@github.com:zhouyaxiong/demo.git #将远程仓库克隆岛本地
git mv readme.txt test.txt #git如果要修改文件名称,则使用git mv命令
git rm 我的文件 #在本地仓储删除文件


