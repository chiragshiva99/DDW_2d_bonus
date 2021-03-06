class MLRModel:
    def __init__(self):
        self.beta0 = -304.993
        self.beta1 = 0.216613
        self.beta2 = 336.0383
        self.beta3 = 0.02595


class LogRegModel:
    target_thres = 60

    def __init__(self):
        self.beta0 = 0.12889905
        self.beta1 = 0.17751605
        self.beta2 = -0.0794467
        self.beta3 = 1.18107464

        self.mean1 = -6.204714e-16
        self.sd1 = 1.0
        self.mean2 = 1.026061e-15
        self.sd2 = 1.0
        self.mean3 = -1.150812e-15
        self.sd3 = 1.0