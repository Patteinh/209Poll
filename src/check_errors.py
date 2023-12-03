from src.utils import help

def check_args(ac, av):
    if ac == 2 and av[1] == "-h":
        help()
        exit(0)
    if ac != 4:
        raise Exception("ERROR: The number of arguments must be 4.")
    for arg in av[1:]:
        try:
            arg_value = float(arg)
        except ValueError:
            raise Exception("ERROR: The provided argument must be a number.")
        if arg_value < 0:
            raise Exception("ERROR: The provided argument must be positive numbers.")
