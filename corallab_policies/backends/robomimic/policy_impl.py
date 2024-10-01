from argparse import Namespace

from robomimic.scripts.train import main as robomimic_train_main


class RobomimicPolicy:

    def __init__(
            self,
            policy_name : str,
            **kwargs
    ):
        pass

    def train(
            self,
            config=None,
            algo=None,
            name=None,
            dataset=None,
            debug=False
    ):
        """
        config: (optional) path to a config json that will be used to override the default settings. \
            If omitted, default settings are used. This is the preferred way to run experiments.
        algo: (optional) name of algorithm to run. Only needs to be provided if --config is not provided
        name: (optional) if provided, override the experiment name defined in the config
        dataset: (optional) if provided, override the dataset path defined in the config
        debug: set this flag to run a quick training run for debugging purposes
        """

        config = Namespace(config=config, algo=algo, name=name, dataset=dataset, debug=debug)
        robomimic_train_main(config)

    def step(
            self
    ):
        pass
