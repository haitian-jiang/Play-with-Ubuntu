# jupyter environments

### Checking supporting jupyter kernels

```bash
jupyter kernelspec list
```

### Add sage to jupyter kernel

```bash
sudo jupyter kernelspec install ./Applications/SageMath/local/share/jupyter/kernels/sagemath
```

### Add conda environment

```bash
conda activate tf1
conda install ipykernel
sudo python -m ipykernel install --name tf1 --display-name "tensorflow1.13"
```

### Add R environment

Use R-Studio or R-Gui rather than R-console to execute the following commands, Otherwise there will be errors like this.
```
--- 在此連線階段时请选用CRAN的鏡子 ---
错误: .onLoad failed in loadNamespace() for 'tcltk', details:
  call: dyn.load(file, DLLpath = DLLpath, ...)
  error: 无法载入共享目标对象‘/usr/lib/R/library/tcltk/libs/tcltk.so’：:
  libtk8.6.so: 无法打开共享对象文件: 没有那个文件或目录
```

Use `sudo rstudio-bin` to start R-Studio with root priority. In R-Studio, 

```R
options(repos = 'http://mirrors.ustc.edu.cn/CRAN/')  # change the mirror
getOption('repos')  # see whether the mirros has been changed
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec(user = FALSE)  # if you didn't use sudo to install packages, then user=TRUE, and the kernel would be installed in home directory
```


# Allow connection from other devices

```bash
jupyter notebook --generate-config
vim ~/.jupyter/jupyter_notebook_config.py
```

In `jupyter_notebook_config.py`, modify the following options
```python
c.ConnectionFileMixin.ip = '0.0.0.0'
c.NotebookApp.ip = '*'
```

[reference](https://blog.csdn.net/Master_Lin_007/article/details/108023362) [reference](https://blog.csdn.net/qcyfred/article/details/82767965)
