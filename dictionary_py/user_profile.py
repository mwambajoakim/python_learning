#!/usr/bin/python3
user_city = __import__('user_city').user_city
update_email = __import__('update_email').update_email

users = [
    {
        "name": "Joe Dean",
        "email": "jd@email.com",
        "age": 27,
        "city":"Maputo"
    },
    {
        "name": "Jane Mern",
        "email": "jm@email.com",
        "age": 24,
        "city":"Tripoli"
    },
    {
        "name": "Kim Lord",
        "email": "km@email.com",
        "age": 34,
        "city":"Kampala"
    }
]

for i in range(len(users)):
    if users[i]["age"] > 25:
        print(users[i])

print("----------------------------------")
print("----------------------------------")

    
user_city(users, "Maputo")

print("----------------------------------")
print("----------------------------------")

update_email(users, "Joe Dean", "dj@email.com")
