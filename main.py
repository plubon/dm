from sys import argv
import DataReader
import time
import pickle
from sklearn import tree
import pydotplus

def main():
    start_time = time.time()
    training_data = DataReader.read_training_data(argv[1])
    print("Loaded data")
    print(training_data[1].count(1))
    print(training_data[1].count(0))
    clf = tree.DecisionTreeClassifier()
    clf.fit(training_data[0], training_data[1])
    pickle.dump(clf, open('tree-multi.pck', 'wb'))
    print("--- %s seconds ---" % (time.time() - start_time))

def validate():
    print("Validating")
    #validation_data = DataReader.read_training_data(argv[2])
    #print(validation_data[1].count(0))
    #print(validation_data[1].count(1))
    clf = pickle.load(open('tree.pck', 'r'))
    #results = clf.predict(validation_data[0])
    #correct = 0
    #for index in range(len(results)):
        #if results[index] == validation_data[1][index]:
            #correct += 1
    #print(float(correct)/float(len(results)))
    dot_data = tree.export_graphviz(clf, out_file=None, feature_names=DataReader.attrs, class_names=['normal', 'attack'], filled=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png("binary.png")



if __name__ == "__main__":
    validate()