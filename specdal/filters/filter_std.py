from .split_good_bad import split_good_bad

def filter_std(collection,wavelength0,wavelength1,std_thresh,group='mean'):
    """Filter the spectra from collection who have a mean std that is greater
    than std_thresh times the mean std between wavelength0 and wavelength1
    group can be mean, median, max, min. min <-> all, max <-> any
    """
    #extract the relevant wavelength range
    data = collection.data.loc[wavelength0:wavelength1]
    mean = data.mean(axis=1)
    std = data.std(axis=1)
    #number of standard deviations from mean at each wavelength
    n_std = data.sub(mean,axis=0).div(std,axis=0).abs()

    if group == 'mean':
        good = n_std.mean() < std_thresh
    if group == 'median':
        good = n_std.median() < std_thresh
    if group == 'min':
        good = n_std.min() < std_thresh
    if group == 'max':
        good = n_std.min() < std_thresh
    #TODO: work around transposing
    return split_good_bad(collection,good)

