### 1. **Feature Engineering**
Feature engineering is the process of transforming raw data into meaningful features that help machine learning models perform better.

#### 1.1 **Missing Values Imputation**
Missing data is common in real-world datasets. Imputation is the process of replacing missing values with substitute values to prevent issues during model training.
- **Methods:**
  - **Mean/Median/Mode Imputation:** Replaces missing values with the mean (numerical), median (numerical), or mode (categorical).
  - **Forward/Backward Fill:** For time-series data, forward fill propagates the last observed value, while backward fill uses the next observed value.
  - **Interpolation:** Estimating missing values based on other data points.
  - **K-Nearest Neighbors (KNN) Imputation:** Uses the nearest neighbors to predict missing values.

#### 1.2 **Handling Categorical Variables**
Categorical variables contain discrete values like labels. These need to be encoded as numerical values for models.
- **Methods:**
  - **Label Encoding:** Assigns a unique number to each category.
  - **One-Hot Encoding:** Creates binary columns for each category.
  - **Target Encoding:** Replaces categories with the mean of the target variable.
  - **Frequency/Count Encoding:** Replaces categories with the count or frequency of each category.

#### 1.3 **Outlier Detection**
Outliers are data points that are significantly different from other observations and can distort model training.
- **Methods:**
  - **Z-Score:** Measures how far a data point is from the mean in terms of standard deviations.
  - **IQR (Interquartile Range):** Detects outliers that fall outside 1.5 * IQR from the 1st and 3rd quartiles.
  - **Visual Inspection:** Using box plots, scatter plots, or histograms to visually detect outliers.
  - **Isolation Forest/DBSCAN:** Machine learning-based approaches for detecting anomalies.

#### 1.4 **Feature Scaling**
Feature scaling ensures that numerical features are on a similar scale, which improves the performance of many algorithms (e.g., gradient descent-based models).
- **Methods:**
  - **Standardization (Z-score scaling):** Scales data to have a mean of 0 and a standard deviation of 1.
  - **Min-Max Scaling (Normalization):** Scales data between 0 and 1 by adjusting values relative to the minimum and maximum values.
  - **Robust Scaling:** Focuses on the median and IQR, making it less sensitive to outliers.
  - **Log Transformation:** Reduces the impact of extreme values by applying logarithmic scaling.

### 2. **Feature Construction**
Feature construction involves creating new features from existing data to improve model performance. This is often domain-specific.
- **Examples:**
  - **Polynomial Features:** Creating interaction terms or power terms like `x²`.
  - **Binning:** Converting continuous variables into categorical bins (e.g., age groups).
  - **Date-Time Features:** Extracting components like day, month, year, or weekday from a timestamp.
  - **Text Features:** Extracting features like word count or sentiment from text data.

### 3. **Feature Selection**
Feature selection involves selecting the most relevant features for a model, reducing dimensionality, and improving performance by eliminating redundant or irrelevant features.
- **Methods:**
  - **Filter Methods:** Using statistical tests (e.g., chi-square, correlation) to select features.
  - **Wrapper Methods:** Iteratively selecting features based on model performance (e.g., recursive feature elimination, forward/backward selection).
  - **Embedded Methods:** Feature selection is part of model training, such as with Lasso (L1 regularization), decision trees, or feature importance ranking in random forests.

### 4. **Feature Extraction**
Feature extraction reduces the dimensionality of data by transforming features into a lower-dimensional space, retaining the most informative parts of the data.
- **Methods:**
  - **Principal Component Analysis (PCA):** Transforms data into a set of orthogonal components, maximizing variance while reducing dimensions.
  - **Linear Discriminant Analysis (LDA):** Maximizes class separability and reduces dimensions in supervised tasks.
  - **t-SNE (t-Distributed Stochastic Neighbor Embedding):** Non-linear technique used for visualizing high-dimensional data in lower dimensions.
  - **Autoencoders:** Neural networks used to learn efficient representations of the data in an unsupervised manner.
