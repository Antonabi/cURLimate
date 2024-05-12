def end():
    sequence = "\033[0m"
    return sequence

def clear():
    sequence = "\033[2J\033[3J\033[H"
    return sequence

class colors:
    MAGENTA = "\u001b[35m"
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def magenta(text):
    return colors.MAGENTA + text + colors.ENDC

def header(text):
    return colors.HEADER + text + colors.ENDC

def okblue(text):
    return colors.OKBLUE + text + colors.ENDC

def okcyan(text):
    return colors.OKCYAN + text + colors.ENDC

def okgreen(text):
    return colors.OKGREEN + text + colors.ENDC

def warning(text):
    return colors.WARNING + text + colors.ENDC

def fail(text):
    return colors.FAIL + text + colors.ENDC

def bold(text):
    return colors.BOLD + text + colors.ENDC

def underline(text):
    return colors.UNDERLINE + text + colors.ENDC