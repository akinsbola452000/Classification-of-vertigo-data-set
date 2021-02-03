# Classification-of-vertigo-data-set

The problem deals with categorigal data: an underlying assumption is that each data item can be assigned into a certain category. 
The goal is to be able to deduce, by computational means,  the category of previously unknown data items. 
We will use real data about medical conditions related to vertigo (a disorder of the balance system). 
Each data item corresponds to a single patient and consists of several attributes (sometimes called features). 
The attributes convey information about what kind of symptoms etc. the patients have experienced. 
The goal is to be able to deduce the patient's condition (= classify, or actually diagnose, the patient) based on the symptoms.

The training data
You may download the file vertigo_train.txt, which contains training data about vertigo patients. 
Each row of the file describes both the correct classification and five attribute values for one data item (= patient). 
The values are separated from each other by white space (tab values). Therefore each row has a total of six values. The first line of the file is shown below.
1 4 1 1 5 0
The first line describes a data item whose correct class is 1 and whose five attributes (describing symptoms) have values 4, 1, 1, 5 and 0. 
It is typical that all data is transformed into numeric form (to better enable e.g. statistical analysis of the values). 
For example in this case the class 1 really means a condition called vestibular schwannoma. Each attribute gives,
again in numeric form, information about the level or variation of some symptom.

Test data for prediction
The file vertigo_predict.txt contains test data about vertigo patients. This data is otherwise similar to the training data but now the first value, the correct classification, 
is missing. Therefore each row contains only five values. These five attribiute values are given in the same order as they appear in the training set.
In addition the file vertigo_answers.txt contains the true classifications for each patient in the test set. Each row contains only one value: 
the classification of the corresponding test patient. Here "correspondence" means the row index. Row i of the answers file corresponds to row i of the test file. 
The task

Now to the actual task of this question.
We test how accurately the following two different methods are able to classify the data items of the test set when the given training set has been available to them.
•	A neural network variant called perceptron. 
o	The scikit-learn library offers an easy-to-use implementation of this method.
