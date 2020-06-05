libs = "There are many, <adje>, ways to choose a/an, <noun>, to read."
j = 0 #tracker for position after last recorded word type
x = 0 #tracker for position of f
NewWord = ""
CompBit= ""
for f in libs:
    x = x + 1
    if f == "<":
        GrabPart = libs[j:x-1] #all words in between start/last word type and new word type
        WordCategory = libs[x:x+4] #word type in between <>
        if WordCategory == "adje":
            NewWord = input("Enter an adjective: ")
        elif WordCategory == "noun":
            NewWord = input("Enter a noun: ")
        else:
            print("error")
        ToAdd = GrabPart + NewWord #Text bit between start/last word type and new word type + fitting word from user
        CompBit = CompBit + ToAdd #Ongoing saved script
        j = x + 6
    else:
        ''
FinalScript = CompBit + libs[j:] #Adding last bit of text after last word category
print(FinalScript)
