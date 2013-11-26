#Meghna Kaul 
#This program uses two functions to determine which word in the dictionary is closest to the user word. The first function, the
#distance function, uses the Levenshtein distance too see how far apart the two words are. This is a better and more accurate
#system than the hamming distance because hamming distance only handles cases of substitution, whereas this handles cases of 
#substituion, insertion and deletion. The autocorrect function keeps track of the closest word and the least distance, and calls
#the word distance fucntion. This function finds a word that has a certain distance from the user word, it will user that distance as least distance, 
#and it will keeping looking for words with smaller distances, and if it finds a word with a smaller distance, that becomes the new closest word. 
#Then it returns the word that is closest to the user word. Extension: I wanted to make a slight optimization in the autocorrect function so that it 
#could "eliminate" some words and not have to recurse through the whole dictionary, so I added lines 43-44 which say that if it looks at a word whose 
#distance from the user word is > the currect least distance, don't even implement the Levenstein distance function and just go to the next word in 
#the dictionary (this saves some time because it doesn't have to recurse through the entire dictionary). 
with open ('words') as wordfile: 
  words = wordfile.read().splitlines() 

user_word = raw_input('Type in a word: ')

    
def word_distance(word_1, word_2): # Word Distance Function #Used Levenshtein distance 
  #Base Case 
  if word_1 == '': 
    return len(word_2) 
  elif word_2 == '':
    return len(word_1) 
    
  #Recusive Step #Handles cases of substituion, deletion and insertion of letters 
  elif word_1[0] == word_2[0]: 
    return 0 + word_distance(word_1[1:], word_2[1:])
  else: 
    substitution = 1 + word_distance(word_1[1:], word_2[1:]) 
    deletion = 1 + word_distance(word_1[1:], word_2) 
    insertion = 1 + word_distance(word_1, word_2[1:]) 
    return min(substitution, deletion, insertion) 
    
  
def autocorrect (word): #Autocorrect Function
  if word in words:  
    return word #This returns the user word if it is correctly spelled.
  else:
    least_distance = 100000000000 
    closest_word = None 
    for w in words: 
      if abs(len(word)-len(w)) >= least_distance: #Optimization- this eliminates some words so we don't have to recurse through the whole dictionary 
        continue #New syntax; this tells it to go back up to the top of the for loop with the next value (word) in the list (dictionary) 
      distance = word_distance(word,w) #This is when it actually calculates distance (calling the distance function) 
      if distance < least_distance:
        least_distance = distance
        closest_word = w 
    return closest_word 

print autocorrect(user_word) 

#Sources:
#http://en.wikipedia.org/wiki/Levenshtein_distance #I know this shouldn't technically be a source but I used it to get an idea of what Levenshtein is 
#http://rosettacode.org/wiki/Levenshtein_distance
#Mr. Hickey 


