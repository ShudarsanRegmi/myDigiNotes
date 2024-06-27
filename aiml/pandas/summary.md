# Pandas


> Python library used for working with data sets.

## Features
 --> It has functions for cleaning, analysing, exploring and manipulating data.

 --> Helps us to make conclusions from big data.
 
 --> Capable of cleaning messy data sets and make them reaable and relevant.
 
 
 ### Converting dictionary with data frame
 
 ```
 import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3,7,2]
}


myvar = pd.DataFrame(mydataset)

print(myvar)
```

# Pandas Series
>It is like a column in a table. It is 1D array holding data of any type.

```
import pandas as pd
a = [1,3,5,7]
my_series = pd.Series(a)
my_series_with_label = pd.Series(a, index = ["x", "y", "z"])
print(my_series)

```

# Dataframe
>A pandas data frame is a 2 dimensional data structure similar to a table

## Creating a DataFrame

### From Dictionary / Json

```
import pandas as pd
data = {} # data can be dictionary/json
df = pd.DataFrame(data)
print(df.loc[0]) # Fetching 0th row
```
### From CSV Files

```
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
print(df.to_string()
print(pd.options.display.max_rows)

```

# Viewing Data

```
df.head() # Fetches the first 5 rows
df.head(10) # Fetches the first 10 rows
df.tail() # Fetches the last 5 rows
df.info() # display the information about the data

# Manipulating Data

### Accessing a specific row
```python
df.loc[column_no]
```
### Dropping Few columns from top
```python
mdf = df.iloc[column_no:]
```
### Deleting specific column_no from last
```python
d.iloc[:,:22]
```


# Data Cleaning
>Data cleaning means removing bad data(empty cells, data in wrong format, wrong data, duplicates) from the data frame



**Removing rows with empty cells is an effective strategy to prevent incorrect data analysis, especially in large datasets where the impact of removing a few rows is negligible**


## Removing rows containing empty cells

```
new_df = df.dropna() # returns the new dataframe
df.dropna(inplace=True) # changes the original dataframe
```

## Replacing Empty Values

```
df.fillna(130, inplace=True)
df.['col_name'].fillna(130, inplace=True)
```

**Replacing empty cells with the mean,median,mode of the column is a good idea**

```
x = df['col_name'].mean()
x = df['col_name'].median()
x = df['col_name'].mode()[0]
df['col_name'].fillna(x,inplace=True)
```



**Iterating through each row**
```
for i in df.index
	print(df.loc[i,'col'])
```

# Removing Wrong Data

```
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
    #df.drop(x, inplace = True) # dropping the

```

# Removing Duplicate Entries

## Finding Duplicates

```
print(df.duplicated()
```

## Dropping Duplicates

```
df.drop_duplicates(inplace=True)
```

# Pandas Correlation

## Finding correlation between each columns in dataframe
```
df.corr()
```

# Plotting DataFrame with matplotlib

```
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.plot()
plt.show()
```

## Plotting Scatter Diagram
```
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
```

## Plotting Histogram
```
df["Duration"].plot(kind = 'hist')
```

