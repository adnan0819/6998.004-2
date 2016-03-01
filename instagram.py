from sys import stdout
import requests
import json
import time
import sys
import datetime  
reload(sys)  
sys.setdefaultencoding('utf-8') 

# In this Python Script, I am polling the Instagram API every two seconds
# to monitor the hashtag (#fire and #nyc or #NYC appearing together and their locations.
# The warning message from the API is natural because we are not using OAuth
# or else you would have to log in using your Instagram ID
# There are high chances that you will not get a meaningful alert in the web interface unless there is 
# a fire in New York City and someone is putting it on Instagram.
# As a proxy for demo (should you run it), I encourage you to replace the string
# "fire" to "food" in line 39 because "food" posts are much more common and will
# send you an alert based on the freuency of posts/rate.


tagId=0 #Preliminary id of the post
tagFireId=0 #preliminary ID of #fire so we do not repeat the same post twice
tagFireIdPrev=-1 #this is a placeholder for a fire hashtag that stores the "previous" post's ID to avoid repetition

# The following infinite loop will run forever polling Instagram's "recent posts" endpoint
# and return only posts that have #fire and (#NYC or #nyc) in them.
while True:
    #This is the infinite loop to call the "recent tags" endpoint of Instagram API
    r = requests.get("https://api.instagram.com/v1/tags/latergram/media/recent?access_token=186174857.3d82e12.e8205e331f0a47499a1e4008c3b86f3b")
    for m in r.json()["data"]:


            tagId=m["id"] #this is the ID of the specific post

            # The following if statements search for the substring of "fire"
            # in the hashtag array.
            # From these filtered posts, we extract the date, location, longitude and latitude
            # Any image without geolocation is discarded
            if any("fire" in s for s in m["tags"]): #Checking for #Fire
                    if any("nyc" or "NYC" in x for x in m["tags"]): #checking for (#nyc or #NYC)
                                #Storing the Instagram given post ID to recognize the post later to avoid repetition
                                tagFireId=m["id"]
                                #The next if block discard posts without geolocation or posts that have appeared already
                                if(tagFireIdPrev==tagFireId):
                                 #m["location"]==None or 
                                    a=0 #do nothing
                 
                                else:
                                    #This block prints all the posts with the conditions met. 
                                    tagFireId=m["id"] #storing the Instagram given unique ID
                                    print json.dumps({"hashtag": "fire", "time": m["created_time"]}) 
                                    sys.stdout.flush()
                                    tagFireIdPrev=tagFireId #Assigning this particular post to "previous" id because we are done with it. 

    time.sleep(2) #Sleeping for two seconds (polling every two seconds)
 