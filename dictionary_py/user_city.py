#!/usr/bin/python3

def user_city(users=[], city=""):
    """Function that searches user by city.

       Args:
            users: A list of user profiles.
            city: The name of the city.

       Return:
              None.
              Prints the user profiles of the city name.
    """
    for i in range(len(users)):
        if users[i]["city"] == city:
            print(users[i])
