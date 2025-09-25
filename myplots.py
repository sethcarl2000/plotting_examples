import numpy as np
import matplotlib.pyplot as plt

# we need to generate four plots

#____________________________________________________________________________________
# create a histogram of our data 
def make_histogram(subplot, data, nbins=100, x_range=[50., 150.], yaxis_log=False):
    
    counts_x, all_bins = np.histogram(data, nbins, x_range)

    #trim off the last bin from the histogram
    bins_x = all_bins[:len(all_bins)-1]

    y_errors = np.sqrt(counts_x)

    # set the y-axis to log-scale if needed
    if yaxis_log: 
        subplot.set_yscale("log", nonpositive='clip')

    subplot.errorbar(bins_x, counts_x, yerr=y_errors, marker='_', linestyle="none")

    return 
#____________________________________________________________________________________


npts = 10000

fig, ((h_basic, h_offset), (h_1_xx, h_double)) = plt.subplots(2,2, layout='constrained')


''', h_1_xx, h_double'''
# standard gaussian
rand_gauss = np.random.normal(100., 6., npts)

make_histogram(h_basic, rand_gauss)


# gaussian with offset
x_range = [50., 150.]
offset = np.random.uniform(x_range[0], x_range[1], npts)
rand_offset = np.concatenate((rand_gauss, offset))

make_histogram(h_offset, rand_offset)


# create a histogram with a 1/xx background
xx_uniform = np.random.uniform(0., 1., 6*npts)
xx_offset = ( (1./x_range[0]) - ((1./x_range[0]) - (1./x_range[1]))*xx_uniform )**(-1)
rand_1_xx = np.concatenate((rand_gauss, xx_offset))
make_histogram(h_1_xx, rand_1_xx)


# create a histogram with a gaussain background
gauss_background = np.random.normal(100., 24, int(npts/2))
make_histogram(h_double, np.concatenate((gauss_background, rand_gauss)))


plt.savefig("canvas2_py.pdf")

plt.show()