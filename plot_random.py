import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_random_csv(csv):
    """
    This function plots the distribution of the valid moves used for solving a board. 
    """

    df = pd.read_csv(csv)

    print(df)

    number_of_iterations = max(df['iteration'])
    average_moves = df['valid_moves'].mean()

    sns.histplot(df['valid_moves'], bins=50, edgecolor='black', color='blue')
    sns.histplot(df['valid_moves'], bins=50, kde=True, color='red', linewidth=2, alpha=0)

    plt.title(f'Distribution of the number of Valid Moves necessary \n to solve the puzzle with {number_of_iterations} Iterations with KDE line')
    plt.xlabel('Valid Moves')
    plt.ylabel('Frequency')

    plt.axvline(average_moves, color='green', linestyle='--', linewidth=2, label=f'Average Number of Moves: {average_moves}')

    plt.legend()

    plt.show()

plot_random_csv('experiments/random2/solved_Rushhour12x12_7.csv')