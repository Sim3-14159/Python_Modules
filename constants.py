from types import MappingProxyType
import keyword

class _ConstantsMeta(type):
    def __setattr__(cls, key, value):
        if key in cls.__dict__:
            raise AttributeError(f"Cannot overwrite existing attribute '{key}'")
        if key in cls._constants or key in cls._mutable_constants:
            raise AttributeError(f"Cannot modify constant '{key}'.")
        if key in {"_constants", "_mutable_constants"}:
            raise AttributeError("Cannot overwrite internal constants!")
        super().__setattr__(key, value)

        
class Constants(metaclass=_ConstantsMeta):
    _mutable_constants = {}
    _constants = MappingProxyType(_mutable_constants)
    
    def __init__(self):
        raise ValueError("Hey! No trying to access private data through an instance.")

    @classmethod
    def new(cls, name, value):
        if not isinstance(name, str):
            raise ValueError("Key must be a string")
        
        if not name.isidentifier() or keyword.iskeyword(name):
            raise NameError(f"'{name}' is not a valid Python variable name")
        
        if name in cls._mutable_constants:
            raise ValueError(f"The Constant '{name}' is already defined and immutable")
        
        cls._mutable_constants[name] = value

        
    @classmethod
    def get(cls, name):
        if name not in cls._constants:
            raise KeyError(f"The Constant '{name}' is not defined")
        return cls._constants[name]
    
    @classmethod
    def all(cls):
        return cls._constants



