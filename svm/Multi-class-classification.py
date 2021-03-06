from sklearn import svm

X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y) 
dec = clf.decision_function([[1]])
print(dec.shape[1]) # 6 classes

clf.decision_function_shape = "ovr"
dec = clf.decision_function([[1]])
print(dec.shape[1])
# 4 classes

lin_clf = svm.LinearSVC()
lin_clf.fit(X, Y) 
dec = lin_clf.decision_function([[1]])
print(dec)
print(dec.shape[1])
