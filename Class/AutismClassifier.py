import pickle

import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import ttest_rel
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, f1_score, make_scorer
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.model_selection import KFold
from statistics import mean
from sklearn.model_selection import train_test_split


class AutismClassifier:
    file_name = "/home/salvo/PycharmProjects/DMML_project/Dataset/preprocessed_notna_dataset.csv"
    x = None
    y = None
    clf = AdaBoostClassifier(base_estimator=BernoulliNB(alpha=0))  # no smoothing



    def load_dataset(self, **kwargs):
        if len(kwargs) == 0:
            df = pd.read_csv(self.file_name,index_col=0)
            self.x = df.drop(axis=1, labels='Class/ASD')
            self.y = df['Class/ASD']
        elif len(kwargs) == 1 and isinstance(kwargs["file_name"], str):
            df = pd.read_csv(kwargs["file_name"])
            self.x = df.drop(axis=1, labels='Class/ASD')
            self.y = df['Class/ASD']

    def get_file_name(self):
        return self.file_name

    def get_data(self):
        return self.x

    def get_label(self):
        return self.y

    def train_classifier(self, **kwargs):
        if len(kwargs) == 1 and isinstance(kwargs["model_name"], str):
            file = open(kwargs["model_name"], "wb")
            self.clf.fit(self.x, self.y)
            pickle.dump(self.clf, file)
        elif len(kwargs) == 3:
            file = open(kwargs["model_name"], "wb")
            self.clf.fit(kwargs["x_train"], kwargs["y_train"])
            pickle.dump(self.clf, file)

    def load_model(self, file_name):
        file = open(file_name, "rb")
        self.clf = pickle.load(file)

    def classify_tuples(self, tuples):
        predicted_labels = self.clf.predict(tuples)
        return predicted_labels


"""
    def train_classifier(self,model_name):
                file = open(model_name,"wb")
        self.clf.fit(self.x,self.y)
        pickle.dump(self.clf,file)

    def train_classifier(self,x_train,y_train,model_name):
        file = open(model_name, "wb")
        self.clf.fit(x_train, y_train)
        pickle.dump(self.clf, file)
"""
"""
    def __init__(self, file_name):
        self.filename = file_name
        self.load_dataset(self)
"""