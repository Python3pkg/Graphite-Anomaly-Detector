from detector import SpikeDetector
from pylab import show, plot

import numpy

def plot_data(original_data, processed_data, results):
    """Plots results for timeseries"""
    mean = numpy.mean(SpikeDetector._get_local_maxima(original_data[1]))

    r_t, r_d = [], []
    for t, v in results:
        r_t.append(t)
        r_d.append(v)

    start = original_data[0][0]
    end = original_data[0][-1]

    plot(processed_data[0], processed_data[1],
         r_t, r_d, "rs",
         original_data[0], original_data[1], "g",
         [start, end], [mean, mean], "r")

    show()


