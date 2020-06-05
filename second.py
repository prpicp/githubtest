libs = [] #array to store enered verbs, nouns, ect...
counter = 0
i = 0
#counter
#with each 'sheet' a limited amount of spaces will be coutned for array spaces
Verb = "Enter a verb: "
Noun = "Enter a noun: "
PluralNoun = "Enter a plural noun: "
Adj = "Enter an adjective: "
BoyName = "Enter a boys name: "
GirlName = "Enter a girls name: "
Clothing = "Enter an article of clothing: "
Place = "Enter a place: "
BodyPart = "Enter a part of the body: "
Number = "Enter a number: "
Celebrity = "Enter the name of a celebrity: "

libs.append(input(Adj))
libs.append(input(Noun))
libs.append(input(PluralNoun))
libs.append(input(GirlName))
libs.append(input(Adj))
libs.append(input(Clothing))
print ("There are many", libs[0], "ways to choose a/an", libs[1],
       "to read. First, you could ask for recomendations from your friends and"
       , libs[2] + ". Just don't ask Aunt", libs[3], "- she only reads" , libs[4],
       "books with", libs[5] + "- ripping goddessess on the cover.")
#function for if vowel[0:1] then a or an
