from sdv.single_table import CTGANSynthesizer

def CTGAN(RD, metadata_st):
    synthesizer = CTGANSynthesizer(metadata_st)
    
    #Initialize the SDV model and fit it to the DataFrame:
    synthesizer.fit(RD)

    # Generate synthetic data using the SDV model:
    return synthesizer.sample(scale=1)
