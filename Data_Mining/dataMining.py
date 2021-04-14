import pandas as pd
import graphviz
import pickle
from sklearn import tree
from sklearn.datasets import load_iris

fields = ['Region', 'Episode week', 'Gender', 'Age group', 'Occupation']
fields2 = ['Died'] # Survived = 0, Died = 1

def read_data():
    print("Reading Data . . .")
    df = pd.read_csv('Data_Mining/dataMiningData.csv', skipinitialspace=True, usecols=fields)
    df2 = pd.read_csv('Data_Mining/dataMiningData.csv', skipinitialspace=True, usecols=fields2)

    # User list comprehension to create a list of lists from Dataframe rows
    data = [list(row) for row in df.values]
    outcome = [list(row) for row in df2.values]

    print("Creating Classification Tree. . .")
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(data, outcome)

    # Save the classifer so that it can be reused
    pickle.dump(clf, open("classifier.pickle", "wb"))
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