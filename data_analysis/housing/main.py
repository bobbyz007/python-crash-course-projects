import pandas as pd

from housing.analyze_data import handle_text_attribute_with_onehot, \
    handle_text_attribute_with_ordinal, fill_missing_data, find_correlation_between_attributes, \
    feature_scaling_transfrom
from housing.download_data import load_housing_data
from housing.split_data import split_data_with_id_hash, split_data_stratified_shuffle
from housing.visualize_data import generate_income_category_by_value, visualize_income_category, \
    visualize_house_value_population, visualize_house_value_population_with_image, visualize_population_by_log, \
    visualize_median_age_by_gaussian_rbf
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
# find_correlation_between_attributes(housing)

# rever to a clean training set
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()


fill_missing_data(housing)
# Handling text attributes: convert from text to number
handle_text_attribute_with_ordinal(housing)
# encode with binary attribute, sparse matrix
handle_text_attribute_with_onehot(housing)

# feature scaling and transformation
housing_num = housing.select_dtypes(include=[np.number])
feature_scaling_transfrom(housing_num)

# transforming a feature to make it closer to a Gaussian distribution
# visualize_population_by_log(housing)
# visualize_median_age_by_gaussian_rbf(housing)
