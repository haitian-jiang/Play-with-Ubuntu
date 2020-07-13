# Manually set /swap partition

[reference](https://juejin.im/post/5c2da2a151882566dc118af5)

```bash
swapon -s  # check the current swap file
sudo dd if=/dev/zero of=/swap-file bs=1G count=50  # create a new swap file
sudo chmod 600 /swap-file  # set file permission
sudo mkswap /swap-file  # activate the swap file
# sudo swapoff /swap-file  # unmount the swap file
sudo swapon /swap-file  # mount the swap file, will be ineffective after rebooting
# now use free of top or swapon -s, two swap file can be seen

# set the swap partition perminantly
sudo vim /etc/fstab  # change the original swap into '/swap-file  none  swap  sw  0  0'
```

