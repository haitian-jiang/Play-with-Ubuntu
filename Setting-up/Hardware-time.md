# Adjust hardware time for dual system

### Situation

If you install both Windows and Linux on your PC, chances are that you will find your time in Windows wrong. For me, in China, the time in Windows and the time in Ubuntu lags for 8 hours.

### Reason

There is a CMOS on your motherboard to count time when then system is shut. It can run even when your system is unplugged because it has a dedicated power supply, we call the time stored in the CMOS "hardware time".
Windows takes the hardware time as the time to show you, so it don't take time zone into consideration. While Linux will take the hardware time as UTC time, so the output time is UTC time plus your time zone. For me, the time zone of China is UTC+8. So if my time in Windows is right, then my time in Linux will be 8 hours ahead.

### Solution

Make Ubuntu work in the same way as Windows.

```bash
sudo apt-get install ntpdate
sudo ntpdate time.windows.com
sudo hwclock --localtime --systohc
```

