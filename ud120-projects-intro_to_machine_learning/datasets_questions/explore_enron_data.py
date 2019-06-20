#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# Q1
#print len(enron_data)

# Q2
#print len(enron_data.itervalues().next())

# Q3
'''
count = 0
for value in enron_data.itervalues():
    if value["poi"]:
        count += 1
print count
'''

#Q4
#data = np.genfromtxt("../final_project/poi_names.txt")

#Q5
#print enron_data['PRENTICE JAMES']['total_stock_value']

#6
#print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#7
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
