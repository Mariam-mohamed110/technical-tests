# generate bag - maybe use a dictionary?
import random
import readline
# quick search how to open a txt file

# magic number?
tileDistribution = {'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6, 'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2}
# dictionary, each letter with its dist.

def openDictionary():
    #  use with open to open file
    with open('dictionary.txt') as f:
        dictionaryTxt = readline(f)
    return dictionaryTxt

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

def generatePoints(letters):
# assign each letter to its points
# declare sum variable
    sum = 0
# for loop going over the word
# if letter is ...: sum is ...
    for i in str(letters):
            if type(i) == str:
                if i == 'D' or i == 'G':
                    sum += 2
                elif i == 'B' or i == 'C' or i == 'M' or i == 'P':
                    sum += 3
                elif i == 'F' or i == 'H' or i == 'V' or i == 'W' or i == 'Y':
                    sum += 4
                elif i == 'K':
                    sum += 5
                elif i == 'J' or i == 'X':
                    sum += 8
                elif i == 'Q' or i == 'Z':
                    sum += 10
                else:
                    sum += 1
    return sum

# print(generatePoints('D, A'))
# print(generatePoints('GUARDIAN')) 
# think about removing space and joining the word together

def tileDrawn(letter):
    return letter.pop(0)


def playScrabble():
# where the random tiles will be held
# player gets 7 tiles which get removed from the bag
# a word is generated which is compared to the dictionary file
    newBag = generateBag(tileDistribution)
    random.shuffle(newBag)
    assignedTiles = [tileDrawn(newBag), tileDrawn(newBag), tileDrawn(newBag), tileDrawn(newBag), tileDrawn(newBag), tileDrawn(newBag), tileDrawn(newBag)]
    return assignedTiles

print(playScrabble())