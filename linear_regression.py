from __future__ import division, print_function, unicode_literals
import pandas
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import linear_model


data_case = np.array([[]]).T
data_death = np.array([[]]).T
date = np.array([[]]).T

def initData(country):
    global date, data_case, data_death, drawX, drawY
    count = 0
    result = pandas.read_csv('owid-covid-data.csv')
    newCase = result[['new_cases', 'new_deaths', 'location', 'date']]
    newCase = newCase[newCase.location == country]
    for i in newCase.values:
        if i[0] != 0.0:
            if i[1] != 0.0:
                data_case = np.append(data_case, i[0])
                data_case = np.array([data_case]).T

                data_death = np.append(data_death, i[1])
                data_death = np.array([data_death]).T

                count += 1
                date = np.append(date, count)
                date = np.array([date]).T


# def array_(X, a):
#     X5 = np.array([[]]).T
#     for x1 in X:
#         X5 = np.append(X5, math.pow(x1, a))
#         X5 = np.array([X5]).T
#     return X5


# def predict(date, case, a, type='line'):
#     count = 0

#     Data2_X = date
#     Data2_y = case

#     arrayX = np.array([[]]).T
#     arrayY = np.array([[]]).T
#     arrayY_sck = np.array([[]]).T

#     plt.figure(figsize=(14, 5))
#     day = len(date)

#     for i in range(0, day // 10):
#         X = Data2_X[count: count + 10]
#         y = Data2_y[count: count + 10]

#         # Building Xbar
#         if type == 'poly':
#             X2 = array_(X, 2)

#         one = np.ones((X.shape[0], 1))
#         Xbar = np.concatenate((one, X), axis=1)
#         if type == 'poly':
#             Xbar = np.concatenate((Xbar, X2), axis=1)

#         # Calculating weights of the fitting line 
#         A = np.dot(Xbar.T, Xbar)
#         b = np.dot(Xbar.T, y)
#         w = np.dot(np.linalg.pinv(A), b)

#         # Preparing the fitting line 
#         w_0 = w[0][0]
#         w_1 = w[1][0]
#         if type == 'poly':
#             w_2 = w[2][0]

#         x0 = np.linspace(Data2_X[count], Data2_X[count + 9], 10)
#         if type == 'poly':
#             y0 = w_0 + w_1 * x0 + w_2 * x0 * x0
#         else:
#             y0 = w_0 + w_1 * x0

#         for f in x0:
#             arrayX = np.append(arrayX, f)
#             arrayX = np.array([arrayX]).T
#         for f in y0:
#             arrayY = np.append(arrayY, f)
#             arrayY = np.array([arrayY]).T

#         # Scikit learn
#         regr = linear_model.LinearRegression()
#         regr.fit(X, y)
#         arrayY_pred = regr.predict(X)

#         for f in arrayY_pred:
#             arrayY_sck = np.append(arrayY_sck, f)
#             arrayY_sck = np.array(arrayY_sck).T

#         count += 10
#     # Drawing data
#     plt.plot(Data2_X[:(day // 10) * 10], Data2_y[:(day // 10) * 10], 'ro', label=a)
#     # draw line
#     plt.plot(arrayX, arrayY, color='blue', linewidth=2, label='Line predict')

#     # Scikit-learn linear model LR
#     plt.plot(arrayX, arrayY_sck.T, color='black', linewidth=2, label='Line SCK')
#     plt.legend(loc='best')
#     plt.title(a + ' scikit-learn predict')
#     plt.show()

# In[2]:


# Russia, United States, Australia, China, ...
country = 'China'
initData(country)

print(date)

# In[3]:


# line predict new cases
# a = predict(date,data_case, 'New cases', 'poly')
# line predic new death
# b = predict(date, data_death, 'New deaths', 'poly')