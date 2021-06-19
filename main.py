from __future__ import division, print_function, unicode_literals
import eel
import pandas
import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import datetime
from sklearn import linear_model
import json

data_case = np.array([[]]).T
data_death = np.array([[]]).T
date = np.array([[]]).T
days_detail = np.array([[]]).T

data_case2 = np.array([[]]).T
data_death2 = np.array([[]]).T
date2 = np.array([[]]).T
days_detail2 = np.array([[]]).T



# NEW INITDATA FUNCTION
def initData(country, country2=None):
    global date, date2, data_case2, data_death2, data_case, data_death, days_detail, days_detail2
    count = 0
    count2 = 0
    result = pandas.read_csv('owid-covid-data-210616.csv')
    newCase = result[['new_cases', 'new_deaths', 'location', 'date']]
    case = newCase[newCase.location == country]
    for i in case.values:
        if i[0] != 0.0:
            if i[1] != 0.0:
                data_case = np.append(data_case, i[0])
                data_case = np.array([data_case]).T
                data_case = np.nan_to_num(data_case)

                data_death = np.append(data_death, i[1])
                data_death = np.array([data_death]).T
                data_death = np.nan_to_num(data_death)

                count += 1
                date = np.append(date, count)
                date = np.array([date]).T

                days_detail = np.append(days_detail, i[3])
                days_detail = np.array([days_detail]).T

    if country2 != None:
        case = newCase[newCase.location == country2]
        for i in case.values:
            if i[0] != 0.0:
                if i[1] != 0.0:
                    data_case2 = np.append(data_case2, i[0])
                    data_case2 = np.array([data_case2]).T
                    data_case2 = np.nan_to_num(data_case2)

                    data_death2 = np.append(data_death2, i[1])
                    data_death2 = np.array([data_death2]).T
                    data_death2 = np.nan_to_num(data_death2)

                    count2 += 1

                    date2 = np.append(date2, count2)
                    date2 = np.array([date2]).T

                    days_detail2 = np.append(days_detail2, i[3])
                    days_detail2 = np.array([days_detail2]).T

def predict_country(Data2_X, Data2_y, count, arr_compare):

    X = Data2_X[count: count + 10]
    y = Data2_y[count: count + 10]

    day = X[9]

    # Building Xbar
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)

    # Calculating weights of the fitting line
    A = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, y)
    w = np.dot(np.linalg.pinv(A), b)

    # Preparing the fitting line
    w_0 = w[0][0]
    w_1 = w[1][0]

    y0 = w_0 + w_1 * day
    arr_compare.append(y0[0])


