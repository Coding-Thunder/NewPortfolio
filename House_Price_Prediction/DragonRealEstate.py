# Basic Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from joblib import dump
# ML Models Imports Statements
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
# Contains original data from data file
housing = pd.read_csv("data.csv")
my_pipeline = Pipeline([("imputer",SimpleImputer(strategy = "median")),
                          ("strd_scaller",StandardScaler())                                            ])

# train test spliting
split = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state = 42)
for train_index, test_index in split.split(housing, housing["CHAS"]):
    strat_train_data = housing.loc[train_index]
    housing_test_data = housing.loc[test_index]

housing_train_data = strat_train_data.copy()
# att = ["MEDV","RM","ZM","LSTAT","TAX"]
# scat_matt = scatter_matrix(housing[att], figsize=(12,8))

# tO see correlation of training set
cor_relation = housing_train_data.corr()


# feture and label seperation
housing_features = housing_train_data.drop("MEDV", axis = 1)
housing_labels = housing_train_data["MEDV"]

housing_final_trainingset = my_pipeline.fit_transform(housing_features)

# Selection of best woking ml model 
# model = LinearRegression()
model = RandomForestRegressor()
model.fit(housing_final_trainingset,housing_labels)

housing_pred = model.predict(housing_final_trainingset)
mse = mean_squared_error(housing_labels,housing_pred)
lin_rmse = np.sqrt(mse)

cross_score = cross_val_score(model, housing_final_trainingset, housing_labels, scoring= "neg_mean_squared_error",cv=10)
rmse_scores = np.sqrt(-cross_score)


def output(scores):
    print("mean",scores.mean())
    print("standrd deviation",scores.std())


#model saved 
dump(model, "DragonRealEstate.joblib")

if __name__ == "__main__":
    print(rmse_scores)
    print(cor_relation)
    output(rmse_scores)