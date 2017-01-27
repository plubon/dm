from sys import argv
import DataReader
from DecisionTree import DecisionTree

def main():
    if len(argv)>=4:
        if(argv[1] == '-t'):
            training_data = None
            if '-b' in argv:
                training_data =  DataReader.read_training_data_binary(argv[2])
            else:
                training_data = DataReader.read_training_data_multi(argv[2])
            tree = DecisionTree()
            tree.train(training_data[0], training_data[1])
            tree.save(argv[3])
        elif(argv[1] == '-v'):
            if '-b' in argv:
                training_data =  DataReader.read_training_data_binary(argv[2])
            else:
                training_data = DataReader.read_training_data_multi(argv[2])
            tree = DecisionTree()
            tree.load(argv[3])
            results = tree.validate(training_data[0], training_data[1])
            with open(argv[4], 'wb') as outfile:
                outfile.write("\n".join(results))
        elif(argv[1] == '-c'):
            if '-b' in argv:
                training_data =  DataReader.read_training_data_binary(argv[2])
            else:
                training_data = DataReader.read_training_data_multi(argv[2])
            tree = DecisionTree()
            tree.load(argv[3])
            results = tree.classify(input_data)
            with open(argv[4], 'wb') as outfile:
                outfile.write("\n".join(results))
    else:
        print("Incorrect parameters provided")

if __name__ == "__main__":
    main()