import scipy,numpy, pandas,matplotlib, sklearn
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas .read_csv('./iris.data',names=names)
print(dataset .groupby('class').size())
dataset.hist()
plt.show()

# Split-aut validation dataset

array=dataset.values
X=array[:,0:4]
Y=array[:,4]
validation_size=0.20
seed=7
scoring='accuracy'
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X,Y,test_size=validation_size,random_state=seed)
# Spot Check Algorithms
models=[]
models.append(('LR',LogisticRegression(solver='liblinear',multi_class='auto')))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('CART',DecisionTreeClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results=[]
names=[]
for name, model in models:
    kfold=model_selection.KFold (n_splits=10, random_state=seed)
    cv_results=model_selection.cross_val_score(model,X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg="%s: %f (%f)" % (name, cv_results.mean(),cv_results.std())
    print(msg)
knn =KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions=knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))