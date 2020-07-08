# exFAT in Ubuntu

ExFAT is an abbreviation for extended FAT. It is a file system that is compatible with Windows, Linux, and MacOS. So it is widely used as file system for mobile hard drives.

Ubuntu does not support exFAT file system by defaults. It is said that the reason is about copyright. So if you mount a device in exFAT, Ubuntu cannot recognize it.

This can be solved by simply install the exFAT file system by the following command.

```bash
sudo apt install exfat-utils exfat-fuse
```
