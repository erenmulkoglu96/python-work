import instaloader

ig = instaloader.Instaloader()
dp = input("Instagram Username: ")
ig.download_profile(dp, profile_pic_only=True)
