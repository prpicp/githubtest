libs = ["Today, every student has a computer small enough to fit into his <noun>. He can solve any math problem by simply pushing the computer’s little <plno>. Computers can add, multiply, divide, and <verb>. They can also <verb> better than a human. Some computers are <bodp>. Others have a <adje> screen that shows all kinds of <plno> and <adje> figures.",
        "This summer I went to band camp in <city> for <numb> days. I made friends with <cele> and <cele>. I learned how to play the <inst> <adve>. My favourite part of camp was learning to play <song> in c minor. My least favourite part was my bunkmate’s snoring which was flat and it sounded like a <inst>. During the talent show, I played <song> on the <instrument> in the style of <genr>, while doing the <danc>. One camper <veed> during my performance! I can’t wait to share my <adje> photos with my friends and give them a <adje> performance!",
        "My name is <name> and I’ve known the graduate for <numb> years. I <verb> all the way from <noun> to celebrate this day. I can still remember when you were in <numb> grade. How the time has flown by. My best advice is ‘Be sure to <verb> before you <verb>, but don’t ever <verb> your professor.’ On your first day of <noun> don’t forget to <verb>! On Friday nights don’t <verb> at least until you have a noun. College is <verb> so you will need <noun>. I wish you <noun> and <noun> on this new step in life.",
        "There are many kinds of <adje> animals that <verb> on a farm. For example, <anis> and <anis> <verb> eggs, and <food> comes from farm-raised <anis> and <anis> make <liquid> that people drink and also use to make <food> and <food>. Some farm animals like <anis> and <anis> have soft <noun>, which is used to make <clot> and <plno>.",
        "Last week was my birthday. We went to my Grandma’s house and had <food> for supper. After that, we all sat in the <room> to open my presents. The first gift was from <name>, and it was a <noun>. The next gift was from <name> and it was a <adje> <noun>. The gift after that was a <noun>. I pretended to be happy, but I already had one of those. All of a sudden, I heard a strange noise. The noise was <adje> and I couldn’t tell where it was coming from. I looked around the room. I stood up and walked <adve> to the <diro>. I looked in the <noun>. I looked under the <noun>. I even looked in the <noun>. I found nothing! I realised that everyone in the other room was laughing! I asked my friend <name>. ‘What’s going on?’ I asked my other friend <name>, and they just laughed. I asked <name> but they <verb> around the room. I heard the noise again. Suddenly, it occurred to me that the noise was coming from one of the presents! I opened the gift and inside the box was a baby <animal>! I was surprised.",
        "Our <plno> are packed for a hike in the <adje> Mountains! We are carrying a picnic lunch with <food> and <food> on our <body>, and I have a <noun> for <ving> photos. We will <verb> past meadows filled with <colo> and <colo> flowers, and pass a <adje> waterfall that sounds like a <noun>. Many animals live in the mountains, like the <adje> <anim> and <adje> <anim>. It’s fun to <verb> them but important to be safe and keep a <adje> distance. The higher we <verb>, the smaller the wildflower meadow and waterfall appear; we may even see <noun> still on the ground from last winter."]
#libs array stores all the mad libs scripts
types = ["noun", "plno", "verb", "ving", "veed", "adje", "food", "liqu", "colo", "anmi", "anis", "room", "city", "bodp", "name", "cele", "genr", "inst", "song", "danc", "numb"]
#types stores the word type in <>
questions = ["Enter a noun: ", "Enter a plural noun: ", "Enter a verb: ", "Enter a verb ending in -ing: ", "Enter a verb ending in -ed", "Enter an adjective: ", "Enter a food: ", "Enter a liquid: ", "Enter a colour: ", "Enter an animal: ", "Enter an animal, plural: ", "Enter a room in a house: ", "Enter a city: ", "Enter a body part, plural: ", "Enter a name:", "Enter the name of a celebrity: ", "Enter a genre of music: ", "Enter an instrument", "Enter the name of a song and who it is by", "Enter a dance style or type: ", "Enter a number: "]
#questions stores the corresponding questions to the word types
explain = ["a person, place, or thing (eg. teacher, chicago, table)", "more than one of a person, place, or thing. usually ending in -s or -es (eg. witches, spoons, children)", "a doing word (eg. slide, smell, throw)", "a doing word ending in -ing (eg. swimming, cooking, cleaning)", "a doing word ending in -ed (eg. clapped, hugged, cried)", "a describing word (eg. large, beautiful, wonderful)", "(eg. cheese, beans, pringles)", "(eg. water, coke, orange juice)", "(eg. blue, silver, hot pink)", "(eg. fox, rabbit, panda)", "more than one of an animal. usually ending in -s or -es (eg. pigs, horses, fish)", "(eg. kitchen, bedroom, bathroom)", "(eg. sydney, london, paris)", "more than one of a body part, usually ending in -s or -es (eg. fingers, legs, backs)", "(eg. george, katy, ash)", "(eg. tom holland, zendaya, jeffree star)", "(eg. blues, pop, jazz)", "(eg. trumpet, drums, violin)", "(eg. all star by smash mouth, starboy by the weeknd, flashing lights by kanye west and dwele)", "(eg. the waltz, YMCA, sprinkler)", "(eg. 5, 1492, 4.57)"]
#explain stores examples of word types

print("1 - the magic computers")
print("2 - band camp")
print("3 - graduation")
print("4 - farm animals")
print("5 - birthday surprise")
print("6 - a hike in the mountains")
choice = int(input("which mad libs would you like to do? "))
text = libs[choice]
#if "help" is written then show tool tip

x = 0 #tracker for position of f
j = 0 #tracker for position after last recorded word type/ start
newword = ""
compbit = ""
for f in text:
    x += 1
    if f == "<":
        grabpart = text[j:x-1] #all characters in between start/last word type and new word type
        wordcategory = text[x:x+4] #word type in between <>
        #subroutine to determine word type what it gives back is the new word
        toadd = grabpart + newword #Text bit between start/last word type and new word type + fitting word from user
        compbit = compbit + toadd  #completed part of script saved after user inputs word
    else:
        ''
finalscript = compbit + text[j:] #Adding last bit of text after last word category
print (finalscript)
speech = input("type 'yes' if you would like the computer to read the script out loud for you")

#changingword(wordcategory, )



wordcategory = "f3eded"

counter = 1
def fittingword(wordcategory):
    for c in category:

        counter += 1


if else then print invalid try again

/ checking for a/ an