from Class.AutismClassifier import AutismClassifier
import pandas as pd
from Class.gui import gui


def create_model():
    autism_clf = AutismClassifier()
    autism_clf.load_dataset()
    autism_clf.train_classifier(model_name="dump/model")



if __name__ == '__main__':
    gui = gui()
    gui.make_window()
    gui.start()


"""
autism = pd.read_csv("Dataset/preprocessed_notna_dataset.csv",index_col=0)

x = autism.drop(axis=1,labels="Class/ASD")
y = autism['Class/ASD']


autism_clf = AutismClassifier()



x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.99)
print("Train size:",x_train.shape[0])
print("Test size:",x_test.shape[0])
print(x_test)


autism_clf.train_classifier(x_train,y_train,"test_model")

x_test_file = open("x_test","wb")
pickle.dump(x_test,x_test_file)

y_test_file = open("y_test","wb")
pickle.dump(y_test,y_test_file)

print(autism_clf.classify_tuples(tuples= x_test.iloc[[0]]))
print(y_test.iloc[[0]])
"""
