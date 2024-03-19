from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np


def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))


# create train and test set，每次产生的都是随机分配
def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


from zlib import crc32


def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2 ** 32


def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


# get data frame
housing = load_housing_data()
print(housing.info())
print(housing["ocean_proximity"].value_counts())

# visualize the data
# housing.hist(bins=50, figsize=(12, 8))
# plt.show()

# train_set, test_set = shuffle_and_split_data(housing, 0.2)
# print(len(train_set))
# print(len(test_set))

housing_with_id = housing.reset_index()
print(housing_with_id.info())
train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")
print(len(train_set))
print(len(test_set))

# 根据值生成类别
housing["income_cat"] = pd.cut(housing["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf], labels=[1, 2, 3, 4, 5])
# housing["income_cat"].value_counts().sort_index().plot.bar(rot=0, grid=True)
# print(housing["income_cat"].value_counts())
# plt.xlabel("Income category")
# plt.ylabel("Number of districts")
# plt.show()

from sklearn.model_selection import StratifiedShuffleSplit, train_test_split

splitter = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
strat_splits = []
# 根据 income_cat 分层抽样
for train_index, test_index in splitter.split(housing, housing["income_cat"]):
    strat_train_set_n = housing.iloc[train_index]
    strat_test_set_n = housing.iloc[test_index]
    strat_splits.append([strat_train_set_n, strat_test_set_n])

# use the first split
strat_train_set, strat_test_set = strat_splits[0]

# shorter way get a single split
strat_train_set, strat_test_set = train_test_split(housing, test_size=0.2, stratify=housing["income_cat"],
                                                   random_state=42)

# drop income_cat column as we won't use it anymore.
for _set in (strat_train_set, strat_test_set):
    _set.drop("income_cat", axis=1, inplace=True)

# now we only care the training set, and make a copy of the original so we can revert to it afterward
housing = strat_train_set.copy()
housing.plot(kind="scatter", x="longitude", y="latitude", grid=True, alpha=0.2)
housing.plot(kind="scatter", x="longitude", y="latitude", grid=True,
             s=housing["population"] / 100, label="population",  # s denotes the radius of each circle(district)
             c="median_house_value", cmap="jet", colorbar=True,  # c denotes color by median_house_value column value
             legend=True, sharex=True, figsize=(10, 7))
plt.show()

# a more beautiful version of the previous figure
IMAGES_PATH = Path().absolute().parent / "images" / "end_to_end_project"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)
housing_renamed = housing.rename(columns={"latitude": "Latitude", "longitude": "Longitude", "population": "Population",
                                          "median_house_value": "Median house value(USD)"})
housing_renamed.plot(kind="scatter", x="Longitude", y="Latitude", grid=True,
             s=housing_renamed["Population"] / 100, label="Population",  # s denotes the radius of each circle(district)
             c="Median house value(USD)", cmap="jet", colorbar=True,  # c denotes color by median_house_value column value
             legend=True, sharex=False, figsize=(10, 7))
california_img = plt.imread(IMAGES_PATH / "california.png")
axis = -124.55, -113.95, 32.45, 42.05
plt.axis(axis)
plt.imshow(california_img, extent=axis)
plt.show()

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
plt.show()

# rever to a clean training set
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()
