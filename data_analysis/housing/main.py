import pandas as pd

from housing.download_data import load_housing_data
from housing.split_data import split_data_with_id_hash, split_data_stratified_shuffle
from housing.visualize_data import generate_income_category_by_value, visualize_income_category, \
    visualize_house_value_population, visualize_house_value_population_with_image
import numpy as np

# get data frame
housing = load_housing_data()
print(housing.info())
print(housing["ocean_proximity"].value_counts())

# train_set, test_set = shuffle_and_split_data(housing, 0.2)
# print(len(train_set))
# print(len(test_set))

housing_with_id = housing.reset_index()
print(housing_with_id.info())
train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")
print(len(train_set))
print(len(test_set))


generate_income_category_by_value(housing)
# visualize_income_category(housing)

# 分层抽样
strat_train_set, strat_test_set = split_data_stratified_shuffle(housing.copy()) # copy: A value is trying to be set on a copy of a slice from a DataFrame
# drop income_cat column as we won't use it anymore.
for _set in (strat_train_set, strat_test_set):
    _set.drop("income_cat", axis=1, inplace=True)

# now we only care the training set, and make a copy of the original so we can revert to it afterward
housing = strat_train_set.copy()
# visualize_house_value_population(housing)
# visualize_house_value_population_with_image(housing)

# Look for correlations between attributes
corr_matrix = housing.corr(numeric_only=True)
print(corr_matrix["median_house_value"].sort_values(ascending=False))
# another way to check correlation
from pandas.plotting import scatter_matrix
attributes = ["median_house_value", "median_income", "total_rooms","housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))

# Looking at the correlation scatterplots, it seems like the most promising attribute
# to predict the median house value is the median income
housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1, grid=True)
# plt.show()

# rever to a clean training set
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

# clean the data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")
housing_num = housing.select_dtypes(include=[np.number])
imputer.fit(housing_num) # compute median of each attribute
X = imputer.transform(housing_num)

# Handling text attributes: convert from text to number
housing_cat = housing[["ocean_proximity"]]
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
print(housing_cat_encoded[:8])

# encode with binary attribute, sparse matrix
from sklearn.preprocessing import OneHotEncoder
cat_encoder = OneHotEncoder()
housing_cat_1hot = cat_encoder.fit_transform(housing_cat) # row: record, column: attribute category
print(housing_cat_1hot.toarray())
# another way: convert categorical feature to one-hot representation
df_test = pd.DataFrame({"ocean_proximity": ["INLAND", "NEAR BAY"]})
print(pd.get_dummies(df_test))