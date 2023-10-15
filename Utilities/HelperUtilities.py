# from win32com import client as wc
# import textract
# import codecs
import json
import os as OS
import re
from datetime import datetime, timedelta
#import ProjectConstantsProvider

# Reading Data from JSON File

def ReadJsonFile(FilePath, Key):
    status = False
    # FilePath = "C:/Projects/PythonSpace/.myvenv/Util/FileCompare/Settings.json"
    # Key = "PreDataFilePath"
    value = None
    try:
        if (OS.path.exists(FilePath) and Key != None):
            # print(" Reading json file.")
            with open(FilePath, 'r') as reader:
                data = json.load(reader)
                value = data[Key]
                status = True
        else:
            print('File path or Key is not correct.!! >> ' + FilePath)
    except Exception as e:
        print('Exception occured while reading the file json file.>> ' + FilePath)
    return value


# =======================================================================================
# Read .Text File

def ReadTextFile(FilePath):
    Status = False
    try:
        with open(FilePath, "r") as reader:
            ContentsList = reader.readlines()
            ContentsList = [x.strip('\n') for x in ContentsList]

            Status = True

    except Exception as e:
        print("Exception Occured while reading Text File file: " + str(e))
        Status = False

    return ContentsList


# =========================================================================


def IfListsEqual(List1, List2):
    # List1 = ['Date is my name.' , 'Date: 15th Jan', 'My name is Dhruav']
    # List2 = ['Date is my name.' , 'Date: 16th Jan', 'My name is Dhruava']
    MyText = 'Date:'
    StatusList = []
    len1 = len(List1)
    len2 = len(List2)
    try:
        for x in range(len2):
            Value1 = List1[x]
            Value2 = List2[x]
            if Value1 == Value2:
                Status = True
            else:
                if (MyText in Value1 or MyText in Value2):
                    Status = True
                else:
                    Status = False
            StatusList.append(Status)
        if False not in StatusList:
            Status = True
        else:
            Status = False
    except Exception as e:
        print("Exception occured during comparing the Lists: " + str(e))
        Status = False
    # print(StatusList)
    return Status

# ========================================================================

## Read CSV File rowwise and return a list containing all the row values.
## Input : File path
## Output : list[] , containing all the rows.
import csv
def ReadCSV(FileName):
    #FileName = 'TestData.csv'
    # Open the CSV file
    DataList = []
    try:
        if (OS.path.exists(FileName)) and FileName != None:
            with open(FileName, 'r') as file:
                # Create a CSV reader object
                reader = csv.reader(file)
                header = next(reader)
                 # Read the CSV file row by row
                for row in reader:
                    #Putting Each row is a list of values
                    DataList.append(row)
        else:
            print('File : < ' + FileName + ' > Not Found!')
    except Exception as e:
        print('Unable to Read the File!' + str(e))
    return DataList

