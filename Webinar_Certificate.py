#!/usr/bin/env python
# coding: utf-8

# In[21]:


# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os


# In[25]:


df = pd.read_csv('EN_session.csv')
#Import your CSV files containing the names of participants#


# In[23]:


font = ImageFont.truetype('arial.ttf',40)
#Define font parameters(Type, Size etc..)


# In[24]:


for index,j in df.iterrows():
    img = Image.open('attestation_en.jpg')
    draw = ImageDraw.Draw(img)
    #####print(j.Name)####
    draw.text(xy=(420,180),text=f'{j.Name}',fill=(0,0,0),font=font)
    img.save('pictures/{}.jpg'.format(j.Name))
    
# create a folder to save the generated images. In our case "picture" was used as the defined folder
# Use Paint to find the XY coordinates where the names will be written


# 

# In[ ]:





# In[ ]:





# In[ ]:




