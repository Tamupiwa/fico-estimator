import requests
import os
import csv
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class Estimator:
    #values from pretrained model
    int = 759.9175579736204
    coef = -5.40286175
    prime_rate = 5

    def __init__(self):
        path = os.path.realpath(__file__)

    #iterates all the html documents in folder, scrapes each one and combines into one list record
    def all_data(self):
        master_data = []
        directory =  self.path + 'LendingClubLoans/Html'
        for file in os.listdir(directory):
            with open(os.path.join(directory, file)) as page:
                data = scrape(page)
                master_data += data
        return master_data

    ##scrapes the lending club loan market place and scrapes the interest rate and fico score for each loan
    def scrape(self, page):
      data = []
      soup = BeautifulSoup(page, 'html.parser')
      #get the div containing all the loans
      loans = soup.find_all('tbody', class_='yui-dt-data')
      loans = loans[0].find_all('tr')
      for l in loans:
          rate = l.find_all('strong', class_='rate')[0].contents[0]
          fico = l.find_all('div', class_='ficoDisplay')[0].contents[0]
          data.append({'lender': 'lending club', 'rate': rate, 'fico': fico, 'prime_rate':self.prime_rate})

      formated_data = self.format(data)
      return formated_data

    #formats the rates from latin1 and transaltes fico range to mean
    def format(self, data):
        new_data = []
        for d in data:
            new_d = {'lender': 'lending club', 'prime_rate': self.prime_rate}
            #remove latin1 encoding
            new_rate = d['rate'].strip(u' \xa0')
            #remove the percentage sign
            new_rate = new_rate.strip('%')
            new_rate = str(new_rate)
            new_d['rate'] = float(new_rate)
            #use the median of fico range
            #convert unicode to string
            range = str(d['fico'])
            ranges = range.split('-')
            #convert the ranges to an integer for calculations
            ranges = [int(r) for r in ranges]
            mean_fico = (ranges[1] + ranges[0]) / 2
            new_d['fico'] = mean_fico
            new_data.append(new_d)
        return new_data

    #same as above but formats csv file
    #path is the path to the csv data file
    def format_csv(self):
        formated = []
        with open(path) as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            for i, row in enumerate(reader):
                #skip the header row
                if i == 0:
                    continue

                rate = row[0]
                #strip the percentage from rate
                rate = rate.strip('%')
                ranges = row[1]
                #get the average of the the fico range
                ranges = ranges.split('-')
                ranges = [int(r) for r in ranges]
                mean_fico = (ranges[1] + ranges[0]) / 2
                formated.append({'rate': rate, 'fico': mean_fico})
        #create new csv file with formated data
        with open(self.path + '/LendingClubLoans/Csv/formatedLendingClub2014.csv', mode='w') as file:
            writer = csv.DictWriter(file, fieldnames = ['rate', 'fico'], delimiter = ',')
            writer.writeheader()
            for f in formated:
                writer.writerow(f)

    #trains the linear regression model using scikit-learn
    #path is the path to the csv data
    def train(self):
        dataset = pd.read_csv(self.path)
        X = dataset.iloc[:,-1].values
        y = dataset.iloc[:,1].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        regressor.fit(X_train, y_train)
        self.int = regressor.intercept_
        self.coef = regressor.coef_

    #make predictions of FICO score using interest rates
    #and coefficient/bias from train function.
    def predict(self, rate):
        fico = (rate*self.coef) + self.int
        return fico
