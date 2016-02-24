import json
import sys
import redis

#This Python script inserts the key-value pair of Time (from the Instagram API in UNIX timestamp/epochs) and the deltas
#between messages/posts
conn = redis.Redis()

#The following infinite loop runs forever and calculates the deltas with a life span of two minutes = 120 seconds
#in redis. 
while True:

    line = sys.stdin.readline() #This line reads the feeds from the script delta.py where the time difference between messages are printed out in JSON format
    d = json.loads(line) #The feed is read
    delta = d["delta"] #assigning the read JSON node d["delta"] to the variable delta
    time = d["t"] #assigning the timestamp from Instagram API of the post to the variable time
    print time
    print delta
    conn.setex(time, delta, 120) #setting the key-value pair of time and delta with a lifespan of two minutes
    #print json.dumps({"time":time, "delta":delta}) #printing the key-value pair to be fed to rate.py in JSON format