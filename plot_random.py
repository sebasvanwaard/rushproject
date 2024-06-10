import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_random_csv(csv):
    """
    This function plots the distribution of the valid moves used for solving a board. 
    """

    df = pd.read_csv(csv)

    # print(df)

    number_of_iterations = max(df['iteration'])

    sns.histplot(df['valid_moves'], bins=50, kde=False, edgecolor='black', color='blue')
    sns.histplot(df['valid_moves'], bins=50, kde=True, color='red', linewidth=2, alpha=0)

    plt.title(f'Distribution of the number of Valid Moves necessary \n to solve the puzzle with {number_of_iterations} Iterations with KDE line')
    plt.xlabel('Valid Moves')
    plt.ylabel('Frequency')

    plt.show()

plot_random_csv('experiments/random/Rushhour6x6_1.csv')