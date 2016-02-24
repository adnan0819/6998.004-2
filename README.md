# COMSE6998.004 Assignment 2

# NYC Fire Alert Powered by Instagram 

# - Adnan Firoze (af2728)
# (Dual MS in CS & Journalism)

This project/assignment polls Instagram API's ***recent tags endpoint*** and pulls out "#fire" and ("#NYC" or "nyc") tags appearing together. From there, we calculate the rate and if we find a rate below 60s then we set off an alarm on a web page. 

# Why should one care?

Firstly it has been shown by multiple media outlets that social media has become an extremely efficient means of storytelling. For instance, www.journalism.co.uk pointed out the efficacy of USA's Electiongram and Stormgram that were very effective in the past few years. In their report (https://www.journalism.co.uk/news/-how-bbc-guardian-innovating-instagram/s2/a555771/) they argued that more and more citizen journalists are turning to instagram for breaking news coverage as both consumers and content creators. 

Also, Niemen Labs pointed out the 91 years old lonform narrative journalism magazine - "Virginia Quarterly Review" has found its unique place in Instragram. 

An evident example is the fact that in August 2015, a gas explotion in East Village in NYC was covered on social media specifically Instagram before any news outlet that reside around the area. The incident is covered here: http://www.nytimes.com/2015/03/27/nyregion/reports-of-explosion-in-east-village.html?_r=0

So, I attempted to find and triangulate fire incidents in the NYC area for this assignment. It can be extended for other incident and other places. 


# The Data

The stream I selected is the Instagram recently uploaded hashtag stream from the API endpoint: https://api.instagram.com/v1/tags/latergram/media/recent?access_token=186174857.3d82e12.e8205e331f0a47499a1e4008c3b86f3b .
Note that the access token is mine. 


**What each message mean?**

Every message polled from this refers to the event of a person taking a picture of a specific fire event (at this moment) that relates to the hashtags mentioned. Note that I used a subsring search so even if I am searching for "fire" I will get hashtags like "buidingfire", "firestorm" etc. 


**The nitty-gritty of the codes are well comprehensively commented in the source files**

# Files of Relevance

1. instagram.py
2. delta.py
3. redis-insert.py
4. rate.py
5. index.html

# How to run:

*** Prerequisites: ***

` 1. Python 2,7x `
` 2. Redis `
` 3. Requests ` 
` 4. Websocketd ` 


Assuming you are using a Mac (or any UNIX based terminal) and have the prerequisites (Python 2.7, websocketd) installed the steps are as follows:

1. Download this directory to your computer

2. In the terminal, change to the directory to the directory where the files have been downloaded.

3. I used Python 2.7 (it will not work properly in Python 3.x). Simply type ` python instagram.py | python delta.py | python redis-insert.py ` (without quotes) and hit enter. 

4. Make sure Redis is running (if not running, type in "redis-server" in Terminal assuming it is in the path). Then in a different terminal tab (while point 1 is running) type in ` python rate.py ` and hit enter. 

4. Setting up web socket: Now open another new tab in the terminal (while being in the same directory) and type in the following (without quotes): ` websocketd --port 8080 python instagram.py ` and hit enter. The web socket will be up and running and will be serving over port 8080. 
 
5. Setting up web server: Again open a new terminal tab (WHILE THE PREVIOUS ONE IS RUNNING) and type in ` python -m SimpleHTTPServer ` (without quotes) and hit enter. Now we are good to go as we have this directory serving over port 8000. 

6. Load up the front end: Go to Google Chrome and browse to ` http://localhost:8000/ `

 * For demo purposes, you might want to open the instagram.py script (LINE 39) and replace "fire" to "food" or "selfie" to see immediate results. The reason is, I have tweaked it in a practical manner i.e. for the alarm to go off, the rate has to be less than or equal to 60 seconds. It is highly unlikely that there will be a fire in NYC when you will be running the assignment.  After loading the page, click "Go." The streaming alerting system will start.


**The webpage will go on forever so you need to reload it (as mentioned in the Assignment instructions).**
