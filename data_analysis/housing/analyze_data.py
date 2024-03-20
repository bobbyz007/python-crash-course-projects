import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fill_missing_data(housing):
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy="median")
    housing_num = housing.select_dtypes(include=[np.number])
    imputer.fit(housing_num)  # compute median of each attribute
    X = imputer.transform(housing_num)


def handle_text_attribute_with_ordinal(housing):
    housing_cat = housing[["ocean_proximity"]]
    from sklearn.preprocessing import OrdinalEncoder
    ordinal_encoder = OrdinalEncoder()
    housing_cat_encoded = ordinal_encoder.fit_transform(housing_cat)
    print(housing_cat_encoded[:8])


def handle_text_attribute_with_onehot(housing):
    housing_cat = housing[["ocean_proximity"]]
    from sklearn.preprocessing import OneHotEncoder
    cat_encoder = OneHotEncoder()
    housing_cat_1hot = cat_encoder.fit_transform(housing_cat)  # row: record, column: attribute category
    print(housing_cat_1hot.toarray())
    # another way: convert categorical feature to one-hot representation
    df_test = pd.DataFrame({"ocean_proximity": ["INLAND", "NEAR BAY"]})
    print(pd.get_dummies(df_test))
    print(cat_encoder.transform(df_test).toarray())  # cat_encoder remembers the categories it was trained on.

    print(cat_encoder.feature_names_in_)
    print(cat_encoder.get_feature_names_out())


def find_correlation_between_attributes(housing):
    # Look for correlations between attributes
    corr_matrix = housing.corr(numeric_only=True)
    print(corr_matrix["median_house_value"].sort_values(ascending=False))
    # another way to check correlation
    from pandas.plotting import scatter_matrix
    attributes = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
    scatter_matrix(housing[attributes], figsize=(12, 8))

    # Looking at the correlation scatterplots, it seems like the most promising attribute
    # to predict the median house value is the median income
    housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1, grid=True)
    plt.show()

def feature_scaling_transfrom(housing_num):
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
    housing_num_min_max_scaled = min_max_scaler.fit_transform(housing_num)
    print(housing_num_min_max_scaled[0])

    std_scaler = StandardScaler()
    housing_num_std_scaled = std_scaler.fit_transform(housing_num)
    print(housing_num_std_scaled[0])

    sample_df = pd.DataFrame({"column1": [1, 2, 4, 100], "column2": [1, 2, 4, 3]})
    print(min_max_scaler.fit_transform(sample_df))
    print(std_scaler.fit_transform(sample_df))



