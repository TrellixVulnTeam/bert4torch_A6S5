# import unittest
# from bert4keras.models import build_transformer_model
# # from bert_pytorch import BERT, BertConfig
# from transformers import BertModel, BertTokenizer, AutoTokenizer
from bert4keras import models
# from bert_pytorch import BertModel
# import pandas as pd
import os

import transformers
# tokenizer = BertTokenizer.from_pretrained('')


# bert = BertModel.from_pretrained('bert-base-chinese', **{'cache_dir': r'pretrained_model/bert-base-chinese'})

import tqdm
import time


l = range(100)


for x in tqdm.tqdm(enumerate(l), desc='10 epoch', total=len(l), position=0, leave=False):
    print(x)
    time.sleep(0.3)







