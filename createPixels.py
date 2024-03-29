#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# importing modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# make an array for the 52 shuffled decks
arrayNp = np.empty([52,52])

# make a deck of cards
# deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# deckNum = list(itertools.product(range(1,53)))
deckNp = np.arange(52)

# draw ten cards
# print("You got:")
# for i in range(10):
#    print(deck[i][0], "of", deck[i][1])
#    print(deckNum[i][0])
#    print(deckNp[i])
   
# Looping through and creating pixels
for index in range(1, 500):
    # shuffle the cards
    for i in range(52):
        np.random.shuffle(deckNp)
        arrayNp[i,:] = deckNp

    #colors = [(0.5, 0, 0), (1, 0, 0)] #red
    #colors = [(0, 0, 0), (0.1, 0.1, 0.1)] #black
    colors = [(0.9, 0.9, 0.9), (1, 1, 1)] #white
    cm = LinearSegmentedColormap.from_list("Custom", colors, N=50)
    mat = np.indices((52,52))[1]
    plt.imshow(arrayNp, cmap=cm)
    #plt.xticks([])
    #plt.yticks([])
    plt.axis("off")
    filename = "images/white" + str(index) + ".png"
    plt.savefig(filename, format="png", bbox_inches="tight", pad_inches=0, transparent=True)
    plt.close()
    #plt.show()
