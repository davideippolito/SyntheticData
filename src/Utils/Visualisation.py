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

# --------------------------------------------------------------------------- #
