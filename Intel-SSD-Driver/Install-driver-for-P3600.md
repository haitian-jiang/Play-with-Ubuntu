# Install driver for P3600

I use an Intel SSD for my linux system. It is a 800G P3600 drive running by PCI-e and NVMe.

Ubuntu can drive this NVMe disk out of the box, but in the daily use I found that Ubuntu cannot tap this drive to the full. When I copy a file from another NVMe SSD to this SSD, the speed is only about several hundred MB/s. Considering I installed a driver from Intel when I installed Windows in this SSD, I guess a dedicated driver may also be needed in linux. So I started to look up.

After a simple look-up, I found the driver from the [official website](https://downloadcenter.intel.com/zh-cn/download/29337/-CLI-?product=80999) that support my SSD(P3600) and my system(Ubuntu 18.04), so I installed it.

[!driver-download](driver-download.png)