import tweepy
import json
import requests
import datetime
import sys

def authorize(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
    twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return twitter_auth

def get_timeline(twitter_auth):
    api = tweepy.API(twitter_auth)
    timeline = api.search(q = 'filter:native_video',  lang='ja', count=50)
    return timeline

def get_url(timeline):
    urls = []
    for num in range(0, len(timeline)-1):
        json = timeline[num]._json
        try:
            url = json["extended_entities"]["media"][0]["video_info"]["variants"][0]['url']
            urls.append(url)
        except KeyError:
            continue
    return urls

def save_videos(urls):
    count = 1
    today = str(datetime.date.today())
    for url in urls:
        response = requests.get(url)
        with open('./results/'+ today + str(count) + '.mp4', 'wb') as f:
            f.write(response.content)
        count += 1
        sys.stdout.write('.')
        sys.stdout.flush()

def main():
    consumer_key = 'kdqWRbGA2s7sHjBHSx0VrVUJd'
    consumer_secret = 'GerdaAl9tSplFtZT9QOakiah4QoiuCrg0qVd48ZIpLDeV44EGt'
    access_token = '796211582837501953-AAOcqcl02kRIhwUR86XvFKW6dTN99dY'
    access_token_secret = 'd0lb9qtZQXD5Gu2D4LFZj1RuWbBlfu4ThGCgm8CLBYKsT'

    timeline = get_timeline(authorize(consumer_key, consumer_secret, access_token, access_token_secret))
    urls = get_url(timeline)
    save_videos(urls)

if __name__ == '__main__':
    main()
