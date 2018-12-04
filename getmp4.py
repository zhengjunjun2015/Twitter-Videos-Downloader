import tweepy
import json

def authorize(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
    twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return twitter_auth

def gettimeline(twitter_auth):
    api = tweepy.API(twitter_auth)
    #timeline = api.search(q = 'tiffany' 'リンク', lang='ja', count=20)
    timeline = api.search(q = 'filter:native_video',  lang='ja', count=10)
    return timeline

def getmp4(timeline):
    #for i in range(len(timeline)):
    #    print(timeline[i])
    json = timeline[0]._json["extended_entities"]["media"][0]["video_info"]["variants"]
    return json

#print(usertimeline[0]._json["extended_entities"]["media"][0]["video_info"]["variants"][1]["url"])
def main():
#    consumer_key = 'zuu1hu9adiao1qjwqnqrigvvt'
#    consumer_secret = 'lrlifh0noo8sobarnmcim952zq0brszectqwpzbackhhdq3ywq'
#    access_token = '796211582837501953-29g90kxysztzbggaekssitlz7nagtdd'
#    access_token_secret = 'sktjfr6d07mwqu1o4ik3k4bferwvkyupfxnqt5z2i9biq'
    consumer_key = 'kdqWRbGA2s7sHjBHSx0VrVUJd'
    consumer_secret = 'GerdaAl9tSplFtZT9QOakiah4QoiuCrg0qVd48ZIpLDeV44EGt'
    access_token = '796211582837501953-AAOcqcl02kRIhwUR86XvFKW6dTN99dY'
    access_token_secret = 'd0lb9qtZQXD5Gu2D4LFZj1RuWbBlfu4ThGCgm8CLBYKsT'
#    q_list = ['filter:native_video',
#            'lang:jamin_retweets:50',
#            'count = 50',]

    timeline = gettimeline(authorize(consumer_key, consumer_secret, access_token, access_token_secret))
    print(getmp4(timeline))

if __name__ == '__main__':
    main()
