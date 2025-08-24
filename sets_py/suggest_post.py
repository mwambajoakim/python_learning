#!/usr/bin/python3

def suggest_post(posts=[], tag=""):
    """Function that suggests posts based
    on related tags.

      Args:
           tag: Tags in the post.

    Return:
           The related posts.
    """
    shared_tags = []
    for post in posts:
        for tg in post:
            if tg == tag:
                shared_tags.append(post)
    return shared_tags
