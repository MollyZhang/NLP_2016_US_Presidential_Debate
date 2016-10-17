# NLP_2016_US_Presidential_Debate
Natural Language Learning and processing of 2016 Presidential Debate Transcripts  
Data download from kaggle: https://www.kaggle.com/mrisdal/2016-us-presidential-debates


### Note on debugging keras and tensorflow:
1. !Do not do "pip install tensorflow", do this instead:  
`sudo easy_install --upgrade six`  
`export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc0-py2-none-any.whl`
`sudo pip install --upgrade $TF_BINARY_URL`

2. tensorflow will try to import the numpy verison that came with Mac, which has API incompatiblility with tf. The correct way to is to use virtualenv and install all needed libraries there

3. `model.add(Dropout(0.2))` complains of import error in `tensorflow_backend.py`, need to edit the import statment at three places in code to this: `from tensorflow.python.ops import control_flow_ops` and `x = control_flow_ops.cond.....`   (Fucking hell...)


### Note on setting up project in hyades ([super computing cluster at UCSC](https://pleiades.ucsc.edu/hyades/Hyades_QuickStart_Guide))
1. `git clone https://github.com/MollyZhang/NLP_2016_US_Presidential_Debate`
2. Install python and pip 2.7 locally (instruction [here](http://thelazylog.com/install-python-as-local-user-on-linux/)), except for one difference:  
 add `$HOME/python/bin/` to $PATH, instead of `$HOME/python/Python-2.7.11/`
3. Setup virtualenv and activate virtualenv:  
 `pip install virtualenv`  
 `virtualenv tf-env`  
 `source tf-env/bin/activate`
4. Install tensorflow (GPU version) along with the correct GNU C library and cuda library following [this instruction](https://github.com/MollyZhang/AlphaGoPolicyNet/blob/master/install_tensorflow_on_hyades.txt)
 create alias "tfpython" in place of the last step in the instruction for speedy python login
5. Ssh into gpu server (gpu-1 to gup-8) and test tensorflow GPU installation following [this link](https://www.tensorflow.org/versions/r0.11/how_tos/using_gpu/index.html) 

 #### Side note on locally install Screen on the GPU server:  
 `mkdir ~/screen/`  
 `cd ~/screen`  
 `wget ftp://ftp.gnu.org/gnu/screen/screen-4.4.0.tar.gz`  
 `tar xzf screen-*.tar.gz`  
 `cd screen-*/`  
 `./configure --prefix=/home/mollyzhang/.local`
 `make && make install`







### Crudely comparing Speed with and without GPU
single hidden LSTM layer with 256 memory units
CPU (laptop): 600s per epoch
GPU (hyades): 300s per epoch
