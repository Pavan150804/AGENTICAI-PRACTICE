users_db=[
    {"name":"Alice","salary":20000},
    {"name":"vamsi","salary":30000},
    {"name":"rahul","salary":70000}
]

def fetch_users():
    print("connecting to the db..")

    for user in users_db:
        print(f"fetching{user['name']}")
        yield user
    print("db closed")

def process_user(user):
    print(f"processing {user['name']}")
    return user['salary']*0.1

newuser=[]

for item in fetch_users():
    result = process_user(item)
    newuser.append(result)
print(newuser)
    