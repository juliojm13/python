def thesaurus(name):
    global names
    name = name.title()
    key = name[0]
    if key in names:
        names[key].append(name)
    else:
        names[key] = []
        names[key].append(name)
    print(names)


names = {}
name = "julio"
print(name.title())
thesaurus("julio")
thesaurus("jaime")
thesaurus("norman")
thesaurus("carlos")
thesaurus("camila")
thesaurus("Cordova")
thesaurus("ana")