import tweepy
import json

def authorize(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
    twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return twitter_auth

def getTimeline(twitter_auth, param):
    api = tweepy.API(twitter_auth)
    timeline = api.search(param)
    return print(timeline)

def getMp4(timeline):
    #for i in range(len(usertimeline)):
    #    print(usertimeline[i])
    return timeline

#print(usertimeline[0]._json["extended_entities"]["media"][0]["video_info"]["variants"][1]["url"])
def main():
    CONSUMER_KEY = 'ZuU1hU9aDiAo1QjWQnQRigvvT'
    CONSUMER_SECRET = 'lrLiFH0Noo8sOBaRnMCIm952ZQ0BRSZEctQWpZBacKhhDQ3yWQ'
    ACCESS_TOKEN = '796211582837501953-29g90KxysZtZbGgaekSSitLZ7nagtdd'
    ACCESS_TOKEN_SECRET = 'skTjfR6d07mWQU1O4iK3k4BfeRWvkyuPfxNqT5z2i9Biq'

    timeline = getTimeline(
            authorize(CONSUMER_KEY,
                CONSUMER_SECRET,
                ACCESS_TOKEN,
                ACCESS_TOKEN_SECRET),
            'filter:native_video lang:jamin_retweets:50')
    print(timeline)

if __name__ == '__main__':
    main()
