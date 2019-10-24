from datetime import datetime
from twitter import *
import os
import time


def create(file, date, twitterAccounts):
    f = open(file, 'w')
    text = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Liga Nord</title>
        <!-- meta name="viewport" content="width=device-width, initial-scale=1" -->
        <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
        <script src="main.js"></script>
    </head>
    <body>
    <div class="header">
        <h1>Liga Nord</h1>
        <p>Updated """ + date + """</p>
    </div> \n"""
    for twitterAccount in twitterAccounts:
        text += """<p><a href="twitter/""" + twitterAccount + """.html">The unfollower history for """ + twitterAccount + """</a> </p>\n"""
    text += """</body>
    </html>"""
    f.write(text)

def createTwitterPage(file, contentFile, twitterAccount):
    f = open(file, 'w')
    text = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Liga Nord</title>
        <!-- meta name="viewport" content="width=device-width, initial-scale=1" -->
        <link rel="stylesheet" type="text/css" media="screen" href="../main.css" />
        <script src="main.js"></script>
    </head>
    <body>
    <div class="header">
        <h1>Liga Nord</h1>
        <p>The history of """ + twitterAccount + """</p>
        <a href="../index.html">Home</a>
    </div> \n
    <p><a href="../index.html">Home</a> </p>
    <div class="timeline">
    """
    
    for line in reversed(list(open(contentFile))):
        text += line.rstrip() + "\n"

#    content = getContentFromFile(contentFile)
#    if content is not None:
#        text += content
    text += """
    </div>
    </body>
    </html>"""
    f.write(text)

def createTwitterData(twitterAccount, t):
    #t = Twitter(auth=OAuth("JXLBr4AACnVzgZAVjDFhlETIv", "LlO8wNFXWGhTA0gff3fssRmB3h8lnIZOes1Iybp1bdtL5XGFpr", "750741242846248960-yvsRcSVRBOsyAX8VbO9HAmLIjF6fb0R", "TfKcfloulOz8DPyX7MHoLDObttWv55yiyNs9Szh7D4DqA"))
    #t = Twitter(auth=OAuth("750741242846248960-yvsRcSVRBOsyAX8VbO9HAmLIjF6fb0R", "TfKcfloulOz8DPyX7MHoLDObttWv55yiyNs9Szh7D4DqA", "JXLBr4AACnVzgZAVjDFhlETIv", "LlO8wNFXWGhTA0gff3fssRmB3h8lnIZOes1Iybp1bdtL5XGFpr"))
    #t.statuses.home_timeline()
    #followerList = t.followers.list(screen_name="fwsthlm")
    #print("Size of followerList: " + str(len(followerList)))
    #for x in followerList["users"]:
    #    print(x["id"])
    cursor = -1
    #api_path = "https://api.twitter.com/1.1/endpoint.json?screen_name=targetUser"

    followerList = t.followers.ids(screen_name=twitterAccount, cursor=cursor)
    time.sleep(60)
    results = list(map(str, followerList["ids"]))
    cursor = followerList["next_cursor"]
    while cursor != 0:
        print("Cursor: " + str(cursor) + ", Total followers for " + twitterAccount + ": " + str(len(results)))
        followerList = t.followers.ids(screen_name=twitterAccount, cursor=cursor)
        time.sleep(60)
        results += list(map(str, followerList["ids"]))
        cursor = followerList["next_cursor"]


    #followerList = t.followers.ids(screen_name=twitterAccount, cursor=cursor)
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

def saveUnfollowerListToFile(file, listOfUnfollowers, today, t):
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))
    f = open(file, "a+")
    f.seek(0)
    for x in listOfUnfollowers:
        try:
            account = t.users.show(user_id=str(x))
            #f.write("<p>" + today + ": " + account["name"] + " <a href=\"https://twitter.com/" + account["screen_name"] + "\">(@" + account["screen_name"] + ", id: " + str(x) + ")</a> unfollowed.</p>\n")
            f.write("<div class=\"container left\"><div class=\"content\"><h2>" + today + "</h2><p>" + account["name"] + " <a href=\"https://twitter.com/" + account["screen_name"] + "\">(@" + account["screen_name"] + ", id: " + str(x) + ")</a> unfollowed.</p></div></div>\n")
        except:
            #f.write("<p>" + today + ": Account with id: " + str(x) + " was suspended.</p>\n")
            f.write("<div class=\"container left\"><div class=\"content\"><h2>" + today + "</h2><p>Account with id: " + str(x) + " was suspended.</p></div></div>\n")
    f.close

twitterAccounts = ["fwsthlm", "aikfotboll"]
now = datetime.now() # current date and time
today = now.strftime("%Y%m%d-%H:%M:%S")
#create("C:\\Users\\Fredrik\\git\\http-sandbox\\index.html", today, twitterAccounts)
create("/data/data/com.termux/files/home/git/http-sandbox/index.html", today, twitterAccounts)
t = Twitter(auth=OAuth("750741242846248960-yvsRcSVRBOsyAX8VbO9HAmLIjF6fb0R", "TfKcfloulOz8DPyX7MHoLDObttWv55yiyNs9Szh7D4DqA", "JXLBr4AACnVzgZAVjDFhlETIv", "LlO8wNFXWGhTA0gff3fssRmB3h8lnIZOes1Iybp1bdtL5XGFpr"))
for twitterAccount in twitterAccounts:
    currentFollowerList = createTwitterData(twitterAccount, t);
    #print("Size of current follower list: " + str(len(currentFollowerList)))
    #previousFollowerList = getPreviousFollowers("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\" + twitterAccount + "\\followers.txt")
    previousFollowerList = getPreviousFollowers("/data/data/com.termux/files/home/git/http-sandbox/twitter/" + twitterAccount + "/followers.txt")
    #print("Size of previous follower list: " + str(len(previousFollowerList)))
    if previousFollowerList is not None:
        unfollowerList = Diff(previousFollowerList, currentFollowerList)
        #print("Size of unfollowerList: " + str(len(unfollowerList)))
        #saveUnfollowerListToFile("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\" + twitterAccount + "\\unfollowers.txt", unfollowerList, today, t)
        saveUnfollowerListToFile("/data/data/com.termux/files/home/git/http-sandbox/twitter/" + twitterAccount + "/unfollowers.txt", unfollowerList, today, t)
        #for x in unfollowerList:
            #print(x + " unfollowed")
    #saveFollowerListToFile("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\" + twitterAccount + "\\followers.txt", currentFollowerList)
    saveFollowerListToFile("/data/data/com.termux/files/home/git/http-sandbox/twitter/" + twitterAccount + "/followers.txt", currentFollowerList)

    #createTwitterPage("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\" + twitterAccount + ".html",
    #                  "C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\" + twitterAccount + "\\unfollowers.txt", twitterAccount)
    createTwitterPage("/data/data/com.termux/files/home/git/http-sandbox/twitter/" + twitterAccount + ".html",
                      "/data/data/com.termux/files/home/git/http-sandbox/twitter/" + twitterAccount + "/unfollowers.txt", twitterAccount)
#currentFollowerList = createTwitterData();
#previousFollowerList = getPreviousFollowers("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\fwsthlm\\followers.txt")
#unfollowerList = Diff(previousFollowerList, currentFollowerList)
#print("Size of unfollowerList: " + str(len(unfollowerList)))
