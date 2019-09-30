from datetime import datetime

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

def createTwitterPage(file):
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
    </body>
    </html>"""
    f.write(text)

now = datetime.now() # current date and time
today = now.strftime("%Y%m%d-%H:%M:%S")
#create("C:\\Users\\Fredrik\\git\\http-sandbox\\index.html", today)
create("/data/data/com.termux/files/home/git/http-sandbox/index.html", today)
#createTwitterPage("C:\\Users\\Fredrik\\git\\http-sandbox\\twitter\\fwsthlm.html")
createTwitterPage("/data/data/com.termux/files/home/git/http-sandbox/twitter/fwsthlm.html")
