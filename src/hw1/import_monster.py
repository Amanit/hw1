from importlib import import_module
from types import ModuleType
from typing import Callable, List, Union


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    """
    Import `method_name` from `modules` and if `method_name`
    is callable add it to `callable_methods`.

    `modules` is the list containing string or python Modules itself.
    Return list of `callable_methods`.
    """
    callable_methods = []
    for module in modules:
        if isinstance(module, str):
            try:
                mod = import_module(module)
            except ImportError:
                continue
        elif isinstance(module, ModuleType):
            mod = module
        else:
            raise TypeError(
                "Wrong Module type, module should be a string or a Python module."
            )
        method = getattr(mod, method_name, None)
        if callable(method):
            callable_methods.append(method)

    return callable_methods
