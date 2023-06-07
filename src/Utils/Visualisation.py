import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_dependency_region_balance(RD, SD):
    # Get unique regions and sort them in descending order
    regions = np.unique(RD['Region'])
    regions = sorted(regions, reverse=True)

    # Get the number of regions
    num_regions = len(regions)

    # Set the width of each bar
    bar_width = 0.35

    # Set the spacing between bars
    spacing = 0.2

    # Calculate the center positions of the bars
    bar_positions = np.arange(num_regions)

    # Calculate the total balance for each region in RD and SD
    RD_total_balance = RD.groupby('Region')['Balance'].sum()
    SD_total_balance = SD.groupby('Region')['Balance'].sum()

    # Create subplots
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot RD total balance by region (inverted y-axis)
    ax.barh(bar_positions, RD_total_balance[regions], height=bar_width, color='blue', alpha=0.5, label='RD')

    # Plot SD total balance by region, overlapping RD bars (inverted y-axis)
    ax.barh(bar_positions, SD_total_balance[regions], height=bar_width, color='red', alpha=0.5, label='SD')

    # Set y-axis tick positions and labels
    ax.set_yticks(bar_positions)
    ax.set_yticklabels(regions)

    # Set labels and title
    ax.set_xlabel('Total Balance')
    ax.set_ylabel('Region')
    ax.set_title('Region / Balance - RD vs SD')

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()


def plot_dependency_employement_type_balance(RD, SD, employment_type):
    # Filter data based on the given employment type
    RD_filtered = RD[RD['Employment_Type'] == employment_type]
    SD_filtered = SD[SD['Employment_Type'] == employment_type]

    # Get balance values for RD and SD
    RD_balance = RD_filtered['Balance']
    SD_balance = SD_filtered['Balance']

    # Create subplots
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot RD balance
    ax.hist(RD_balance, bins=30, color='blue', alpha=0.5, label='Real Data')

    # Plot SD balance
    ax.hist(SD_balance, bins=30, color='red', alpha=0.5, label='Synthetic Data')

    # Set labels and title
    ax.set_xlabel('Balance')
    ax.set_ylabel('Frequency')
    ax.set_title(f'{employment_type} / Balance - Real Data vs Synthetic Data')

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()
