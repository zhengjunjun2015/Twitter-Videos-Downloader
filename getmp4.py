# -*- coding: utf-8 -*-
import tweepy
import sys
import json
import requests
import datetime

def authorize(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
    twitter_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return twitter_auth

def get_timeline(twitter_auth, pages):
    api = tweepy.API(twitter_auth)
    #timeline = api.search(q = 'filter:native_video',  lang='ja', count=50)
    # とりあえずユーザーから取得
    timeline = api.user_timeline('buzzgamisama', count=pages, )
    return timeline

def get_url_and_text(timeline):
    contents = {}
    for num in range(0, len(timeline)-1):
        json = timeline[num]._json
        try:
            text = json['text'].split('http')[0].replace('\n', '') 
            url = json["extended_entities"]["media"][0]["video_info"]["variants"][0]['url']
            contents[url] = text
        except KeyError:
            continue
    return contents

def save_videos(urls):
    count = 1
    today = datetime.date.today()
    for url in urls:
        response = requests.get(url)
        with open('./results/'+ str(today) + str(count) + '.mp4', 'wb') as f:
            f.write(response.content)
        sys.stdout.write('.')
        sys.stdout.flush()
        count += 1

def main():
    with open('keys.txt', 'r') as f:
        keys = f.read().split('\n'[0])

    consumer_key = keys[0]
    consumer_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]

    timeline = get_timeline(authorize(consumer_key, consumer_secret, access_token, access_token_secret), 10)
    contents = get_url_and_text(timeline)
    save_videos(contents.keys())


if __name__ == '__main__':
    main()
