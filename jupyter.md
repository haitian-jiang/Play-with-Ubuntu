# jupyter environments

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

### Checking supporting jupyter kernels

```bash
jupyter kernelspec list
```
