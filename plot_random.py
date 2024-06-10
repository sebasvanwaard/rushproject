import matplotlib.pyplot as plt
import pandas as pd

def plot_random_csv(csv):
    """
    This function plots the distribution of the valid moves used for solving a board. 
    """

    df = pd.read_csv(csv)

    print(df)

    plt.hist(df['valid_moves'], bins=50, edgecolor='black')
    plt.show()

# plot_random_csv('experiments/random/Rushhour6x6_1.csv')