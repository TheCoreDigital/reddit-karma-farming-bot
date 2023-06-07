import logging
import requests
import praw
import time
from dotenv import dotenv_values

config = dotenv_values("config.env")

CLIENT_ID = config['reddit_id']
CLIENT_SECRET = config['reddit_secret']
username = config['reddit_username']
password = config['reddit_password']

vis = {}
comments = [
    "upvoted you. Can you upvote back plz ?",
    "Up me. I have upvoted you.",
    "Really need of upvotes here.",
    "Gotchu with an upvote. Up me as well",
    "done bro. upvote you",
    "upvoted you. anything else",
    "u r awesome. upvoted you",
    "luv to see guys like u. upvoted..",
    "wut a funny guy, can a i get an upvote plz",
    "this post is just hilarious",
    "upvoted ur recent posts. upvote me as well",
    "dont know about u but I upvoted.",
    "this is fun. Upvote me as well.",
    "can we trade upvotes? upvoted",
    "Free karma for you and me both",
    "I upvoted pls pls pls upvote back",
    "Looking to trade an upvote or two, return the one I just gave you on some recent posts of mine?",
    "upvote me back pls <3",
    "upvote me for god sake. have a long life.",
    "Just 4 karma plz and TY",
    "Hope you enjoy the rest of your day! Just upvoted you, could you return on a post or two?",
    "You get an upvote! I get an upvote! Everybody gets an upvote!!",
    "have just upvoted you :D Could you please return the favor on my top posts?",
    "upvote you mate. Please come back and vote",
    "help a mate. upvote me",
    "upvote is very necessary, Plz upvote me",
    "need help to gain karma. Upvote you mate. Help me as well",
    "Well, here is an upvote! Please return on some posts of mine?",
    "You have just been upvoted by yours truly. Please return the favor on some of my posts?",
    "Help me. really need karma to post. Upvote you.",
    "can u return the favour that I just upvoted you.",
    "can we trade some upvotes here and there. upvoted u",
    "upvoted, plz show some luv on my recent posts",
    "upvoted needed badly, upvoted you and ur recent posts"
]
n = len(comments)

def check(res):
    rem_requests = int(float(res.headers["x-ratelimit-remaining"]))
    rem_time = int(float(res.headers["x-ratelimit-reset"]))
    
    if(rem_requests <= 5):
        print("Waiting for ", rem_time+20, "s")
        time.sleep(rem_time+20)
    
    print("Remaining requests per 10 mins: ", str(rem_requests))
    
ptr = 0
total_time_taken = time.time()
total_comments_did = 0
last = time.time()
start_time = time.time()
ok = False

while(True): 
    
    taken = time.time() - last
    
    if(taken >= 3300 or ok == False):
        #authorizing
        ok = True
        last = time.time()
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        
        data = {'grant_type': 'password',
                'username': username,
                'password': password }

        headers = {'User-Agent': 'MyBot/0.0.1'}

        Res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=headers)

        TOKEN = Res.json()['access_token']
        
        headers['Authorization'] = 'bearer ' + TOKEN

        ##auth done
    
    Res = requests.get("https://oauth.reddit.com/r/FreeKarma4U/hot",
                       headers=headers, params = {'limit' : '20'})
    res = Res.json()
        
    check(Res)
    print("-------TIME TAKEN: " , int(time.time() - start_time))
    
    item = res['data']['children'][0]
    
    
    for p in res['data']['children']:
        post_id = p['data']['id']
        
        print("GOT post id: ", post_id)

        Res = requests.get('https://oauth.reddit.com/r/FreeKarma4U/comments/' + post_id, headers = headers)
        res = Res.json()

        check(Res)
        print("-------TIME TAKEN: " , int(time.time() - start_time))
        
        
        print("GOT comment ids........")
        print("Post_id: ", post_id, " Total comments: ", str(len(res[1]['data']['children'])))
        
        

        for p in res[1]['data']['children']:
            #iterate over all comment ids
            comment_id = p.get('data').get('id')

            if(comment_id is not None and vis.get(comment_id) is None):
                vis[comment_id] = True

                Res = requests.post("https://oauth.reddit.com/api/comment", 
                                    data = { 'parent' : 't1_'+ comment_id,'text' : comments[ptr]},
                                    headers=headers)
                check(Res)
                print("-------TIME TAKEN: " , int(time.time() - start_time))
                
                
                ptr = (ptr + 1) % n
                total_comments_did += 1
                print("------------COMMENTED on id: ", comment_id, "   Total comments: ", total_comments_did)    
