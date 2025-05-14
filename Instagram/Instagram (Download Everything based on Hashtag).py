##We want to download pictures/videos/hastags/comments from all the posts
#that have the tag called “nflgame”. See the code below to do that.
#In the code below, we are downloading 10 of them – we can change
#that number to 100 or 1500.
#first download library called instaloader.

import instaloader
from instaloader import Profile, Post
instance = instaloader.Instaloader()
instance.download_hashtag(hashtag="nflgame",max_count=10)