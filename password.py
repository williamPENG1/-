import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
#def data_process_x(number_list):
  #  letter2number = {'Q': 0, 'X': 1, 'Y': 2, 'Z': 3}
 #   list = []
  #  for i in range(len(number_list)):
   #     for j in range(60):
    #        for letter, number2 in letter2number.items():
       #             if number_list[i][j] == letter:
      #                  list.append(number2)
  #  return list

#def data_process_y(numberlist):
 #   list = []
  #  letter2number = {'A':1,'B':2,'C':3}
  #  for i in numberlist:
     #   for letter,number in letter2number.items():
     #       if i == letter:
      #          list.append(number)
  #  return list
data = pd.read_csv('C:\\Users\\Administrator\\Desktop\\trainDataafter.csv')
data2= pd.read_excel('C:\\Users\\Administrator\\Desktop\\Students2.xls')
print (data2.head())
data_x = data.drop(['class'],axis = 1)
data_y = data['class']
data_x_train,data_x_test,data_y_train,data_y_test = train_test_split(data_x,data_y,test_size = 0.3,random_state = 123)
mode = GradientBoostingClassifier(learning_rate=0.095)
print (mode)
mode.fit(data_x_train,data_y_train)
answer = mode.predict(data2)
df = pd.DataFrame(answer)
df.to_csv("C:\\Users\\Administrator\\Desktop\\answer.csv")
#print (np.mean(answer == data_y_test))


