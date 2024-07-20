#DataFrames: It is a 2-D data structures like a 2D array with table including rows and columns.
import pandas as pd
data= {"cal":[420, 380, 390],
       "dur":[50, 40, 45]}
shreyas=pd.DataFrame(data)
print(shreyas)


#Locate row: Pandas use th eloc attribute to return one or more specified row.
import pandas as pd
data= {"cal":[420, 380, 390],
       "dur":[50, 40, 45]}
shreyas=pd.DataFrame(data)
print(shreyas.loc[0])

#Example o freturning (output) row 0 and 1.
import pandas as pd
data= {"cal":[420, 380, 390],
       "dur":[50, 40, 45]}
shreyas=pd.DataFrame(data)
print(shreyas.loc[[0, 1]])

#Name Index: With the index arg, you can name your own index.
import pandas as pd
data= {"cal":[420, 380, 390],
       "dur":[50, 40, 45]}
shreyas=pd.DataFrame(data, index=["day1", "day2", "day3"])
print(shreyas)

#Locate the name index:
import pandas as pd
data= {"cal":[420, 380, 390],
       "dur":[50, 40, 45]}
shreyas=pd.DataFrame(data, index=["day1", "day2", "day3"])
print(shreyas.loc["day2"])

#Output in a DataFrame
import pandas as pd
data= {"cal":[420, 380, 390],
       "dur":[50, 40, 45]}
shreyas=pd.DataFrame(data, index=["day1", "day2", "day3"])
print(shreyas.loc[["day1", "day2"]])

#Load th edata from the CSV file into line DataFrame i.e. data.csv .
import pandas as pd
fileload=pd.read_csv("data.csv")
print(fileload)