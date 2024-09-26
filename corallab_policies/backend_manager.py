from .backends import backend_list
import importlib
import types


class BackendManager:
    def __init__(self):
        self.backend = None
        self.backend_kwargs = {}
        self.backend_list = backend_list
        self.backend_dict = {}

    def register_backend(self, backend: str, module):
        self.backend_dict[backend] = module

    def set_backend(self, backend: str, **backend_kwargs):
        assert backend in self.backend_list
        self.backend = backend
        self.backend_kwargs = backend_kwargs

    def get_backend(self, backend=None):
        assert backend or self.backend is not None, "Need to select a backend!"

        if backend in self.backend_dict:
            return self.backend_dict[backend]

        if isinstance(backend, types.ModuleType):
            return backend
        else:
            try:
                return importlib.import_module(
                    "." + (backend or self.backend),
                    package="corallab_policies.backends"
                )
            except KeyError:
                raise Exception("Backend not found!")

    def get_backend_attr(self, attr, backend=None):
        backend_module = self.get_backend(backend=backend)
        return getattr(backend_module, attr)

    def get_backend_kwargs(self):
        return self.backend_kwargs

    def get_backend_kwarg(self, name):
        return self.backend_kwargs[name]



backend_manager = BackendManager()
