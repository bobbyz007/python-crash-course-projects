from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import rbf_kernel


def visualize_simple(data):
    # visualize the data
    data.hist(bins=50, figsize=(12, 8))
    plt.show()

def generate_income_category_by_value(housing):
    # 根据值生成类别
    housing["income_cat"] = pd.cut(housing["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                   labels=[1, 2, 3, 4, 5])


def visualize_income_category(housing):
    housing["income_cat"].value_counts().sort_index().plot.bar(rot=0, grid=True)
    print(housing["income_cat"].value_counts())
    plt.xlabel("Income category")
    plt.ylabel("Number of districts")
    plt.show()


def visualize_house_value_population(housing):
    housing.plot(kind="scatter", x="longitude", y="latitude", grid=True, alpha=0.2)
    housing.plot(kind="scatter", x="longitude", y="latitude", grid=True,
                 s=housing["population"] / 100, label="population",  # s denotes the radius of each circle(district)
                 c="median_house_value", cmap="jet", colorbar=True,
                 # c denotes color by median_house_value column value
                 legend=True, sharex=True, figsize=(10, 7))
    plt.show()


def visualize_house_value_population_with_image(housing):
    # a more beautiful version of the previous figure
    IMAGES_PATH = Path().absolute().parent / "images" / "end_to_end_project"
    IMAGES_PATH.mkdir(parents=True, exist_ok=True)
    housing_renamed = housing.rename(
        columns={"latitude": "Latitude", "longitude": "Longitude", "population": "Population",
                 "median_house_value": "Median house value(USD)"})
    housing_renamed.plot(kind="scatter", x="Longitude", y="Latitude", grid=True,
                         s=housing_renamed["Population"] / 100, label="Population",
                         # s denotes the radius of each circle(district)
                         c="Median house value(USD)", cmap="jet", colorbar=True,
                         # c denotes color by median_house_value column value
                         legend=True, sharex=False, figsize=(10, 7))
    california_img = plt.imread(IMAGES_PATH / "california.png")
    axis = -124.55, -113.95, 32.45, 42.05
    plt.axis(axis)
    plt.imshow(california_img, extent=axis)
    plt.show()

def visualize_population_by_log(housing):
    fig, axs = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
    housing["population"].hist(ax=axs[0], bins=50)
    housing["population"].apply(np.log).hist(ax=axs[1], bins=50) # loge
    axs[0].set_xlabel("Population")
    axs[1].set_xlabel("Log of population")
    axs[0].set_ylabel("Number of districts")
    plt.show()

def visualize_median_age_by_gaussian_rbf(housing):
    ages = np.linspace(housing["housing_median_age"].min(),
                       housing["housing_median_age"].max(),
                       500).reshape(-1, 1)
    gamma1 = 0.1
    gamma2 = 0.03
    rbf1 = rbf_kernel(ages, [[35]], gamma=gamma1)
    rbf2 = rbf_kernel(ages, [[35]], gamma=gamma2)

    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Housing median age")
    ax1.set_ylabel("Number of districts")
    ax1.hist(housing["housing_median_age"], bins=50)

    ax2 = ax1.twinx() # create a twin axis that shares the same x-axis
    color = "blue"
    ax2.plot(ages, rbf1, color=color, label="gamma = 0.10")
    ax2.plot(ages, rbf2, color=color, label="gamma = 003", linestyle="--")
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylabel("Age similarity", color=color)

    plt.legend(loc="upper left")
    plt.show()


