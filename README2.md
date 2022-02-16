# Product Price Prediction for Black Friday dataset

### Data


### Objective
Black Friday Sale is one of the most popular and anticipated sale which falls on the day after Thanksgiving. A person buys a product based on different criteria.

In this demonstration, the goal is to use this dataset to predict the amount spent by a person on a product.

### Data Description
1) (User_ID)
1) (Product_ID)
1) (Gender)
1) (Age)
1) (Occupation)
1) (City_Category)
1) (Stay_In_Current_City_Years)
1) (Marital_Status)
1) (Product_Category_1)
1) (Product_Category_2)
1) (Product_Category_3)
1) (Purchase)

# Exploratory Data Analysis
The cloumns Product_Ctegory_2 and Product_Category_3 has 173,638 and 383,247 NaN values respectively. This will result in bad data. So we have to remove these columns.

# Feature Selection
Since the Product_ID and User_ID won't effect the prediction, We won't be including those columns as well.

# Feature Engineering
Since all the Columns are already categorized, we have encoded the columns except Marital status because it is already a numerical column. The column Gender is Label encoded. And the rest of the input columns (Age, Occupation, City_Category, Stay_In_Current_City_Years, Product_Category_1) are OneHot Encoded resulting in 58 columns.

The resulting matrix is then Standardized using Standard Scaler 