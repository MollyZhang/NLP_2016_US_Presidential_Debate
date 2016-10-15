# NLP_2016_US_Presidential_Debate
Natural Language Learning and processing of 2016 Presidential Debate Transcripts  
Data download from kaggle: https://www.kaggle.com/mrisdal/2016-us-presidential-debates


### Note on installation and use of keras and tensorflow:
1. !Do not do "pip install tensorflow", do this instead:  
`sudo easy_install --upgrade six`  
`export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc0-py2-none-any.whl`
`sudo pip install --upgrade $TF_BINARY_URL`

2. Another bad time: tensorflow will try to import the numpy verison that came with Mac, which has API incompatiblility with tf. The correct way to solve it is to use virtualenv and install all needed libraries there

3. crazy bug with keras:
when do `model.add(Dropout(0.2))`, this file complain of import error:

`/tf_env/lib/python2.7/site-packages/keras/backend/tensorflow_backend.py`,
need to go into the code and edit the import statment to this:  
`from tensorflow.python.ops import control_flow_ops
 x = control_flow_ops.cond.....`  
at three places where control_flow_ops is used. Fucking hell! 

