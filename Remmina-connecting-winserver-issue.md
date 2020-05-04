# Remmina-connecting-winserver-issue

Today when I use remmina to connect a remote server running Winserver 2016, I met a problem. 

After I have entered the ip address, username and password correctly and click OK, a message poped out.

It reads like this

![rdp-problem](remmina-rdp.png)

The problem can be solved by running ```remmina -n``` in terminal to open a new connection or click the icon on top bar and open a new connection.

See more about this problem at [here](https://unix.stackexchange.com/questions/440803/remmina-cant-remote-into-windows-server)
