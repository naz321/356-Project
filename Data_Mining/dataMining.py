import pandas as pd
import graphviz
import pickle
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.utils import shuffle
import numpy as np


fields = ['Region', 'Episode week', 'Gender', 'Age group', 'Occupation']
fields2 = ['Died'] # Survived = 0, Died = 1
SEED = 2

def read_data():
    print("Reading Data . . .")
    df = pd.read_csv('Data_Mining/dataMiningData.csv', skipinitialspace=True, usecols=fields)
    df2 = pd.read_csv('Data_Mining/dataMiningData.csv', skipinitialspace=True, usecols=fields2)

    # User list comprehension to create a list of lists from Dataframe rows
    data = np.array([list(row) for row in df.values])
    outcome = np.array([list(row) for row in df2.values])

    print("Creating Classification Tree. . .")
    kf = KFold(n_splits=10, random_state=SEED, shuffle=True)
    max_accuracy = 0
    best_clf = None
    
    for train_index, test_index in kf.split(data):
        X_train, X_test = data[train_index], data[test_index]
        y_train, y_test = outcome[train_index], outcome[test_index]

        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X_train, y_train)

        accuracy = clf.score(X_test, y_test)
        # print('New accuracy: ', accuracy)

        if accuracy > max_accuracy:            
            best_clf = clf 
            max_accuracy = accuracy

    # print('Highest Value Accuracy: ', max_accuracy)
    # Save the classifer so that it can be reused
    pickle.dump(best_clf, open("classifier.pickle", "wb"))
    print("Data Mining Done!")

def data_mine(input_data):    
    clf = pickle.load(open("classifier.pickle", "rb"))
    x = []
    x.append(input_data)
    rate = clf.predict_proba(x)

    surviveRate = (rate[:,0])[0] * 100
    deathRate = (rate[:,1])[0] * 100

    print('Given the following scenario, you have a %.2f%% chance of surviving and a %.2f%% of dying.' % (surviveRate, deathRate)) 

def create_decision_tree_output():
    clf = pickle.load(open("classifier.pickle", "rb"))

    # Create Decision Tree Diagram
    dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=fields,  
                         class_names=['Survived', 'Died'],
                         filled=True, rounded=True,  
                         special_characters=True)  
    graph = graphviz.Source(dot_data) 
    graph.render("COVID_19_Decision_Tree")