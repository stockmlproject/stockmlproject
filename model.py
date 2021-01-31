import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import tkinter as tk
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import warnings

warnings.filterwarnings('ignore') #We will ignore the different warnings 

usdcad = pd.read_csv('usdcad.csv')
audusd = pd.read_csv('audusd.csv')
gbpusd = pd.read_csv('gbpusd.csv')
eurusd = pd.read_csv('eurusd.csv')
eurchf = pd.read_csv('eurchf.csv')

data = pd.concat([usdcad, audusd, gbpusd, eurusd, eurchf]) 

# The columns are in type float, the data is already cleaned

x = data[['Price', 'Open' ,'Low']].values #This variables will used to predict the price
y = data['High'].values #Variable that we want predict

#Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.18, random_state = 0)

#Train the data
clf = LinearRegression()
clf.fit(x_train, y_train)

print("Accuracy train LinearRegression x,y: {:.3f}".format(clf.score(x_train, y_train)))
print("Accuracy test LinearRegresion x,y: {:.3f}".format(clf.score(x_test, y_test)))


#Make a test prediction
X = [[1.2126, 1.2158, 1.2076]]
predicted = clf.predict(X)
print("Predicted value for último in LR:", predicted.round(4))

#Calculate the difference between realvalues and predicted values.
predictions = [] #Vector for our predictions
realvalues = [] #Vector for real values
it = x_train.shape[0]

for i in range(0, int(it)):
    values = [[x_train[i][0], x_train[i][1], x_train[i][2]]]
    predictions.append(clf.predict(values))
    realvalues.append(y_train[i])
    values = [[]]
    
bad = []
good = []

for i in range(0, len(realvalues)): #For all values in the realvalues array
    sub = realvalues[i] - predictions[i] #Calculate the substract between the real value and our prediction
    abs(sub) #The difference allways is positive
    
    if(sub > 0.003): #If difference > 0.003
        bad.append(sub)
    else:
        good.append(sub)

# Print the length of our arrays
print("The number of well predicted values is: ", len(good))
print("The number of bad predicted values is: ", len(bad))

# Plot this length
labels = 'bad', 'good'
length = np.array([len(bad), len(good)])
plt.pie(length, labels = labels, autopct='%1.1f%%')


# Save model
filename = 'modelo_high.sav'
pickle.dump(clf, open(filename, 'wb'))
