import numpy as np

class MonteCarlo:
    def __init__(self, num_simulations):
        self.num_simulations = num_simulations
        self.results = []

    def run_simulation(self, func, *args, **kwargs):
        for _ in range(self.num_simulations):
            result = func(*args, **kwargs)
            self.results.append(result)
        return self.results

    def calculate_mean(self):
        return np.mean(self.results)

    def calculate_std_dev(self):
        return np.std(self.results)