import pandas
import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import datetime
from sklearn import linear_model

data_covid = 'owid-covid-data-210616.csv'


class LinearRegression:
    def __init__(self):
        self.data_case = np.array([[]]).T
        self.data_death = np.array([[]]).T
        self.date = np.array([[]]).T
        self.days_detail = np.array([[]]).T

        self.data_case2 = np.array([[]]).T
        self.data_death2 = np.array([[]]).T
        self.date2 = np.array([[]]).T
        self.days_detail2 = np.array([[]]).T

    # NEW INITDATA FUNCTION
    def init_data(self, country, country2=None):
        count = 0
        count2 = 0
        result = pandas.read_csv(data_covid)
        new_case = result[['new_cases', 'new_deaths', 'location', 'date']]
        case = new_case[new_case.location == country]
        for i in case.values:
            if i[0] != 0.0:
                if i[1] != 0.0:
                    self.data_case = np.append(self.data_case, i[0])
                    self.data_case = np.array([self.data_case]).T
                    self.data_case = np.nan_to_num(self.data_case)

                    self.data_death = np.append(self.data_death, i[1])
                    self.data_death = np.array([self.data_death]).T
                    self.data_death = np.nan_to_num(self.data_death)

                    count += 1
                    self.date = np.append(self.date, count)
                    self.date = np.array([self.date]).T

                    self.days_detail = np.append(self.days_detail, i[3])
                    self.days_detail = np.array([self.days_detail]).T

        if country2 is not None:
            case = new_case[new_case.location == country2]
            for i in case.values:
                if i[0] != 0.0:
                    if i[1] != 0.0:
                        self.data_case2 = np.append(self.data_case2, i[0])
                        self.data_case2 = np.array([self.data_case2]).T
                        self.data_case2 = np.nan_to_num(self.data_case2)

                        self.data_death2 = np.append(self.data_death2, i[1])
                        self.data_death2 = np.array([self.data_death2]).T
                        self.data_death2 = np.nan_to_num(self.data_death2)

                        count2 += 1

                        self.date2 = np.append(self.date2, count2)
                        self.date2 = np.array([self.date2]).T

                        self.days_detail2 = np.append(self.days_detail2, i[3])
                        self.days_detail2 = np.array([self.days_detail2]).T

    @staticmethod
    def predict_country(data_x, data_y, count, arr_compare):
        X = data_x[count: count + 10]
        y = data_y[count: count + 10]

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

    def compare(self, title, countryA, countryB):
        count = 0
        if self.date.size > self.date2.size:
            Data2_X = self.date2
            Data3_X = self.date2
            day = self.date2.size
            day_info = self.days_detail2

        else:
            Data2_X = self.date
            Data3_X = self.date
            day = self.date.size
            day_info = self.days_detail

        if 'cases' in title:
            Data2_y = self.data_case
            Data3_y = self.data_case2

        if 'deaths' in title:
            Data2_y = self.data_death
            Data3_y = self.data_death2

        label = []
        arr_compare = []
        arr_compare2 = []
        i = 0

        for i in range(0, day // 10):
            i += 1
            self.predict_country(Data2_X, Data2_y, count, arr_compare)
            self.predict_country(Data3_X, Data3_y, count, arr_compare2)
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
        plt.title('The ' + title + ' comparison between ' +
                  countryA + ' and ' + countryB, fontsize=20)
        plt.xticks(x, label, fontsize=7, rotation="75")
        plt.yticks(fontsize=10)
        plt.xlabel('Stages', fontsize=10)
        plt.ylabel('The ' + title, fontsize=10)
        plt.legend(loc='best', fontsize=10)

        plt.bar_label(rects1, padding=3, fontsize=10)
        plt.bar_label(rects2, padding=3, fontsize=10)

        plt.tight_layout()

        plt.show()

    def init_continent(self, continent):
        count = 0
        result = pandas.read_csv(data_covid)
        new_case = result[['new_cases', 'new_deaths', 'continent', 'date']]
        new_case = new_case[new_case.continent == continent]
        new_case = new_case.groupby('date').sum()
        for i in new_case.values:
            if i[0] != 0.0:
                if i[1] != 0.0:
                    self.data_case = np.append(self.data_case, i[0])
                    self.data_case = np.array([self.data_case]).T
                    self.data_case = np.nan_to_num(self.data_case)

                    self.data_death = np.append(self.data_death, i[1])
                    self.data_death = np.array([self.data_death]).T
                    self.data_death = np.nan_to_num(self.data_death)

                    count += 1
                    self.date = np.append(self.date, count)
                    self.date = np.array([self.date]).T

    @staticmethod
    def array_(X, a):
        X5 = np.array([[]]).T
        for x1 in X:
            X5 = np.append(X5, math.pow(x1, a))
            X5 = np.array([X5]).T
        return X5

    def predict(self, title, type='line'):
        count = 0

        Data2_X = self.date
        if 'cases' in title:
            Data2_y = self.data_case

        if 'deaths' in title:
            Data2_y = self.data_death

        arrayX = np.array([[]]).T
        arrayY = np.array([[]]).T
        arrayY_sck = np.array([[]]).T

        plt.figure(figsize=(14, 5))
        day = len(self.date)

        for i in range(0, day // 10):
            X = Data2_X[count: count + 10]
            y = Data2_y[count: count + 10]

            # Building Xbar
            if type == 'poly':
                X2 = self.array_(X, 2)

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
                 Data2_y[:(day // 10) * 10], 'ro', label=title)
        # draw line
        plt.plot(arrayX, arrayY, color='blue', linewidth=2, label='Line predict')

        # Scikit-learn linear model LR
        plt.plot(arrayX, arrayY_sck.T, color='black',
                 linewidth=2, label='Line SCK')

        plt.legend(loc='best')
        plt.title(title + ' scikit-learn predict')
        plt.xlabel('Days')
        plt.ylabel('Total ' + title)
        plt.show()

    def clear_data(self):
        self.date = self.data_case = self.data_death = self.date2 = self.data_case2 = self.data_death2 = np.array([
                                                                                    []]).T
