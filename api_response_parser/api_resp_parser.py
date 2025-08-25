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
user_names = []
for name in users:
    print(name["name"])
   # user_names.append(name["name"])

# 2. Calculate total likes across all posts
users = api_response["data"]["users"]
posts = [post["post"] for post in posts]
print(posts)
