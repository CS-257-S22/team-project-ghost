from CoreFunctions.conversionFunctions import *
from CoreFunctions.helperCheckInput import *
from CoreFunctions.indexDictionary import *
from CoreFunctions.helperClasses import *

#use the database if operating on server, else use the local .csv files
import settings

if (settings.isOnServer):
    from CoreFunctions.retrieveDataFromDatabase import *
else:
    from CoreFunctions.retrieveDataFromLocal import *
    
def getDataCombination(location, dateRange):
    """
    Inputs: 
    locations is a Location object
    dateRange is a DateRange object

    Output:
    returns a DataCombanation object for graphing and displaying raw data
    """
    dataSet = getDataWithLocationAndDateRange(location, dateRange)
    dates = getDates(dataSet)
    confirmedCases = getConfirmedCases(dataSet)
    confirmedDeaths = getConfirmedDeaths(dataSet)
    return DataCombination(dates, confirmedCases, confirmedDeaths)

def getDataWithLocationAndDateRange(location, dateRange):
    '''
    returns a list of data that fits the given location and daterange in 
    the format [Date (as a list of form [Year, Month, Day]), County, State, Confirmed Cases, Confirmed Deaths]
    
    locations is a Location object
    dateRange is a DateRange object
    '''

    list = getCountyStateData(location.county, location.state)
    list = getDateRangeData(list, dateRange)
    return list

def getDateRangeData(dataSet, dateRange):
    '''
    trim a list with a dateRange
    return the first subset of record within that daterange'''
    startDate = toDateTime(dateRange.startDate)
    endDate = toDateTime(dateRange.endDate)
    newList = []
    for line in dataSet:
        line = list(line)
        line[dateIndex] = splitDate(line[dateIndex])
        thisdate = toDateTime(line[dateIndex])
        if(thisdate < startDate): continue
        if(thisdate > endDate): break
        newList.append(line)
    return newList

def getDates(dataSet):
    '''return the column of dates from a list '''
    
    dates = [i[dateIndex] for i in dataSet]
    return dates

def getConfirmedCases(dataSet):
    '''return the column of death numbers from a list '''
    
    deaths = [int(i[confirmedCaseseIndex]) for i in dataSet]
    return deaths

def getConfirmedDeaths(dataSet):
    '''return the column of confirmed cases from a list '''
    deaths = [int(i[confirmedDeathsIndex]) for i in dataSet]
    return deaths

def getStateNames(dataSet):
    '''input data set'''
    '''trim date set to just state names'''
    '''out put list of state names'''
    stateNames = []
    for line in dataSet:
        stateNames.append(line[stateIndex])
    return  stateNames

