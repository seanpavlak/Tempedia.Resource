#!/usr/bin/env python
# coding: utf-8

# In[32]:


from PIL import Image, ImageDraw, ImageFont #dynamic import
import glob


# In[33]:


images = glob.glob('..//images//luma//*.gif')
# images = glob.glob('..//images//standard//*.gif')


# In[34]:


for image in images:
    gif = image.split(".gif")
    img = Image.open(image)
    img.save(gif[0]+".png",'png', optimize=True, quality=100)


# In[35]:


images


# In[ ]:




