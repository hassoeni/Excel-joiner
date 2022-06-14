#import modules
import pandas as pd
import glob
  
# path of the folder
path = r'ExcelFolder' #define here your own folder make a directory in the same folder you are storing this file and name it ExcelFolder
  
# reading all the excel files
filenames = glob.glob(path + "\*.xlsx")
print('File names:', filenames) 
  
# initializing empty data frame
finalexcelsheet = pd.DataFrame()
  
# to iterate excel file one by one 
# inside the folder
for file in filenames:
  
    # combining multiple excel worksheets
    # into single data frames
    df = pd.concat(pd.read_excel(
      file, sheet_name=None), ignore_index=True, sort=False)
  
    # appending excel files one by one
    finalexcelsheet = finalexcelsheet.append(
      df, ignore_index=True)
  
# to print the combined data
print('Final Sheet:')
# display(finalexcelsheet)
  
finalexcelsheet.to_excel(r'Final.xlsx', index=False)