import baselines.run as openai_baselines
from ..policy_interface import PolicyInterface


class OpenAIBaselinesPolicy(PolicyInterface):

    def __init__(
            self,
            policy_name : str,
            **kwargs
    ):
        pass

    def train(
            self
    ):
        pass

    def step(
            self
    ):
        pass
