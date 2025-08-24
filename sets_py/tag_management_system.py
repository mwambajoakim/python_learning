#!/usr/bin/python3
suggest_post = __import__('suggest_post').suggest_post

post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "web", "flask"}
post3_tags = {"javascript", "web", "frontend"}

# 1. Find common tags between post1 and post2
print(post1_tags & post2_tags)

# 2. Find all unique tags across all posts
print(post1_tags | post2_tags | post3_tags)

# 3. Find tags that appear in only one post
print(post1_tags ^ post2_tags ^ post3_tags)

# 4. Create a function that suggests related posts based on shared tags
posts = [post1_tags, post2_tags, post3_tags]
shared = suggest_post(posts, "python")
print(shared)
