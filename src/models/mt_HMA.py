# --------------------------------------------------------------------------- #
#                                   IMPORT                                    #
# --------------------------------------------------------------------------- #

from sdv.multi_table import HMASynthesizer


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

    #Initialize the SDV model and fit it to the DataFrame:
    synthesizer.fit(datasets)

    # Generate synthetic data using the SDV model:
    return synthesizer.sample(scale=1)

# --------------------------------------------------------------------------- #
