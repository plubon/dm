import pickle
from sklearn import tree

class DecisionTree:

	def __init__(self):
		self.classifier = tree.DecisionTreeClassifier()

	def train(self, X, Y):
		self.classifier.fit(X, Y)

	def classify(self, X):
		results = self.classifier.predict(X)

	def validate(self, X, Y):
		results = self.classifier.predict(X)
		correct = 0
		for index in range(len(results)):
			if results[index] == Y[index]:
				correct += 1
		print('Accuracy: '+str(float(correct)/float(len(results))))
		return results

	def save(self, path):
		pickle.dump(self.classifier, open(path, 'wb'))

	def load(self, path):
		self.classifier = pickle.load(open(path, 'rb'))