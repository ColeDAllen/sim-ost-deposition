#!/usr/bin/env python

import numpy as np

default_shape = (41, 21)
default_gauss = 0.005
default_temper = 0.6
default_threshold = 6.0


# shape: (int, int) = default_shape: we are adding a method parameter "shape" of type tuple (int, int), defaulting to default_shape
class BiasMap:
    def __init__(self, fe_surface: np.ndarray, shape: (int, int) = default_shape, gauss: float = 0.005, temper: float = 0.6, threshold: float = 6.0):
        self.shape = shape
        self.init_gauss = gauss
        self.curr_gauss = gauss
        self.temper = temper
        self.threshold = threshold
        self.bias_counts = np.zeros(shape)
        # self.fe_surface is likely going to be an array which holds the height of our "true" unbiased FE surface.
        self.fe_surface = fe_surface

    def add_bias(self) -> (int, int):
        # Adds a bias to self.bias_counts, and returns (lam index, dUdL index) in case it's needed.
        # Can remove that by eliminating the -> (int, int) bit.
        return (0, 0)


def gen_fe_surface() -> np.ndarray:
    # In here, logic to define the FE surface.
    # I'll see about copying one of our pre-existing 2D PMF files.
    pass


# In my actual jobs: 1 million depositions. Likely reduce this for dev/testing
num_iterations = 1000000
bias_map = BiasMap(gen_fe_surface())

for i in range(num_iterations):
    bias_map.add_bias()
    pass
    # This would be the main loop: deposit a bias, etc.

# Output the contents of bias_map as preferred and/or use Matplotlib to plot it.
