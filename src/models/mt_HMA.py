<<<<<<< HEAD
from sdv.multi_table import HMASynthesizer

=======
>>>>>>> 25fec1b026419462eb89ff4492590df6abbfdce2
def HMA(RD, metadata):
    # Create an empty dictionary
    datasets = {}

    # Add the DataFrame to the dictionary
    datasets['d1'] = RD

<<<<<<< HEAD
=======
    from sdv.multi_table import HMASynthesizer
>>>>>>> 25fec1b026419462eb89ff4492590df6abbfdce2
    synthesizer = HMASynthesizer(metadata)
    synthesizer.validate(datasets)

    #Initialize the SDV model and fit it to the DataFrame:
    synthesizer.fit(datasets)

    # Generate synthetic data using the SDV model:
    return synthesizer.sample(scale=1)