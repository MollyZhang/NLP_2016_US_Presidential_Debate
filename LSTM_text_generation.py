import numpy
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

#df = pd.read_csv("data/debate.csv", encoding = 'iso-8859-1')
#trump_text = ". ".join(df[df.Speaker=="Trump"]['Text']).encode("ascii", "replace").lower()