#========================================================================
## Provide Column values of a CSV file
## Input : CSV File Path , Column Name (column Header )
## Output : list[] with all values in the column
import csv
def getColumValues_csv(filename, columnName):

    column_values = []
    try:
        with open(filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                column_values.append(row[columnName])
    except Exception as e:
        print('Unable to read CSV file : ' + str(filename))
        return column_values

    return column_values



## ====================================================================
"""Extract nested values from a JSON tree."""

def jsonExtract(jsonObject, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(jsonObject, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(jsonObject, dict):
            for k, v in jsonObject.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(jsonObject, list):
            for item in jsonObject:
                extract(item, arr, key)
        return arr

    values = extract(jsonObject, arr, key)
    return values
#=============================================================================
def is_yesterday_date(input_date_string):
    try:
        input_date = datetime.strptime(input_date_string, "%Y-%m-%dT%H:%M:%S%z")
        current_date = datetime.now(input_date.tzinfo)
        yesterday_date = current_date - timedelta(days=1)

        return input_date.date() == yesterday_date.date()
    except ValueError:
        return False
#==============================================================================
import logging
def logger(message , type = 'info'):

    # Configure logging
    logging.basicConfig(
        filename='runLog.log',  # Name of the log file
        #level=logging.DEBUG,  # Minimum log level to record
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    if type.lower() == 'info':
        logging.info(message)
    elif type.lower() == 'debug':
        logging.debug(message)
    elif type.lower() == 'warning':
        logging.warning(message)
    elif type.lower() == 'error':
        logging.error(message)
    elif type.lower() == 'critical':
        logging.critical(message)


#==============================================================================
import inspect
def get_current_method_name():
    return inspect.currentframe().f_back.f_code.co_name

#****************************************************************************
from configparser import ConfigParser
def read_INI_File(filename, sectionHeader , key):
    value = None
    isFileExist = OS.path.isfile(filename)
    if isFileExist:
        try:

            configur = ConfigParser()
            configur.read(filename)
            value = configur.get(sectionHeader, key)
        except Exception as e:
            print('Getting issues in reading INI file. < ' + filename + ' > ! ' + 'Error: ' + str(e) )
            return value
    return value

#****************************************************************************
# Reading CSV File using Pandas
## Input : CSV File Path
## Output : list[] with all values in the rows
import pandas as pd
def getAllRows_csv_pandas(fileName):
    list_of_rows = []
    try:
        if (OS.path.exists(fileName)) and fileName != None:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(fileName)

            # Convert the DataFrame to a list of rows
            list_of_rows = df.values.tolist()
        else:
            print('File : < ' + fileName + ' > Not Found!')
    except Exception as e:
        print('Unable to Read the File!' + str(e))
    return list_of_rows

#****************************************************************************
# Extract a Number from a String
## Input : String that has a number eg 'The amount is $234.20'
## Output : Number in the string

import re

def extract_number_from_string(input_string):
    # Use regular expression to find numbers in the string
    numbers = re.findall(r'\d+', input_string)

    # If there are multiple numbers, you can choose the first one
    if numbers:
        return int(numbers[0])
    else:
        return None  # Return None if no numbers were found


#****************************************************************************
# Get a particular  row from a csv File
## Input : CSV file, columnName, Column Value to Match
## Output : Row in a list of Dictioniries

import pandas as pd
def getArow_csv(csvFile,column_name,value_to_match):
    filtered_row_list= []
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csvFile)

        # Replace 'column_name' with the name of the column you want to filter on
        # column_name = 'Name'
        # value_to_match = 'getSingleRetunAll_picqer'

        # Filter rows where the specified column equals the desired value
        filtered_row = df[df[column_name] == value_to_match]
        filtered_row_list = filtered_row.values.tolist()
        # Print the filtered row(s)
    except Exception as e:
        print('Issue in Read the File! < Error > : ' + str(e))
    return filtered_row_list




# #*****************************************************************
# Get a Date which is current Date or a past date
## Input : DeltaDaysNumber ( for currentDate DeltaDaysNumber = 0 , for Ysterdays Date DeltaDaysNumber = 1 )
## Output : Return the date ( currentDate - DeltaDaysNumber) in "%Y-%m-%d 00:00:00" format.
def getDate(deltaDaysNumber):
    try:
        # Get the current date and time
        now = datetime.now()

        # Format it as "YYYY-MM-DD 00:00:00"
        formatted_Current_date = now.strftime("%Y-%m-%d 00:00:00")

        input_date = datetime.strptime(formatted_Current_date, "%Y-%m-%d 00:00:00")
        current_date = datetime.now(input_date.tzinfo)
        requiredDate = current_date - timedelta(days=deltaDaysNumber)

        return requiredDate.strftime("%Y-%m-%d 00:00:00")
    except Exception as e:
        return formatted_Current_date


#**************************************************************************************************
# Check if a file is exist and not empty
## Input : file name
## Output : Boolean ( True/False )


def file_exists_and_not_empty(file_path):
    # Check if the file exists
    if OS.path.exists(file_path):
        # Check if the file is not empty (has a size greater than 0)
        return OS.path.getsize(file_path) > 0
    else:
        # The file does not exist
        return False


#******************************************************************************************************
# Read an xlsx and return a list of data
## Input : file name , Sheet name
## Output : List
# import pandas as pd
def readExcel_pandas(file_path, sheet_name):
    # Replace 'your_file.xlsx' with the path to your Excel file
    #file_path = "D:\FreelanceWork\Alwin\Docs\CampaignTestData.xlsx"
    data_list_of_dicts = []
    # Replace 'sheet_name' with the name or index of the sheet you want to read
    #sheet_name = "campaign"  # Replace with the actual sheet name or index

    try:

        df = pd.read_excel(file_path, sheet_name=sheet_name)
        #df = pd.read_excel(file_path)
        #data_list = df.values.tolist()
        data_list_of_dicts = df.to_dict(orient="records")
        #print(data_list)
    except FileNotFoundError:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data_list_of_dicts


#******************************************************************************************************
# Search for a String in a CSV Column1, If found get the corresponding value from Column2
## Input : SearchString , Column1, Column2
## Output : List of String
# import pandas as pd

def get_Matching_cellValues_csv(file_path,search_string,column_to_search,column_value_to_capture):

    # Step 2: Read the CSV file into a DataFrame
    #file_path = 'output/GetListOfCampaigns.csv'
    df = pd.read_csv(file_path)

    # Step 3: Search for a string in Column1 and filter the DataFrame
    #search_string = '8720254660523 - Category - Auto - Auto - NL'
    filtered_df = df[df[column_to_search].str.contains(search_string, case=False, na=False)]

    # Step 4: Retrieve the corresponding values from Column2
    corresponding_values = filtered_df[column_value_to_capture].tolist()

    # Print the corresponding values
    #print('Corresponding values from CompaignID:')
    #print(corresponding_values)
    return corresponding_values
#***********************************************************************************************************************
# Search for a String in a CSV Column1, If found get the corresponding value from Column2
## Input : SearchString , Column1, Column2
## Output : List of String
# import pandas as pd

import openpyxl
def column_letter_from_column_name(sheet, column_name):
    for cell in sheet[1]:  # Assumes column names are in the first row
        if cell.value == column_name:
            return cell.column_letter

    # If the column name is not found, you may want to handle this case accordingly
    raise ValueError(f"Column name '{column_name}' not found in the sheet.")

#***********************************************************************************************************************
def write_status_to_excel(file_path, sheet_name, row_number, column_name, data_to_write):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select the specified sheet by name
    sheet = workbook[sheet_name]

    # Get the column letter for the specified column name
    column_letter = column_letter_from_column_name(sheet, column_name)

    # Update the status in the specified row and column
    sheet[f"{column_letter}{row_number}"].value = data_to_write

    # Save the workbook with the updated status
    workbook.save(file_path)


# Example usage
# file_path = 'input/CampaignTestData.xlsx'
# sheet_name = 'adgroup'
# row_number = 2  # Example row number (1-based index)
# column_name = 'adgroupId'  # Example column name
# data_to_write = 819828  # Example status value

# Write the status to the specified row and column
# write_status_to_excel(file_path,sheet_name, row_number, column_name, data_to_write)
#***********************************************************************************************************************
# input_date_str = '01-10-2023'
# input_format = '%d-%m-%Y'
# desired_outout_date_formate = '%Y-%m-%d'

def convert_to_desired_format(input_date_str, input_format, desired_outout_date_formate):
    try:
        # Parse the input date using the provided input format
        parsed_date = datetime.strptime(input_date_str, input_format)

        # Convert the parsed date to the desired format 'YYYY-MM-DD'
        formatted_date = parsed_date.strftime(desired_outout_date_formate)

        return formatted_date
    except ValueError:
        return "Invalid date format or date"



# **********************************************************************************************************************

# On the basis of a input date , return a datelist till current date
## Input : Date ( '%Y-%m-%d' )
## Output : List of dates till current data
#from datetime import datetime, timedelta

def generate_date_list_Ymd(input_startDate_str,input_endDate_str):

    # Initialize an empty list to store the dates
    date_list = []
    try:

        # Convert input date string to a datetime object
        input_startDate = datetime.strptime(input_startDate_str, '%Y-%m-%d')


        if input_endDate_str == 'NA':
            # Get the current date
            input_endDate = datetime.today()
        else:
            input_endDate = datetime.strptime(input_endDate_str, '%Y-%m-%d')



        # Iterate from the input date to the current date, adding each date to the list
        while input_startDate <= input_endDate:
            date_list.append(input_startDate.strftime('%Y-%m-%d'))
            input_startDate += timedelta(days=1)
    except Exception as e:
        print('Error is getting Date lit. :' + str(e))

    return date_list

# Example usage
#input_startDate_str = '2023-10-01'
#input_endDate_str = 'NA'

#date_list = generate_date_list(input_startDate_str,input_endDate_str)

# Print the list of dates
#print(date_list)
