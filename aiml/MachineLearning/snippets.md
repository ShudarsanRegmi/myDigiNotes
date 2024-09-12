# Machine Learning Snippets

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
```


### Reading CSVs

```python
df = pd.read_csv('/path/to/csv', header=None)
df.head()
df.shape
df.describe()
```

### Splitting Data

```python
x = sonar_data.drop(columns=60, axis=1)
y = sonar_data[60]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=1)
```

### Training

```python
model = LogisticRegiression()
model.fit(x_train, y_train)
```

### Getting Prediction

```
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)
```







