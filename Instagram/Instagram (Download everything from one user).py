#Download all pictures/videos from someone’s profile
#download all the pictures/videos from someone's profile such as that of Espn or kingjames or
#any other person:
import instaloader
from instaloader import Profile, Post
instance = instaloader.Instaloader()
instance.login(user="Put your IG username here",passwd="Put your Ig password here")
instance.download_profile(profile_name="kingjames")
#The output of this would be inside a new subfolder within your HelloWorld (or any other Python
#Project) folder. This can take quite a while in the event of a very loaded profile but eventually,
#you will find yourself with an enormous amount of data such as:
#.txt files with every caption for every post
# .json files of comment threads for every post
# .jpg files for every post, with the creation date being the actual published date
# and a .jpg file for the Instagram account’s profile picture