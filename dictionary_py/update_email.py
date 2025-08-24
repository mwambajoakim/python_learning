#!/usr/bin/python3

def update_email(users=[], name="", new_email=""):
    """Function that updates the email of a user.

       Args:
            users: A list of user profiles.
            name: Name of the user.
            new_email: The new email to update with.
       Return:
              None
              prints the user with updated email.
    """
    for i in range(len(users)):
        if users[i]["name"] == name:
            users[i].pop("email")
            users[i]["email"] = new_email
            print(users[i])
