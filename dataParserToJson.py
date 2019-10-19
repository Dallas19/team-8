#import pandas library
import pandas as pd

#Function receives input file path as excel format
#and returns the output as JSON format
def readFile(df, output):
  data = pd.read_excel(df)
  return data.to_json(output)