# NLP_2016_US_Presidential_Debate
Natural Language Processing and Deep Learning of 2016 Presidential Debate Transcripts. In particular, automatically generate Trump or Hillary debate speech.  
Data download from [kaggle](https://www.kaggle.com/mrisdal/2016-us-presidential-debates), the data is essential text transcript of the first two presendential debates.  
Most of the code is adapted from [this tutorial](http://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/).   

## Some example result from best model so far (1.09 cross entropy loss):

#### Random seed 1:
" illary was going to bring back jobs to upstate new york and she failed. i've heard them where hillar "  
#### Generated Text 1:  
y clinton has been a disaster. . and she said she salks about some bompanies are jostrtation. and i will tell you that i'm going to have a stepoenng to me and otr country. i aglee it the gissing to the war. and i will tell you that i'm going to have a stepoenng to me and of the freatest problem the stopigms and so doe to brpendry with the internet, and i will tell you that i'm going to have a stepoena, they're going to be a bompany. and i will tell you that i'm going to have a stepoena, they're going to be a bompany. and i will tell you that i'm going to have a stepoena, they're going to be a bompany. and i will tell you that i'm going to have a stepoena, they're going to be a bompany. and i will tell you that i'm going to have a stepoena, they're going to be a bompany. and i will tell you that i'm going to have a stepoena, they're going to be a bompany. and i will tell you that i'm going to have a stepoena, they're going to be a bompany. and i will tell you that i'm going to have a st

#### Randome Seed 2: 
" ticians have done.. i'll tell you very -- well, just very simple to say. sidney blumenthal works for "  
#### Generated Text 2:
the country that she salks about to many of the people that are going to be a bompa tp be a president that was to be a desaster. she doesn't have the stamina. i mean, it was a disaster. and i don't think you thie in the world, i agree with you the interest rates and all of the people that are going to be a bompa tp be a president that was to be a desaster. she doesn't have the stamina. i mean, it was a disaster. and i don't think you thie in the world, i agree with you the interest rates and all of the people that are going to be a bompa tp be a president that was to be a desaster. she doesn't have the stamina. i mean, it was a disaster. and i don't think you thie in the world, i agree with you the interest rates and all of the people that are going to be a bompa tp be a president that was to be a desaster. she doesn't have the stamina. i mean, it was a disaster. and i don't think you thie in the world, i agree with you the interest rates and all of the people that are going to be a b


#### Molly's comment:  
It's exciting to see that the network learned to complete names like "hillar" with a letter "y" as well as her last name "clinton". In fact, the model learned to produce some actual English words and sentences with semi-correct grammar just from a few hours worth of debate text. The sentence structure is preserved even though many words don't exist. I am surprised to find that many words and phrases are preserved, such as "country", "dissaster", "I will tell you", "I'm going to have a", etc. However, the speech gets stuck in a loop for the latter part of the paragragh. 


### Crudely comparing Speed with and without GPU  
 Single hidden LSTM layer with 256 memory units:  
 CPU (laptop): 610s per epoch  
 GPU (hyades): 260s per epoch  

 Two hiddlen LSTM layers with 256 memory unites each:  
 CPU (laptop): 1700s per epoch  
 GPU (hyades): 1100s per epoch  

 total training time (GPU):  
 one-layer LSTM: 265s * 20 = 88 min, loss: 1.89  
 two-layer LSTM: 1100 * 50 = 15 hours, loss: 1.09  


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

