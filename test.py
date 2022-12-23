#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:11:32 2022

@author: evan
"""

# Python program to shuffle a deck of card

# importing modules
import itertools, random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# make an array for the 52 shuffled decks
arrayNp = np.empty([52,52])

# make a deck of cards
# deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# deckNum = list(itertools.product(range(1,53)))
deckNp = np.arange(52)

# shuffle the cards
# random.shuffle(deck)
# random.shuffle(deckNum)
for i in range(52):
    np.random.shuffle(deckNp)
    arrayNp[i,:] = deckNp

# draw ten cards
# print("You got:")
# for i in range(10):
#    print(deck[i][0], "of", deck[i][1])
#    print(deckNum[i][0])
#    print(deckNp[i])
   
#  first color is black-er (0.0 would be black), last is "true" red
colors = [(0.5, 0, 0), (1, 0, 0)] 
cm = LinearSegmentedColormap.from_list("Custom", colors, N=50)
mat = np.indices((52,52))[1]
#plt.imshow(mat, cmap=cm)
plt.imshow(arrayNp, cmap=cm)
plt.show()


# test comment