#A Pandas series is like a column in a table. It is 1-D array which holds data of any type.
#Here we will create a simple pamdas series.
import pandas as pd
shreyas=[1,7,2]
shreyasnew=pd.Series(shreyas)
print(shreyasnew)

#Labeling  - lable can be used to access a specified value.
import pandas as pd
shreyas=[1,7,5]
shreyasnew=pd.Series(shreyas)
print(shreyasnew[0])

#With create lables you can create your own name lable:
import pandas as pd
shreyas=[1,7,2]
shreyasnew=pd.Series(shreyas, index=["x", "y", "z"])
print(shreyasnew)

#Labeling  - lable can be used to access a specified value.(After creating own lable)
import pandas as pd
shreyas=[1,7,5]
shreyasnew=pd.Series(shreyas, index=["x", "y", "z"])
print(shreyasnew["x"])

#You can also use a key or value object like a dictonary, when creating a series.
#Here we will create a simple pandas series from a dictionary.
import pandas as pd
cal = {"Day1":420,
       "Day2":380,
       "Day3":390}
shreyasnew=pd.Series(cal)
print(shreyasnew)

#Now we will create a series using only data from day1 and day2.
import pandas as pd
cal = {"Day1":420,
       "Day2":380,
       "Day3":390}
result=pd.Series(cal, index=["Day1", "Day2"])
print(result)

#DataFrame:  Data sets in pandas are usually multidimensionals tables, and they are called DataFrames.
#Series are like columns and DataFrames is whole table.
#Wewill now create a DataFrame from 2 series.
import pandas as pd
shreyas={"cal":[420, 380, 390], "duration": [50, 40, 45]}
shreyasnew=pd.DataFrame(shreyas)
print(shreyasnew)