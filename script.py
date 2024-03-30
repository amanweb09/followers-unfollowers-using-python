import json

followers = []
following = []

with open('followers_1.json') as file:
    followers = json.load(file)

with open("following.json") as file:
    following = json.load(file)

following_list = [username["string_list_data"][0]["value"] for username in following["relationships_following"]]


followers_list = [username["string_list_data"][0]["value"] for username in followers]


unfollowers = [u for u in following_list if u not in followers_list]

for uf in unfollowers:
    print("-> ", uf, "\n")