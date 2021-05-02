import json

location = []


def loadLocation():
    f = open('location.json',)
    data = json.load(f)

    for i in data['country']:
        location.append(i['name'])

    # Closing file
    f.close()

loadLocation()
# for i in location:
#     print(i)

def locaExist(loca):
    a = 0
    if loca in location:
        a = 1
    else:
        a = 0
    print(a)
    
locaExist('United States')
# print(locaExist('Xomali'))

# x = ["Moon","Earth","Jupiter"]
# print(x.index("Earth"))

