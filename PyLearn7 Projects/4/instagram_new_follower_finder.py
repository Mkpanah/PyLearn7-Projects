import instaloader
import getpass

f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()


L = instaloader.Instaloader()

username = input("username: ")
password = getpass.getpass("password: ")

L.login(user=username, passwd=password)
profile = instaloader.Profile.from_username(L.context, "mkp_1997")

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for new_follower in new_followers:
    if new_follower not in old_followers:
        # print out the followers that has been added in comparison to old followers
        print(new_follower)


f = open("followers.txt", "w")

for follower in new_followers:
    f.write(follower + "\n")
f.close()