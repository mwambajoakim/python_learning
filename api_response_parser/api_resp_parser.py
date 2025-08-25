#!/usr/bin/python3

api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "posts": [{"title": "Hello World", "likes": 15}]},
            {"id": 2, "name": "Bob", "posts": [{"title": "Python Tips", "likes": 32}]}
        ],
        "total_count": 2
    }
}

# 1. Extract all user names
users = api_response["data"]["users"]
user_names = [name["name"] for name in users]
print(user_names)

# 2. Calculate total likes across all posts
users = api_response["data"]["users"]
posts = [post["posts"] for post in users]
total = 0
for post in posts:
    for like in post:
        total += like["likes"]
print(total)

# 3. Find the user with the most likes
users = api_response["data"]["users"]
posts = [post["posts"] for post in users]
for post in posts:
    most_likes = post[0]["likes"]
    for most in post:
        if most_likes < most["likes"]:
            most_likes = most["likes"]
print(most_likes)

# 4. Create a summary dictionary with user stats
users = api_response["data"]["users"]
posts = [post["posts"] for post in users]
user_dict = []
for name in users:
    user_dict.append({keys: values
                      for keys, values in name.items()
                      if keys == "name"})
