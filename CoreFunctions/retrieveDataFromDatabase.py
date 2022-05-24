#gets data from our online database for our functions
import psycopg2
import psqlConfig as config

from CoreFunctions.conversionFunctions import *
from CoreFunctions.helperCheckInput import *
from CoreFunctions.indexDictionary import *

def getCountyStateData(county, state):
    '''returns a list of data that fits the county and state from dataSet'''
    my_source = DataSource()
    rawdata = my_source.getState(county,state)
    return rawdata

class DataSource:
    '''this is the object that connects the database to python code'''
    def __init__(self):
        '''this intlizes the variable that points to the database'''
        self.connection = self.connect()

    def connect(self):
        '''this opens the connection to the pesfied data base or returns an error if the data base cannot be reached'''
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def getState(self,countyName,stateName):
        '''
        get data according to county and state in the database
        input: countyName, stateName as strings
        output: a tuple object of data
        '''
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM  CovidData WHERE StateName = %s and CountyName =%s ORDER BY day"
            cursor.execute(query, (stateName,countyName))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

if __name__ == '__main__':
    print(getCountyStateData('Warren', 'Iowa'))
