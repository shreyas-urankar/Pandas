#Read csv files: (comma separated file) it is a siimple way to store the big and biggest data sets. CSV files contains plain text.
#Loading the csv inot a dataframewoth to_string 
import pandas as pd
df = pd.read_csv("data.csv")
print(df.to_string())

#Loading the csv into a dataframe without to_string
import pandas as pd
df = pd.read_csv("data.csv")
print(df)

#max_rows: you can check your system's maximum rows with:
import pandas as pd 
print(pd.options.display.max_rows)

#Yes, we can increase the maximum number of rows to displaythe entire dataframe.
import pandas as pd 
pd.options.display.max_rows = 9999
df = pd.read_csv("data.csv")
print(df)