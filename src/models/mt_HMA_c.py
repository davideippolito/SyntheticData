# --------------------------------------------------------------------------- #
#                                   IMPORT                                    #
# --------------------------------------------------------------------------- #

from sdv.multi_table import HMASynthesizer

# External Functions
from utils.Constraints import *

# --------------------------------------------------------------------------- #
#                                    MODEL                                    #
# --------------------------------------------------------------------------- #

def HMA(RD, metadata):
    # Create an empty dictionary
    datasets = {}
    # Add the DataFrame to the dictionary
    datasets['d1'] = RD
    synthesizer = HMASynthesizer(metadata)
    synthesizer.validate(datasets)
    # # Add Constraints
    # synthesizer.add_constraints(constraints=[
    #         c_mt_dependency_balance_region,
    #         c_mt_dependency_balance_employment_type,
    #         c_mt_dependency_tot_transaction_amount_credit_score,
    #     ]
    # )

    synthesizer.load_custom_constraint_classes(
        filepath='utils/Constraints.py',
        class_names=['c_mt_dependency_balance_region']
    )
    synthesizer.load_custom_constraint_classes(
        filepath='utils/Constraints.py',
        class_names=['c_mt_dependency_balance_employment_type']
    )
    synthesizer.load_custom_constraint_classes(
        filepath='utils/Constraints.py',
        class_names=['c_mt_dependency_tot_transaction_amount_credit_score']
    )


    #Initialize the SDV model and fit it to the DataFrame:
    synthesizer.fit(datasets)
    # Generate synthetic data using the SDV model:
    return synthesizer.sample(scale=1)

# --------------------------------------------------------------------------- #
