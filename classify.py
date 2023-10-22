from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier, DistanceMetric
from sklearn.metrics import accuracy_score

##### reading training, testing and gold data ####
### testing changes2
import nltk


classes = []
training_data = []

with open('vertigo_train.txt', "r") as train_data:

    for entry in train_data:
        entries = entry.split()
        attribute = [int(entries[1]), int(entries[2]), int(entries[3]), int(entries[4]), int(entries[5])]

        classes.append(int(entries[0]))

        training_data.append(attribute)

testing_data = []

with open('vertigo_predict.txt', 'r') as f_handler:

    for entry in f_handler:
        entries = entry.split()
        attribute = [int(entries[0]), int(entries[1]), int(entries[2]), int(entries[3]), int(entries[4])]

        testing_data.append(attribute)

gold_data = []

with open('vertigo_answers.txt', 'r') as f_handler:

    for entry in f_handler:
        entries = entry.split()
        gold_data.append(int(entries[0]))


def perceptron(training_data, classes, testing_data, gold_data):
    """

    :param training_data: contains the training data
    :param classes: contains the labels of the training data
    :param testing_data: the testing set
    :param gold_data: the gold labels of the testing set
    """
    p = Perceptron()
    p.fit(training_data, classes)
    training_results = p.predict(testing_data)
    print(accuracy_score(gold_data, training_results))


def k_nn(training_data, classes, testing_data, gold_data):
    """

    :param training_data: contains the training data
    :param classes: contains the labels of the training data
    :param testing_data: the testing set
    :param gold_data: the gold labels of the testing set
    """

    neigh = KNeighborsClassifier(n_neighbors=5, metric='manhattan')
    neigh.fit(training_data, classes)
    training_results = neigh.predict(testing_data)

    print(accuracy_score(gold_data, training_results))


perceptron(training_data, classes, testing_data, gold_data)
k_nn(training_data, classes, testing_data, gold_data)

