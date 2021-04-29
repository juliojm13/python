import json
import sys

with open('users.csv', 'r', encoding='utf-8') as f_u, open('hobby.csv', 'r', encoding='utf-8') as f_h:
    users = [el.split('\n') for el in f_u.readlines()]
    print(users)
    print(len(users))
    hobby = [el.split('\n') for el in f_h.readlines()]
    print(hobby)
    print(len(hobby))
    people = {}
    if len(hobby) > len(users):
        sys.exit(1)

    else:
        for el in users:
            if users.index(el) < len(hobby):
                user = el[0]
                print(user)
                hobb = hobby[users.index(el)][0]
                print(hobb)
                people[user] = hobb
            else:
                user = el[0]
                people[user] = None
        print(people)
    with open('people.json', 'w', encoding='utf-8') as f:
        json.dump(people, f)
    with open('people.json', 'r', encoding='utf-8') as f:
        people = json.load(f)
        print(people)
