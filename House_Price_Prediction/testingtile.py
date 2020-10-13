from DragonRealEstate import *

x_test = housing_test_data.drop("MEDV", axis = 1)
y_test = housing_test_data["MEDV"]

x_test_prepared = my_pipeline.transform(x_test) 
final_predictions = model.predict(x_test_prepared)
final_mse = mean_squared_error(y_test,final_predictions)
final_rmse = np.sqrt(final_mse)
print(final_mse, final_rmse)