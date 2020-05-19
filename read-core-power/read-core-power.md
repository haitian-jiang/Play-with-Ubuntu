# Read core power consumption

### GPU power consumption

I use a NVIDIA graphic card and I installed the driver from NVIDIA. After installing the NVIDIA driver, there will be a command called ``nvidia-smi`` installed.

The output of ``nvidia-smi`` is something like this.

![nvidia-smi](nvidia-smi.png)

The power consumption can be directly read. In order to get the pure number of power consumption, we can use ``grep`` to get it.

The pattern looks like some digits, a W, a slash with space around both side, and a 250W. So ``nvidia-smi | grep "[0-9]*W / 250W"``