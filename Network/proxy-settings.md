# Proxy Setting

Assuming that you have already set up shadowsocks or v2ray, etc., and your http proxy runs on port 1080, sock proxy runs on port 1088



### terminal

For short term change(in the current terminal), run the following commands.

```bash
export http_proxy=127.0.0.1:1080
export https_proxy=127.0.0.1:1080
```

For long term change, add these commands into ``~/.bashrc`` or ``~/.zshrc``



### git

[reference](https://segmentfault.com/q/1010000000118837) [reference](https://segmentfault.com/a/1190000018813121) [reference](https://gist.github.com/laispace/666dd7b27e9116faece6) [reference](https://gist.github.com/fearblackcat/850c6e027d5a03017c44daaa6a7ffc30) [reference](https://www.v2ex.com/t/332816)

step 1: configure http://

You can add these in ``~/.gitconfig``

```bash
[core]
	gitproxy = socks5://127.0.0.1:1088
[http]
	proxy = http://127.0.0.1:1080
[https]
	proxy = https://127.0.0.1:1080
```

Or you can run the following commands to reach the same effect

```bash
git config --global http.proxy 'http://127.0.0.1:1080'
git config --global https.proxy 'https://127.0.0.1:1080'
git config --global core.gitproxy 'socks5://127.0.0.1:1088'
```

Now you can accelerate ``git clone http://``



step 2: configure git://

Add the following into ``~/.ssh/config``

```bash
Host github.com
HostName github.com
User git
Port 22
ProxyCommand nc -x 127.0.0.1:1088 %h %p
```

<<<<<<< HEAD
Now you can accelerate ``git clone git://``
=======
run ``chmod 644 ~/.ssh/config``, otherwise ssh will return "Bad owner or permissions on /home/$USER/.ssh/config"
>>>>>>> 6b5366042542d51c3e3ec69e1c597e5b74ad2ab9
