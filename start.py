from datetime import datetime
from twitter import *
import os


def create(file, date):
    f = open(file, 'w')
    text = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Tapas Theory</title>
        <!-- meta name="viewport" content="width=device-width, initial-scale=1" -->
        <!--link rel="stylesheet" type="text/css" media="screen" href="main.css" / -->
        <script src="main.js"></script>
    </head>
    <body>
    <h1>Hello World</h1>
    <h2>Updated """ + date + """</h2>
    <p><a href="twitter/fwsthlm.html">The Twitter Tapas</a> </p>
    </body>
    </html>"""
    f.write(text)

def createTwitterPage(file, contentFile):
    f = open(file, 'w')
    text = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Tapas Theory</title>
        <!-- meta name="viewport" content="width=device-width, initial-scale=1" -->
        <!--link rel="stylesheet" type="text/css" media="screen" href="main.css" / -->
        <script src="main.js"></script>
    </head>
    <body>
    <h1>Twitter Tapas</h1>
    <h2>The twitter tapas for fwsthlm</h2>
    <p><a href="../index.html">Home</a> </p>
    """
    content = getContentFromFile(contentFile)
    if content is not None:
        text += content
    text += """
    </body>
    </html>"""
    f.write(text)

def createTwitterData():
    #t = Twitter(auth=OAuth("JXLBr4AACnVzgZAVjDFhlETIv", "LlO8wNFXWGhTA0gff3fssRmB3h8lnIZOes1Iybp1bdtL5XGFpr", "750741242846248960-yvsRcSVRBOsyAX8VbO9HAmLIjF6fb0R", "TfKcfloulOz8DPyX7MHoLDObttWv55yiyNs9Szh7D4DqA"))
    t = Twitter(auth=OAuth("750741242846248960-yvsRcSVRBOsyAX8VbO9HAmLIjF6fb0R", "TfKcfloulOz8DPyX7MHoLDObttWv55yiyNs9Szh7D4DqA", "JXLBr4AACnVzgZAVjDFhlETIv", "LlO8wNFXWGhTA0gff3fssRmB3h8lnIZOes1Iybp1bdtL5XGFpr"))
    #t.statuses.home_timeline()
    #followerList = t.followers.list(screen_name="fwsthlm")
    #print("Size of followerList: " + str(len(followerList)))
    #for x in followerList["users"]:
    #    print(x["id"])
    followerList = t.followers.ids(screen_name="fwsthlm")
    #print("Size of followerList: " + str(len(followerList)))
    #for x in followerList["ids"]:
        #print(x)
    
    #print("Number of followers: " + str(len(followerList["ids"])))
    #JXLBr4AACnVzgZAVjDFhlETIv (API key)
    #LlO8wNFXWGhTA0gff3fssRmB3h8lnIZOes1Iybp1bdtL5XGFpr (API secret key)
    #750741242846248960-yvsRcSVRBOsyAX8VbO9HAmLIjF6fb0R (Access token)
    #TfKcfloulOz8DPyX7MHoLDObttWv55yiyNs9Szh7D4DqA (Access token secret)
    results = list(map(str, followerList["ids"]))
    return results;

def getPreviousFollowers(file):
    if os.path.isfile(file):
        #lines = [line.rstrip('\r\n') for line in open(file)]
        #f = open(file, "r")
        #if f.mode == 'r':
            #lines = f.read().splitlines()
            #print("Read " + str(len(lines)) + " lines.")
        lines = list()
        with open(file) as f:
            x = 0
            for line in f:
                #print(str(x) + ": " + line.rstrip('\n'))
                x = x + 1
                lines.append(line.rstrip('\n'))
        return lines

def getContentFromFile(file):
    if os.path.isfile(file):
        f = open(file, "r")
        if f.mode == 'r':
            return f.read()

def Diff(li1, li2): 
    return (list(set(li1) - set(li2)))

def saveFollowerListToFile(file, listOfFollowers):
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))
    f = open(file, "w+")
    for x in listOfFollowers:
        f.write(str(x) + "\n")
    f.close

def saveUnfollowerListToFile(file, listOfUnfollowers):
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))
    f = open(file, "a+")
    f.seek(0)
    for x in listOfUnfollowers:
        f.write("<p>" + str(x) + " unfollowed.</p>\n")
    f.close

now = datetime.now() # current date and time
today = now.strftime("%Y%m%d-%H:%M:%S")
#create("C:\\Users\\Fredrik\\git\\http-sandbox\\index.html", today)
create("/data/data/com.termux/files/home/git/http-sandbox/index.html", today)


currentFollowerList = createTwitterData();
#print("Size of current follower list: " + str(len(currentFollowerList)))
#previousFollowerList = getPreviousFollowers("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\fwsthlm\\followers.txt")
previousFollowerList = getPreviousFollowers("/data/data/com.termux/files/home/git/http-sandbox/twitter/fwsthlm/followers.txt")
#print("Size of previous follower list: " + str(len(previousFollowerList)))
if previousFollowerList is not None:
    unfollowerList = Diff(previousFollowerList, currentFollowerList)
    #print("Size of unfollowerList: " + str(len(unfollowerList)))
    #saveUnfollowerListToFile("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\fwsthlm\\unfollowers.txt", unfollowerList)
    saveUnfollowerListToFile("/data/data/com.termux/files/home/git/http-sandbox/twitter/fwsthlm/unfollowers.txt", unfollowerList)
    #for x in unfollowerList:
        #print(x + " unfollowed")
#saveFollowerListToFile("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\fwsthlm\\followers.txt", currentFollowerList)
saveFollowerListToFile("/data/data/com.termux/files/home/git/http-sandbox/twitter/fwsthlm/followers.txt", currentFollowerList)

#createTwitterPage("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\fwsthlm.html",
                #"C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\fwsthlm\\unfollowers.txt")
createTwitterPage("/data/data/com.termux/files/home/git/http-sandbox/twitter/fwsthlm.html",
                "/data/data/com.termux/files/home/git/http-sandbox/twitter/fwsthlm/unfollowers.txt")
#currentFollowerList = createTwitterData();
#previousFollowerList = getPreviousFollowers("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\fwsthlm\\followers.txt")
#unfollowerList = Diff(previousFollowerList, currentFollowerList)
#print("Size of unfollowerList: " + str(len(unfollowerList)))
