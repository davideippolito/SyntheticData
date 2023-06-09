# --------------------------------------------------------------------------- #
#                                   IMPORT                                    #
# --------------------------------------------------------------------------- #

import pandas as pd


# --------------------------------------------------------------------------- #
#                                  FUNCTIONS                                  #
# --------------------------------------------------------------------------- #

def calculate_statistics(dataset):
    stats = {}
    stats['Mean'] = {
        'Balance': dataset['Balance'].mean(),
        'Credit_Score': dataset['Credit_Score'].mean()
    }
    stats['Std'] = {
        'Balance': dataset['Balance'].std(),
        'Credit_Score': dataset['Credit_Score'].std()
    }
    return stats

def compare_statistics(dataset1_stats, dataset2_stats):
    # Create an empty comparison DataFrame
    comparison_df = pd.DataFrame(columns=['Statistic', 'RD_Balance', 'SD_Balance', 'RD_Credit_Score', 'SD_Credit_Score'])
    # Iterate over the statistics and populate the comparison DataFrame
    for statistic in dataset1_stats:
        dataset1_balance = dataset1_stats[statistic]['Balance']
        dataset2_balance = dataset2_stats[statistic]['Balance']
        dataset1_credit_score = dataset1_stats[statistic]['Credit_Score']
        dataset2_credit_score = dataset2_stats[statistic]['Credit_Score'] 
        comparison_df.loc[len(comparison_df)] = [statistic, dataset1_balance, dataset2_balance, dataset1_credit_score, dataset2_credit_score]
    return comparison_df

# --------------------------------------------------------------------------- #
