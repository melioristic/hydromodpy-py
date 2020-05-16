import numpy as np

class GOF(object):

    """
    Good of Fitneess are used to compare simulation with observations. GOF methods include, mean error, percent bias, mean absolute error, root mean square error, Nash Shutcliffe Efficiency and Index of Agreement.

    Attributes:
        simulation(numpy.ndarray) : Simulation from a model
        observation(numpy.ndarray) : Observation or ground truth

    """
    def __init__(self, sim:np.ndarray, obs:np.ndarray):
        self.simulation = sim
        self.observation = obs

    def mean_error(self):
        return np.mean(self.observation-self.simulation)

    def percent_bias(self):
        return 100*(np.mean(self.simulation)-np.mean(self.observation))/np.mean(self.observation)

    def mean_absolute_error(self):
        return np.mean(np.abs(self.observation-self.simulation))

    def root_mean_square_error(self):
        return np.sqrt(np.mean(np.square(self.observation-self.simulation)))

    def nash_shutcliffe_efficiency(self):
        numerator = np.sum(np.square(self.observation-self.simulation))
        denominator = np.sum(np.square(self.observation-np.mean(self.observation)))
        return 1-numerator/denominator

    def index_of_agreement(self):
        numerator = np.sum(np.square(self.observation-self.simulation))
        denominator = np.sum(np.square(
            (np.abs(self.simulation-np.mean(self.simulation)))+(np.abs(self.observation-np.mean(self.observation)))))

        return 1-numerator/denominator