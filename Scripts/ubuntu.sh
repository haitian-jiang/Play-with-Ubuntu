# clear home
rm Anaconda3-2020.11-Linux-x86_64.sh
rm -r lishujingDesk
rm -r nccl
rm -r runcode

# utils
chmod 1777 /tmp  # for apt to work
apt update
apt install -y htop
apt install -y iputils-ping

# vim
echo "inoremap jk <Esc>" > ~/.vimrc

# git
echo "140.82.112.3 github.com" >> /etc/hosts
echo "185.199.108.153 assets-cdn.github.com" >> /etc/hosts
echo "199.232.69.194 github.global.ssl.fastly.net" >> /etc/hosts
# avoid gnutls_handshake() failed: The TLS connection was non-properly terminated.
git config --global  --unset https.https://github.com.proxy 
git config --global  --unset http.https://github.com.proxy 

# zsh
apt install -y zsh
chsh -s $(which zsh)
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone git://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="ys"/' ~/.zshrc
sed -i 's/plugins=(git)/plugins=(git zsh-syntax-highlighting zsh-autosuggestions)/' ~/.zshrc
cat >>~/.zshrc<<EOF
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="\$('/root/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ \$? -eq 0 ]; then
    eval "\$__conda_setup"
else
    if [ -f "/root/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/root/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/root/anaconda3/bin:\$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

bindkey ';' autosuggest-accept
alias p='python3'
export PATH="/usr/local/cuda/bin:.:$PATH"
EOF
source .zshrc


# jupyter
jupyter notebook --generate-config
sed -i "s/# c.NotebookApp.ip = '127.0.0.1'/c.NotebookApp.ip = '0.0.0.0'/" ~/.jupyter/jupyter_notebook_config.py
sed -i "s/# c.NotebookApp.open_browser = True/c.NotebookApp.open_browser = False/" ~/.jupyter/jupyter_notebook_config.py

# conda
conda create -n mytorch python=3.9 pytorch torchvision jupyter ipython jupyterlab networkx cudatoolkit=11.3 -c pytorch
conda install pyg -c pyg -c conda-forge
conda deactivate
python -m ipykernel install --name tf1 --display-name "tensorflow1.13"

