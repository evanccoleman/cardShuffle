#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# importing modules
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#rows
#1  w w b b w   w w b b w   w
#2  w b r r b   w b r r b   w
#3  b r r r r   b r r r r   b
#4  b r r r r   r r r r r   b
#5  w b r r r   r r r r b   w
#6  w w b r r   r r r b w   w
#7  w w w b r   r r b w w   w
#8  w w w w b   r b w w w   w
#9  w w w w w   b w w w w   w

# creating/saving the first row - w w b b w   w w b b w   w
row1 = ['images/white1.png', 'images/white2.png', 'images/black1.png', 'images/black2.png', 'images/white3.png',
        'images/white4.png', 'images/white5.png', 'images/black3.png', 'images/black4.png', 'images/white6.png',
        'images/white7.png']
imgs    = [ Image.open(i) for i in row1 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row1.png' )    

# creating/saving the second row - w b r r b   w b r r b   w
row2 = ['images/white8.png', 'images/black5.png', 'images/red1.png', 'images/red2.png', 'images/black6.png',
        'images/white9.png', 'images/black7.png', 'images/red3.png', 'images/red4.png', 'images/black8.png',
        'images/white10.png']
imgs    = [ Image.open(i) for i in row2 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row2.png' )  

# creating/saving the third row - b r r r r   b r r r r   b
row3 = ['images/black9.png', 'images/red5.png', 'images/red6.png', 'images/red7.png', 'images/red8.png',
        'images/black10.png', 'images/red9.png', 'images/red10.png', 'images/red11.png', 'images/red12.png',
        'images/black11.png']
imgs    = [ Image.open(i) for i in row3 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row3.png' )  

# creating/saving the fourth row - b r r r r   r r r r r   b
row4 = ['images/black12.png', 'images/red13.png', 'images/red14.png', 'images/red15.png', 'images/red16.png',
        'images/red17.png', 'images/red18.png', 'images/red19.png', 'images/red20.png', 'images/red21.png',
        'images/black13.png']
imgs    = [ Image.open(i) for i in row4 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row4.png' )  

# creating/saving the fifth row - w b r r r   r r r r b   w
row5 = ['images/white11.png', 'images/black14.png', 'images/red22.png', 'images/red23.png', 'images/red24.png',
        'images/red25.png', 'images/red26.png', 'images/red27.png', 'images/red28.png', 'images/black15.png',
        'images/white12.png']
imgs    = [ Image.open(i) for i in row5 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row5.png' )  

# creating/saving the sixth row - w w b r r   r r r b w   w
row6 = ['images/white13.png', 'images/white14.png', 'images/black16.png', 'images/red29.png', 'images/red30.png',
        'images/red31.png', 'images/red32.png', 'images/red33.png', 'images/black17.png', 'images/white15.png',
        'images/white16.png']
imgs    = [ Image.open(i) for i in row6 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row6.png' )  

# creating/saving the seventh row - w w w b r   r r b w w   w
row7 = ['images/white17.png', 'images/white18.png', 'images/white19.png', 'images/black18.png', 'images/red34.png',
        'images/red35.png', 'images/red36.png', 'images/black19.png', 'images/white20.png', 'images/white21.png',
        'images/white22.png']
imgs    = [ Image.open(i) for i in row7 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row7.png' )  
   
# creating/saving the eigth row - w w w w b   r b w w w   w
row8 = ['images/white23.png', 'images/white24.png', 'images/white25.png', 'images/white26.png', 'images/black20.png',
        'images/red37.png', 'images/black21.png', 'images/white27.png', 'images/white28.png', 'images/white29.png',
        'images/white30.png']
imgs    = [ Image.open(i) for i in row8 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row8.png' )  

# creating/saving the ninth row - w w w w w   b w w w w   w
row9 = ['images/white31.png', 'images/white32.png', 'images/white33.png', 'images/white34.png', 'images/white35.png',
        'images/black22.png', 'images/white36.png', 'images/white37.png', 'images/white38.png', 'images/white39.png',
        'images/white40.png']
imgs    = [ Image.open(i) for i in row9 ]
imgs_comb = np.hstack([i for i in imgs])
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save( 'outputImages/row9.png' )  

# combining the rows
rowList = ['outputImages/row1.png', 'outputImages/row2.png', 'outputImages/row3.png', 'outputImages/row4.png',
           'outputImages/row5.png', 'outputImages/row6.png', 'outputImages/row7.png', 'outputImages/row8.png',
           'outputImages/row9.png']
imgs = [Image.open(i) for i in rowList]
imgs_comb = np.vstack([i for i in imgs])
imgs_comb = Image.fromarray( imgs_comb)
imgs_comb.save( 'outputImages/test2.png' )
