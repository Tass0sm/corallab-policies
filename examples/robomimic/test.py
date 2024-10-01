# import functools
# from datetime import datetime
# import matplotlib.pyplot as plt

from corallab_lib import Gym

from corallab_policies import Policy



# env_name = "ant"
# gym = Gym(env_name, backend="brax")


config_file_path = "/home/tassos/phd/research/robomimic/robomimic/exps/templates/bc.json"
dataset_path = "/home/tassos/phd/research/robomimic/datasets/can/ph/low_dim_v141.hdf5"

policy = Policy("nothing", backend="robomimic")

policy.train(config=config_file_path, dataset=dataset_path, debug=True)
