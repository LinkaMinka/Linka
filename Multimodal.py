import random
onlinegames=('Smash Siblings','Airsoft Simulator','Very Hard MLG Pro Game','Fantasy Dragons')
offlinegames=('Simulator Metropalis','Friend Monsters','Fantasy Dragons','Very Hard MLG Pro Game')
def start():
    name=input('What is your name?: ')
    print('\n Video games have been around for a while now, people of all kinds of backgrounds enjoy some time off whith all kinds of games. There are so many genres, just \n like how there are so many kinds of books and movies')
    x=input('\n Do you agree that video games are good? Type(Yes or No): ')
    if x=='Yes':
        print('\n {}, you are of the younger generation that grew up on video games and this \n is just another way to be entertained'.format(name))
        game(name)
    if x=='No':
        print('\n {} you are an older person, and believe that video games will destroy mankind. \n Ignoring that this is what even older generation thought of \n magazines, radios, movies, and much more.'.format(name))
        old(name)

def game(x):
    mode=input('Do you have fast internet?: ')
    if mode=='Yes':
        print('\n You got a chance to play these games, {}'.format(onlinegames))
    if mode=='No':
        print('\n You got the chance to play these games, {}'.format(offlinegames))
    game=input('What do you want to play?: ')
    if game=='Smash Siblings':
        print('This game is about fighting, you play as character from other franchises, and it is fast paced')
    if game=='Airsoft Simulator':
        print('This game can be in various settings that are known for wars, popular titles often take place in World War 1 or 2')
    if game=='Very Hard MLG Pro Game':
        print('This game is known to be very hard, but it is fair in its mechanics and rewards mastery of the game')
    if game=='Fantasy Dragons':
        print('This takes place in a fantsy world filled with magic, monsters, and dragons. You can appreciate the time and effort it took to create an interesting world')
    if game=='Simulator Metropalis':
        print('This game allows you to make your own city, and you can be as good or evil you want to your fake citizens')
    if game=='Friend Monsters':
        print('You collect cute monsters and train them for battles. With your monsters you travel accross the country for adventure')
    friends(x,game)

            
def friends(n,g):
    if g in onlinegames:
        print('\n {} has a chat function, and you can talk to people online'.format(g))
        print('You played this game hours on end, and you ended up talking to people')
        print('Months later, you still talk to these same group, all of them are miles away from each other')
        print('You became friends, years past and these are still one of your best friends, and to this day still play {} with your friends'.format(g))
        if g in offlinegames:
            pass
    if g in offlinegames:
        print('\n {} does not have an online funtion'.format(g))
        how=input('Go to School Clubs or Online Server?: ')
        if how=='School Clubs':
            print('\n Your school has a dedicated club for video games. It could be any kind, everyone can join')
            d=input('How dedicated are you to the club? Very or Not At All?: ')
            if d=='Very':
                print('You make many friends and help with the club as much as possible')
                print('Later, you become the president of the club. Everyone knows about {}'.format(n))
                print('They were friendly, helpful, and a very nice person. And they always made people feel welcomed into the club')
        if how=='Online Server':
            print('There is a chat website and app, called Doscord')
            print('Doscord allows you to talk about anything to many people')
            print('You joined a group chat dedicated to {}'.format(g))
            print('Over the years, you made many friends from all around the globe')
            print('You know these are good people, and you are glad that you found people who understand you')
    arts(n,g)


