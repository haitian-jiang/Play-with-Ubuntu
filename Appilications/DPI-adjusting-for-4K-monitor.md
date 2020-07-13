### NetEase Could Music

The icons of applications mostly are stored in ``/usr/share/applications``, we can change the ``.desktop`` files in this directory to customize the launch icons.

`` sudo vim /usr/share/applications/netease-cloud-music.desktop``

change ``Exec=netease-cloud-music %U`` into ``Exec=netease-cloud-music --force-device-scale-factor=2.0 %U`` the number is the scaling factor, I set it equals to 2.0 so the the size is doubled.