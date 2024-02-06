"""
This file demonstrates how to use different machine learning model to analyze boston housing dataset.
"""

import math
import pandas as pd
from sklearn import preprocessing, linear_model, metrics, model_selection, svm, tree

TRAIN_FILE = 'boston_housing/train.csv'
TEST_FILE = 'boston_housing/test.csv'


def main():

	data = pd.read_csv(TRAIN_FILE)
	data.pop('ID')
	data = one_hot_encoding(data, 'chas')

	data_train, data_val = model_selection.train_test_split(data, test_size=0.75)
	labels_train = data_train.pop('medv')
	labels_val = data_val.pop('medv')
	standardlizer = preprocessing.StandardScaler()
	data_train = standardlizer.fit_transform(data_train)
	data_val = standardlizer.fit_transform(data_val)

	##### S1: degree1 linear regression #####
	h = linear_model.LinearRegression()
	classifier = h.fit(data_train, labels_train)
	predictions = classifier.predict(data_train)
	error = metrics.mean_squared_error(predictions, labels_train) ** 0.5
	print('s1 Train error_ basic:', error)

	predictions = classifier.predict(data_val)
	error = metrics.mean_squared_error(predictions, labels_val) ** 0.5
	print('s1 Val error_ basic:', error, '\n')

	# #### S2: degree2 linear regression #####
	# poly_phi = preprocessing.PolynomialFeatures(degree = 2)
	# data_train_poly = poly_phi.fit_transform(data_train)
	# data_val_poly = poly_phi.transform(data_val)
	#
	# classifier_poly = h.fit(data_train_poly, labels_train)
	# predictions = classifier_poly.predict(data_train_poly)
	# error = metrics.mean_squared_error(predictions, labels_train) ** 0.5
	# print('Train error_ poly degree2:', error)
	#
	# predictions = classifier_poly.predict(data_val_poly)
	# error = metrics.mean_squared_error(predictions, labels_val) ** 0.5
	# print('Val error_ poly degree2:', error)

	# ##### S3: svm ((Support Vector Machine) #####
	# h = svm.SVR(gamma=0.5, C=10)
	# svm_classifier = h.fit(data_train, labels_train)
	# predictions = svm_classifier.predict(data_train)
	# error = metrics.mean_squared_error(predictions, labels_train) ** 0.5
	# print('Train error_ svm:', error)
	#
	# predictions =svm_classifier.predict(data_val)
	# error = metrics.mean_squared_error(predictions, labels_val) ** 0.5
	# print('Val error_ svm:', error)

	##### S4: decision tree #####
	d_tree = tree.DecisionTreeRegressor(max_leaf_nodes=12, min_samples_leaf=6)
	d_tree_classifier = d_tree.fit(data_train, labels_train)
	predictions = d_tree_classifier.predict(data_train)
	error = metrics.mean_squared_error(predictions, labels_train) ** 0.5
	print('Train error_d_tree:', error)

	predictions = d_tree_classifier.predict(data_val)
	error = metrics.mean_squared_error(predictions, labels_val) ** 0.5
	print('Val errord_tree:', error)

	# test data outfile
	data_test = pd.read_csv(TEST_FILE)
	test_id = data_test.pop('ID')
	data_test = one_hot_encoding(data_test, 'chas')
	data_test = standardlizer.transform(data_test)
	predictions = d_tree_classifier.predict(data_test)
	out_file(predictions, test_id, 'boston_svm.csv')


def out_file(predictions, test_id, filename):
	print('\n===============================================')
	print(f'Writing predictions to --> {filename}')
	with open(filename, 'w') as out:
		out.write('ID,medv\n')
		for i in range(len(predictions)):
			if i != len(predictions)-1:
				out.write(str(test_id[i]) + ',' + str(predictions[i]) + '\n')
			else:
				out.write(str(test_id[i]) + ',' + str(predictions[i]))
	print('===============================================')


def one_hot_encoding(data, feature):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: DataFrame, remove the feature column and add its one-hot encoding features
	"""
	if feature == 'chas':
		data['chas_0'] = 0
		data.loc[data.chas == 0, 'chas_0'] = 1
		data['chas_1'] = 0
		data.loc[data.chas == 1, 'chas_1'] = 1
		data.pop('chas')
	return data


if __name__ == '__main__':
	main()