def arts(na,ga):
    print('\n You are very fond of {}. All of its mechanics, story, world building'.format(ga))
    print('You want to show your appreaciation, but how?')
    print('You know people Paint, Write, or even Program')
    a=input('what will you do?: ')
    if a=='Paint':
        print('You draw fanart of your favorite character in {}'.format(ga))
        print('You start a Pictogram account, so you can post your art to the internet')
        print('You finf that people enjoy your art, and are waiting patiently for more')
        print('You get positive messages from strangrs who say your art makes their day')
        print('You start doing commisions, and everyone wants to buy your art')
        print('Years past, and everyone knows abou {}'.format(na))
        print('The one who makes beautiful, colorful, dynamic art')
        print('Who started by posting fanart of {} on the internet'.format(ga))
    if a=='Write':
        print('You love the stories and characters from {}'.format(ga))
        print('You finf that they are full of life, depth, and really make you think')
        print('This made you inspired to write fanfiction, which you post on Toombler')
        print('People comments saying these are very accurate portayals of the characters of {}'.format(ga))
        print('You wanted to make your own stories, completely new, unrelated to {}'.format(ga))
        print('You post it on the internet, and people love it')
        print('It took you a couple years, but you managed to get your stories published and read by the public')
        print('People know you as {}, the person who writes fantastic stories that everyone enjoys'.format(na))
    if a=='Program':
        print('You loved the mechanics of {}'.format(ga))
        print('You started to get interested in how they work')
        print('You started to teach yourself how to program, and hopefully make your own games')
        print("You manage to do more than the beginners' 'Hello World'")
        print('On the internet, you post pictures and videos of your prototype. Even the code')
        print('Years past and you make brilliant indie games, such as cubecraft and Rivers Inc.')
        print('You are known as {}. The one who revolutionised the gaming industry'.format(na))
    end(na)


def old(x):
    print('You do not understand video games, but your relatives do')
    print('You see your siblings, cousins, maybe even the younger generation, play these video games')
    print('After a while, you lightened up, and tried these strange intractive thingamajigs')
    oldgame(x)

def oldgame(x):
    mode=input('Do you have fast internet?: ')
    if mode=='Yes':
        print('\n You got a chance to play these games, {}'.format(onlinegames))
    if mode=='No':
        print('\n You got the chance to play these games, {}'.format(offlinegames))
    game=input('What do you want to play?: ')
    if game=='Smash Siblings':
        print('This game is about fighting, you play as character from other franchises, and it is fast paced')
    if game=='Airsoft Simulator':
        print('This game can be in various settings that are known for wars, popular titles often take place in World War 1 or 2')
    if game=='Very Hard MLG Pro Game':
        print('This game is known to be very hard, but it is fair in its mechanics and rewards mastery of the game')
    if game=='Fantasy Dragons':
        print('This takes place in a fantsy world filled with magic, monsters, and dragons. You can appreciate the time and effort it took to create an interesting world')
    if game=='Simulator Metropalis':
        print('This game allows you to make your own city, and you can be as good or evil you want to your fake citizens')
    if game=='Friend Monsters':
        print('You collect cute monsters and train them for battles. With your monsters you travel accross the country for adventure')
    oldfriends(x,game)


def oldfriends(n,g):
    if g in onlinegames:
        print('\n {} has a chat function, and you can talk to people online'.format(g))
        print('You played this game hours on end, and you ended up talking to people')
        print('Months later, you still talk to these same group, all of them are miles away from each other')
        print('You became friends, years past and these are still one of your best friends, and to this day still play {} with your friends'.format(g))
        if g in offlinegames:
            pass
    if g in offlinegames:
        print('\n {} does not have an online funtion'.format(g))
        how=input('Go to Public Forums or Online Server?: ')
        if how=='Public Forums':
            print('\n Your forum has a dedicated club for video games. It could be any kind, everyone can join')
            d=input('How dedicated are you to the club? Very or Not At All?: ')
            if d=='Very':
                print('You make many friends and help with the club as much as possible')
                print('Later, you become the president of the club. Everyone knows about {}'.format(n))
                print('They were friendly, helpful, and a very nice person. And they always made people feel welcomed into the club')
        if how=='Online Server':
            print('There is a chat website and app, called Doscord')
            print('Doscord allows you to talk about anything to many people')
            print('You joined a group chat dedicated to {}'.format(g))
            print('Over the years, you made many friends from all around the globe')
            print('You know these are good people, and you are glad that you found people who understand you')
    arts(n,g)


def end(n):
    print('Thank you for playing, {}'.format(n))

start()
