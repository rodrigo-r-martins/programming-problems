from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, jaccard_score
from sklearn.ensemble import VotingClassifier


# Checking dataset
#dataset = datasets.load_breast_cancer()
# print(dataset)

# Loading dataset
X, y = datasets.load_breast_cancer(return_X_y=True)

# Splitting data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=4)

print(f'Shape of X_train: {X_train.shape}')
print(f'Shape of y_train: {y_train.shape}')


# Creating Logistic Regression
LR = LogisticRegression(solver='liblinear')


# Creating Decision Tree with the best number of depth
best_score_DT = 0.0
for depth in range(1, 10):
    DT = DecisionTreeClassifier(criterion='gini',
                                max_depth=depth,
                                min_samples_leaf=0.2)
    scores = cross_val_score(DT, X_test, y_test, cv=10)
    score = scores.mean()

    if score > best_score_DT:
        best_score_DT = score
        best_DT = DT
        best_depth = depth

DT = best_DT


# Creating KNeighbors Classifier with the best number of neighbors
best_score = 0.0
for k in range(3, 13):
    KNN = KNeighborsClassifier(n_neighbors=k,
                               algorithm='auto')
    scores = cross_val_score(KNN, X_test, y_test, cv=10)
    score = scores.mean()

    if score > best_score:
        best_score = score
        best_KNN = KNN
        best_k = k

KNN = best_KNN


# Creating Support Vector Machine
SVM = SVC(max_iter=1000)


# List of models to iterate over
models = [('Logistic Regression', LR),
          ('KNeighbors', KNN),
          ('Decision Tree', DT),
          ('Support Vector Machine', SVM)]

# for model in models:
#    print(model)


# Dictionary to save results
accuracy_per_model = {}


# Getting accuracy results
for name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy_per_model[name] = round(acc, 3)


print(accuracy_per_model)


# Voting is one of the simplest way of combining the predictions from multiple machine learning algorithms
VC = VotingClassifier(estimators=models, voting='hard')
VC.fit(X_train, y_train)
y_pred = VC.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print('Voting Classifier Accuracy:', round(acc, 3))
