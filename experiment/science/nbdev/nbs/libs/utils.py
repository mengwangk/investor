def is_lib_exists(name):
    import importlib
    lib = importlib.util.find_spec(name)
    return lib is not None