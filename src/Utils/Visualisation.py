import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_region_balance_comparison(RD, SD):
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
    ax.set_title('Total Balance Comparison - RD vs SD')

    # Add legend
    ax.legend()

    # Show the plot
    plt.show()
