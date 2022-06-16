#import modules
import pandas as pd
import glob
  
# path of the folder
path = r'C:\Users\Hasso\Downloads\Programmeren\Python Projects\ExcelFolder' #define here your own folder make a directory in the same folder you are storing this file and name it ExcelFolder and change the path
  
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
print('Final Sheet:', finalexcelsheet)
# display(finalexcelsheet)
  
finalexcelsheet.to_excel(r'C:\Users\Hasso\Downloads\Programmeren\Python Projects\Final.xlsx', index=False) #change this into the folder you want to store the file and give it a name FinalExcel.xlsx or something else