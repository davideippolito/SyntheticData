# --------------------------------------------------------------------------- #
#                                   IMPORT                                    #
# --------------------------------------------------------------------------- #

from sdv.single_table import CTGANSynthesizer

# --------------------------------------------------------------------------- #
#                                    MODEL                                    #
# --------------------------------------------------------------------------- #

def CTGAN(RD, metadata_st):
    synthesizer = CTGANSynthesizer(
        metadata_st,
        epochs=10,
        verbose=True
    )
    
    #Initialize the SDV model and fit it to the DataFrame:
    synthesizer.fit(RD)
    synthetic_data = synthesizer.sample(1)
    
    # Generate synthetic data using the SDV model:
    return synthetic_data

# --------------------------------------------------------------------------- #
