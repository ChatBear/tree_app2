from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
import pickle 


X = pd.read_csv('data.csv', header=0, names=['hmm', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
y = pd.read_csv('target.csv')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
X_train = X_train[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y_train = y_train[['target']]

clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)


pickle.dump(clf, open('model_tree.sav', 'wb'))
print('Model saved')