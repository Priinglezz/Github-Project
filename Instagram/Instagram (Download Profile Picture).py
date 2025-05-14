#the code below allows us to Download
#Instagram Profile Picture of a Stranger or a Friend:
import instaloader
ig = instaloader.Instaloader()
dp = input("Enter Insta username : ")
ig.download_profile(dp, profile_pic_only=True)