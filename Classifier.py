import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import ttest_rel
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, f1_score, make_scorer
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import KFold
from statistics import mean
from sklearn.model_selection import train_test_split


class Classifier:
    filename = "//preprocessed_dataset.csv"
    x = None
    y = None


    def _init_(self):
        pass

    def _init(self, filename):
        self.filename = filename

    def load_dataset(self):
        df = pd.read_csv(self.filename)
        self.x = df.drop(axis=1, labels='Class/ASD')
        self.y = df['Class/ASD']

    def get_data(self):
        return self.x

    def get_label(self):
        return self.y


    def evaluate_classifier(self,clf,x,y):
        estimators = [('fs',SelectKBest()),('clf',clf)]
        pipe_fs = Pipeline(estimators)

        estimators_nofs = [('clf',clf)]
        pipe_nofs = Pipeline(estimators_nofs)

        kf = KFold(n_splits=10)

        results_fs = cross_validate(pipe_fs,
                             x,
                             y,
                             scoring = {'fscore': make_scorer(f1_score),
                                        'accuracy': make_scorer(accuracy_score)},
                             return_estimator = True,
                             cv = kf,
                             n_jobs = -1)
        results_nofs = cross_validate(pipe_nofs,
                             x,
                             y,
                             scoring = {'fscore': make_scorer(f1_score),
                                        'accuracy': make_scorer(accuracy_score)},
                             return_estimator = True,
                             cv = kf,
                             n_jobs = -1)
        metrics = pd.DataFrame({'fsel': results_fs['test_fscore'],
                            'nofsel': results_nofs['test_fscore']})

        ax = metrics.boxplot(figsize = (3,3))
        ax.set_ylabel('f-score')
        plt.show()
        print("Mean feature selection:",mean(metrics['fsel']))
        print("Mean No feature selection",mean(metrics['nofsel']))
        print(ttest_rel(metrics['fsel'],metrics['nofsel']))

    def train_classifier(self,clf):








