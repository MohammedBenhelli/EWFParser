import yaml

# Declare a global variable to hold the cached constants
_CACHED_CONSTANTS = None


def load_constants(config: str = ''):
    global _CACHED_CONSTANTS
    if _CACHED_CONSTANTS is None:
        with open(config) as file:
            _CACHED_CONSTANTS = yaml.load(file, Loader=yaml.FullLoader)
    return _CACHED_CONSTANTS