#     type: line -> đường thẳng
#           poly -> đường cong -> độ chính xác cao hơn
#     date: tổng số ngày lấy được từ dữ liệu gốc
#     case: muốn dự đoán số ca chết or số ca mắc mới
def compare(case1, case2, name, countryA, countryB):
    global date, date2, days_detail, days_detail2
    count = 0
    if date.size > date2.size:
        Data2_X = date2
        Data3_X = date2
        day = date2.size
        day_info = days_detail2

    else:
        Data2_X = date
        Data3_X = date
        day = date.size
        day_info = days_detail

    Data2_y = case1
    Data3_y = case2

    label = []
    arr_compare = []
    arr_compare2 = []
    i = 0

    for i in range(0, day // 10):
        i += 1
        predict_country(Data2_X, Data2_y, count, arr_compare)
        predict_country(Data3_X, Data3_y, count, arr_compare2)
        label.append(datetime.strptime(str(day_info[count][0]), "%Y-%m-%d")
        .strftime("%d/%m/%Y") + ' - ' + datetime.strptime(str(day_info[count + 9][0]), "%Y-%m-%d")
        .strftime("%d/%m/%Y"))
        # label.append(str(day_info[count][0]) + " to " + str(day_info[count + 9][0]))
        count += 10

    x = np.arange(len(label))  # the label locations
    width = 0.35  # the width of the bars

    plt.figure(figsize=(18, 6))

    rects1 = plt.bar(x - width/2, arr_compare, width, label=countryA)
    rects2 = plt.bar(x + width/2, arr_compare2, width, label=countryB)
    plt.title('The ' + name + ' comparison between ' +
              countryA + ' and ' + countryB, fontsize=20)
    plt.xticks(x, label, fontsize=7, rotation="75")
    plt.yticks(fontsize=10)
    plt.xlabel('Stages', fontsize=10)
    plt.ylabel('The ' + name, fontsize=10)
    plt.legend(loc='best', fontsize=10)

    plt.bar_label(rects1, padding=3, fontsize=10)
    plt.bar_label(rects2, padding=3, fontsize=10)

    plt.tight_layout()

    plt.show()


def initContinent(continent):
    global date, data_case, data_death
    count = 0
    result = pandas.read_csv('owid-covid-data-210616.csv')
    newCase = result[['new_cases', 'new_deaths', 'continent', 'date']]
    newCase = newCase[newCase.continent == continent]
    newCase = newCase.groupby('date').sum()
    for i in newCase.values:
        if i[0] != 0.0:
            if i[1] != 0.0:
                data_case = np.append(data_case, i[0])
                data_case = np.array([data_case]).T
                data_case = np.nan_to_num(data_case)

                data_death = np.append(data_death, i[1])
                data_death = np.array([data_death]).T
                data_death = np.nan_to_num(data_death)

                count += 1
                date = np.append(date, count)
                date = np.array([date]).T


def array_(X, a):
    X5 = np.array([[]]).T
    for x1 in X:
        X5 = np.append(X5, math.pow(x1, a))
        X5 = np.array([X5]).T
    return X5


def predict(date, case, a, type='line'):
    count = 0

    Data2_X = date
    Data2_y = case

    arrayX = np.array([[]]).T
    arrayY = np.array([[]]).T
    arrayY_sck = np.array([[]]).T

    plt.figure(figsize=(14, 5))
    day = len(date)

    for i in range(0, day // 10):
        X = Data2_X[count: count + 10]
        y = Data2_y[count: count + 10]

        # Building Xbar
        if type == 'poly':
            X2 = array_(X, 2)

        one = np.ones((X.shape[0], 1))
        Xbar = np.concatenate((one, X), axis=1)
        if type == 'poly':
            Xbar = np.concatenate((Xbar, X2), axis=1)

        # Calculating weights of the fitting line
        A = np.dot(Xbar.T, Xbar)
        b = np.dot(Xbar.T, y)
        w = np.dot(np.linalg.pinv(A), b)

        # Preparing the fitting line
        w_0 = w[0][0]
        w_1 = w[1][0]
        if type == 'poly':
            w_2 = w[2][0]

        x0 = np.linspace(Data2_X[count], Data2_X[count + 9], 10)
        if type == 'poly':
            y0 = w_0 + w_1 * x0 + w_2 * x0 * x0
        else:
            y0 = w_0 + w_1 * x0

        for f in x0:
            arrayX = np.append(arrayX, f)
            arrayX = np.array([arrayX]).T
        for f in y0:
            arrayY = np.append(arrayY, f)
            arrayY = np.array([arrayY]).T

        # Scikit learn
        regr = linear_model.LinearRegression()
        regr.fit(X, y)
        arrayY_pred = regr.predict(X)

        for f in arrayY_pred:
            arrayY_sck = np.append(arrayY_sck, f)
            arrayY_sck = np.array(arrayY_sck).T

        count += 10
    # Drawing data
    plt.plot(Data2_X[:(day // 10) * 10],
             Data2_y[:(day // 10) * 10], 'ro', label=a)
    # draw line
    plt.plot(arrayX, arrayY, color='blue', linewidth=2, label='Line predict')

    # Scikit-learn linear model LR
    plt.plot(arrayX, arrayY_sck.T, color='black',
             linewidth=2, label='Line SCK')

    plt.legend(loc='best')
    plt.title(a + ' scikit-learn predict')
    plt.xlabel('Days')
    plt.ylabel('Total ' + a)
    plt.show()


def clearData():
    global date, data_case, data_death, date2, data_case2, data_death2
    date = data_case = data_death = date2 = data_case2 = data_death2 = np.array([
                                                                                []]).T


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
    initData(country)
    predict(date, data_case, 'New case of ' + country, 'poly')
    predict(date, data_death, 'New death of ' + country, 'poly')
    clearData()


@eel.expose
def contGroup(continent):
    initContinent(continent)
    predict(date, data_case, 'New case of ' + continent, 'poly')
    predict(date, data_death, 'New death of ' + continent, 'poly')
    clearData()


@eel.expose
def locaComparison(location1, location2):
    initData(location1, location2)
    compare(data_case, data_case2, 'cases', location1, location2)
    compare(data_death, data_death2, 'deaths', location1, location2)
    clearData()


eel.init("www")
eel.start("index.html")
