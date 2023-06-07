from sdv.lite import SingleTablePreset

def FAST_ML(RD, metadata_st):

    synthesizer = SingleTablePreset(metadata_st, name='FAST_ML')

    #Initialize the SDV model and fit it to the DataFrame:
    synthesizer.fit(RD)

    # Generate synthetic data using the SDV model:
    return synthesizer.sample(scale=1)
