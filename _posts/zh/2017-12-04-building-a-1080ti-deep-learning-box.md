---
layout: post
title: "1080ti + tensorflow-gpu + ubuntu 14.04 + SSD/机械双硬盘安装历险记"
date: 2017-12-04 23:23:34
lang: zh
ref: building-a-1080ti-deep-learning-box
redirect_from:
  - "/2017/12/04/1080ti-tf-gpu-ubuntu14-04-SSD-机械双硬盘安装历险记.html"
---

为什么题目这么长？

因为真的有那么多事情要说。&#40;不知道SEO会不会有帮助，该版本是在某大侠武林秘籍之上改编而成，如有雷同，实属巧合&#41;

经过了说不清楚的一段时间的折腾，终于完成了新的GPU计算服务器&#40;以下简称fwq&#41;的安装，现记录如下，以备未来之需：

- **安装ubuntu 14.04:**
这一步就颇为折腾。有以下坑：

>(initramfs) unable to find a medium containing a live file system...
	
解决办法：在启动 bios 里面关闭 secure boot, 或者在选择启动位置的时候选择不带 UEFI 的那项。原因：不明，可能是SSD &#43; 机械硬盘双硬盘导致的

>选择安装ubuntu（Install Ubuntu) 之后黑屏

解决办法：在高亮 Install Ubuntu 之后，按&quot;e&quot;进入高级设置，找到 quite splash ---, 删掉最后的 ---， 替换成 nomodeset，然后按 F10 开始安装。原因：ubuntu自带显卡驱动和1080ti不兼容。

>开始安装以后选择安装到SSD，显示无法写入grub错误

解决办法：装到机械硬盘上... 原因：不明

在fwq 备份 /etc/apt/sources.list 到 /etc/apt/sources.list.bak

修改 /etc/apt/sources.list来加入国内源，并运行

sudo apt-get update

- **启动 ssh server**

sudo apt-get install openssh-server


- 服务器端启动ssh服务: 

/etc/init.d/ssh start. 

安装完成以后在客户端进行ssh 登陆，检查

- 安装linux注释头

sudo apt-get install linux-headers-$(uname -r)

- 解决显卡和驱动的冲突：

>Create a file at /etc/modprobe.d/blacklist-nouveau.conf, 
>加入以下内容：blacklist nouveau options modeset=0

并 regenerate the kernel initramfs:

sudo update-initramfs -u

- 安装linux source 

sudo apt-get install dpkg-dev
sudo apt-get source linux-image-$(uname -r)

- **安装驱动**

据说在14.04上安装cuda要把驱动选得正好。这里我们尝试安装384.90驱动成功，其他驱动没有每一个试过。首先下载正确驱动：

>NVIDIA-Linux-x86_64-384.90.run

查看自己显卡是不是Nvidia的：

lspci | grep -i vga

然后看列出来的名字里面有没有Nvidia。清除掉现有驱动：

sudo apt-get remove --purge nvidia-*

然后进入文本模式 &#40;ctrl &#43; alt &#43; f1&#41;。关闭图形界面：

sudo service lightdm stop

运行

sudo <driver's name.run>

最好选择备份x11。安装完成后运行

nvidia-smi

确认版本是否正确。

- 下载cuda_8.0:

>cuda_8.0.61_375.26_linux.run

然后安装cuda_8.0:

chmod +x [cuda_8.0 run file]
sudo [cuda_8.0 run file]

- 在/etc/profile里面配置相应路径：

export PATH=/usr/local/cuda-8.0/bin:/usr/local/cuda:${PATH}
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:/usr/local/cuda/lib64:$LD_LIBRARY_PATH

- 对example里面的1_Utillities里面的deviceQuery进行make，然后执行。如果一切顺利，最后一行的输出应该是**Pass**

- 安装cudnn。这里用到的文件是：

>cudnn-8.0-linux-x64-v6.0.tgz

对文件解压并放到相应文件夹：

tar -zxvf [cudnn file name.tgz]

sudo cp cuda/include/*.h /usr/local/cuda/include

sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64

cd /usr/local/cuda/lib64

chmod 777 /usr/local/cuda/lib64/libcudnn*


- **安装anaconda**

为了加速，我们使用了清华的anaconda镜像：

>https//mirrors.tuna.tsinghua.edu.cn/help/anaconda/

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda config --set show_channel_urls yes

为pip添加douban源, 创建 ~/.pip/pip.conf

在其中加入：

>[global]
>index-url = http://pypi.douban.com/simple/
>trusted-host = pypi.douban.com

然后就是创建虚拟环境，并在其中安装tensorflow-gpu by calling:

pip install tensorflow-gpu

步骤比较多，不过我们按照大致这套流程已经成功安装了3台机器了。话说，装完系统又发现手机不充电了，又是清理插口，又是各种测试，修了很久没弄好，仔细看才发现原来昨晚停电之后我的台式机一直没开机，所以USB口也根本没法供电。这样看来，我还蛮适合装电脑、修手机的中关村生活的...


----------------
原创文章如转载，请注明出处“本文首发于blog.infplus.top”
