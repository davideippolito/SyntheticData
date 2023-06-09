# --------------------------------------------------------------------------- #
#                                   IMPORT                                    #
# --------------------------------------------------------------------------- #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------------------------------- #
#                                  FUNCTIONS                                  #
# --------------------------------------------------------------------------- #

def plot_dependency_region_balance(dataframes):
    # Get unique regions and sort them in descending order
    regions = np.unique(dataframes['RD']['Region'])
    regions = sorted(regions, reverse=True)
    # Get the number of regions
    num_regions = len(regions)
    # Set the width of each line
    line_width = 2.0
    # Set the spacing between lines
    line_spacing = 0.5
    # Calculate the x-axis positions of the lines
    line_positions = np.arange(num_regions) * line_spacing
    # Create subplots
    fig, ax = plt.subplots(figsize=(10, 6))
    # Define colors for each DataFrame
    colors = ['blue', 'red', 'green']
    # Loop over the dataframes and plot the total balance by region
    for idx, (label, dataframe) in enumerate(dataframes.items()):
        total_balance = dataframe.groupby('Region')['Balance'].sum()
        # Plot total balance with a line for each region
        ax.plot(line_positions, total_balance[regions], linewidth=line_width, color=colors[idx], label=label)
    # Set x-axis tick positions and labels
    ax.set_xticks(line_positions)
    ax.set_xticklabels(regions, rotation=90)
    # Set labels and title
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Balance')
    ax.set_title('Region / Balance')
    # Add legend
    ax.legend()
    # Show the plot
    plt.show()


def plot_dependency_employment_type_balance(dataframes, employment_types):
    # Create subplots
    fig, axs = plt.subplots(len(employment_types), 1, figsize=(10, 6 * len(employment_types)), sharex=True)
    # Iterate over the employment types
    for idx, employment_type in enumerate(employment_types):
        ax = axs[idx]
        # Iterate over the dataframes
        for i, dataframe in enumerate(dataframes):
            # Filter data based on the given employment type
            filtered_data = dataframe[dataframe['Employment_Type'] == employment_type]
            # Get balance values
            balance = filtered_data['Balance']
            # Plot balance with a different label for each DataFrame
            ax.hist(balance, bins=30, alpha=0.5, label=f'DataFrame {i+1}')
        # Set labels and title for each subplot
        ax.set_xlabel('Balance')
        ax.set_ylabel('Frequency')
        ax.set_title(f'{employment_type} / Balance')
        # Add legend to the last subplot
        if idx == len(employment_types) - 1:
            ax.legend()
    # Adjust the spacing between subplots
    plt.tight_layout()
    # Show the plot
    plt.show()


def compare_real_and_synthetic(real_data, synthetic_data):
    # Calculate summary statistics for real data
    real_stats = real_data.describe()
    # Calculate summary statistics for synthetic data
    synthetic_stats = synthetic_data.describe()
    # Create a comparison DataFrame
    comparison_df = pd.DataFrame(columns=['Statistic', 'Real Data', 'Synthetic Data'])
    # Iterate over columns and populate comparison DataFrame
    for column in real_data.columns:
        real_values = real_stats[column]
        synthetic_values = synthetic_stats[column]
        comparison_df = comparison_df.append({'Statistic': 'Count',
                                              'Real Data': real_values['count'],
                                              'Synthetic Data': synthetic_values['count']},
                                             ignore_index=True)

        comparison_df = comparison_df.append({'Statistic': 'Mean',
                                              'Real Data': real_values['mean'],
                                              'Synthetic Data': synthetic_values['mean']},
                                             ignore_index=True)

        comparison_df = comparison_df.append({'Statistic': 'Std',
                                              'Real Data': real_values['std'],
                                              'Synthetic Data': synthetic_values['std']},
                                             ignore_index=True)
        # Add more summary statistics as needed
    return comparison_df

# --------------------------------------------------------------------------- #
