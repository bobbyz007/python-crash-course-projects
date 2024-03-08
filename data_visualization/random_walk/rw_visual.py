import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(12,9))
    point_nums = range(rw.num_points)

    # edgecolors="none", to get rid of the black outline around each point.
    ax.scatter(rw.x_values, rw.y_values, c=point_nums, cmap=plt.cm.Blues, edgecolors="none", s=15)
    ax.set_aspect('equal')  # both axes should have equal spacing between tick marks

    # Emphasize the first and last points.
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (Y/n):")
    if keep_running == "n":
        break
