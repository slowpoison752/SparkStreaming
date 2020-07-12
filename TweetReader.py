#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from tweepy import OAuthHandler,Stream


# In[ ]:


from tweepy.streaming import StreamListener
import socket
import json


# In[ ]:


api_key = 'o3TX2wy2tEupR4OoCQ4eBbPYh'
api_secret = '9zDD5cK0kF3XBOaMXqCbFUb6wXvDAzP4br3PnNhs2T32KaU3rs'
access_token = '1282405177517993984-FzGJqXnvmCQCAucZzeZas5OJOMGEen'
access_secret = 'dF68W51TnB2bvWWsfgp30zhRan6wKvHMjPj22qTkI9B57'


# In[ ]:


class TwitterListener(StreamListener):
    
    def __init__(self,csocket):
        self.client_socket =csocket
    
    def on_data(self,data):
        
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print('ERROR',e)
        return True
    
    def on_error(self,status):
        print(status)
        return True


# In[ ]:


def sendData(c_socket):
    auth = OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_secret)
    
    twitter_stream = Stream(auth,TwitterListener(c_socket))
    twitter_stream.filter(track=['cricket'])


# In[ ]:


if __name__ =='__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 9990
    s.bind((host,port))
    
    print('listening on port 9990')
    
    s.listen(5)
    c,addr=s.accept()
    
    sendData(c)


# In[ ]:




