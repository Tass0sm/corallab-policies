from .backend_manager import backend_manager

class Policy:
    def __init__(
            self,
            *args,
            backend=None,
            from_impl=None,
            **kwargs
    ):
        PolicyImpl = backend_manager.get_backend_attr(
            "PolicyImpl",
            backend=backend
        )

        if from_impl:
            self.policy_impl = PolicyImpl.from_impl(from_impl, *args, **kwargs)
        else:
            self.policy_impl = PolicyImpl(*args, **kwargs)

    def __getattr__(self, name):
        if hasattr(self.policy_impl, name):
            return getattr(self.policy_impl, name)
        else:
            # Default behaviour
            raise AttributeError
