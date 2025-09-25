import numpy as np
import matplotlib.pyplot as plt
import ROOT as r

# we need to generate four plots
#____________________________________________________________________________________
# create a histogram of our data 
def make_histogram2d(h_name, h_title, data_x, data_y, nbins=100, x_range=[50., 150.], y_range=[50., 150.]):
    
    h2d = r.TH2D(h_name, h_title, nbins, x_range[0], x_range[1], nbins, y_range[0], y_range[1])
    
    for xy in np.stack((data_x, data_y), axis=-1):
        h2d.Fill(xy[0], xy[1])

    return h2d 
#____________________________________________________________________________________

npts = 100000

x0    = 50.
x1    = 150.
mean  = 100. 
sigma = 6.
int nbins = 100 

x_test = np.random.uniform(x0, x1, 10)
y_test = np.random.uniform(x0, x1, 10)

for xy in np.stack((x_test, y_test), axis=-1):
    print("x/y: ", xy[0], "/", xy[1])

exit()


# standard gaussian
pts_gauss_x = np.random.normal(mean, sigma, npts)
pts_gauss_y = np.random.normal(mean, sigma, npts)

h_gauss = make_histogram2d("h", "gauss", pts_gauss_x, pts_gauss_y, nbins, [x0,x1], [x0,x1])


# gaussian with offset
x_range = [50., 150.]
pts_uniform_x = np.random.uniform(x0, x1, npts)
pts_uniform_y = np.random.uniform(x0, x1, npts)
pts_offset_x  = np.concatenate((pts_gauss_x, pts_uniform_x))
pts_offset_y  = np.concatenate((pts_gauss_y, pts_uniform_y))

h_offset = make_histogram2d("h_offset", "gauss + offset", pts_offset_x, pts_offset_y, nbins, [x0,x1], [x0,x1])


# create a histogram with a 1/xx background
pts_uniform_x = np.random.uniform(0., 1., 6*npts)
pts_uniform_y = np.random.uniform(0., 1., 6*npts)

pts_1xx_offset_x = ( (1./xmin) - ((1./xmin) - (1./xmax))*pts_uniform_x )**(-1)
pts_1xx_offset_y = ( (1./xmin) - ((1./xmin) - (1./xmax))*pts_uniform_y )**(-1)

pts_1xx_x = np.concatenate((pts_gauss_x, pts_1xx_offset_x))
pts_1xx_y = np.concatenate((pts_gauss_y, pts_1xx_offset_y))

h_1xx = make_histogram("h_1xx", "gauss + 1/x^{2}", pts_1xx_x, pts_1xx_y, bins, [x0,x1], [x0,x1])


# create a histogram with a gaussain background
pts_gauss_bg_x = np.concatenate((pts_gauss_x, np.random.normal(mean, sigma*6, npts))) 
pts_gauss_bg_y = np.concatenate((pts_gauss_y, np.random.normal(mean, sigma*6, npts)))

h_gauss_bg = make_histogram("h_gbg", "gauss + gauss background (6#sigma)", pts_gauss_bg_x, pts_gauss_bg_y, bins, [x0,x1], [x0,x1])


plt.show()