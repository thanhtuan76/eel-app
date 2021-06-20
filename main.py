from linear_regression import LinearRegression
import json
import eel

location = []



def loadLocation():
    f = open('location.json',)
    data = json.load(f)

    for i in data['country']:
        location.append(i['name'])

    # Closing file
    f.close()


loadLocation()

code = 0


@eel.expose
def locaExist(loca):
    global code
    if loca in location:
        code = 1
    else:
        code = 0
    eel.checkInput(code)


flag = 0


@eel.expose
def locaExist2(loca1, loca2):
    global code
    if (loca1 in location) and (loca2 in location):
        flag = 1
    else:
        flag = 0
    eel.checkExist(flag)


# MAIN FUNCTION
@eel.expose
def plotGraph(country):
    ln = LinearRegression()
    ln.init_data(country)
    ln.predict('New cases of ' + country, 'poly')
    ln.predict('New deaths of ' + country, 'poly')
    # ln.clear_data()


@eel.expose
def contGroup(continent):
    ln = LinearRegression()
    ln.init_continent(continent)
    ln.predict('New cases of ' + continent, 'poly')
    ln.predict('New deaths of ' + continent, 'poly')
    # ln.clear_data()


@eel.expose
def locaComparison(location1, location2):
    ln = LinearRegression()
    ln.init_data(location1, location2)
    ln.compare('cases', location1, location2)
    ln.compare('deaths', location1, location2)
    # ln.clear_data()


eel.init("www")
eel.start("index.html")
