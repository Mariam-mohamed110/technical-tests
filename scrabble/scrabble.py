# generate bag - maybe use a dictionary?
import random
import readline
# quick search how to open a txt file

# magic number?
tileDistribution = {'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6, 'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2}
# dictionary, each letter with its dist.

def generateBag(letters):
# variable = empty array
    bagTiles = []
# nested loop going through the dictionary for tile distribution
    for letter in letters:
        for i in range(letters[letter]):
            bagTiles.append(letter)
    
    return bagTiles

# print(generateBag(tileDistribution))
# It works yay


def generatePoints():
# assign each letter to its points
# declare sum variable
# for loop going over the word
# if letter is ...: sum is ...

def openDictionary():
#  use with open to open file
    with open('dictionary.txt') as f:
        dictionaryTxt = readline(f)
    return dictionaryTxt

def shuffle():
# to shuffle the tile in bag
# use import random function


def playScrabble():
# where the random tiles will be held
# player gets 7 tiles which get removed from the bag
# a word is generated which is compared to the dictionary file

