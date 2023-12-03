#!/usr/bin/env python3
import sys
from src.utils import *
from src.check_errors import *
from src.poll import *

if __name__ == '__main__':
    try:
        check_args(len(sys.argv), sys.argv)
        poll(sys.argv)
    except Exception as message:
        print(message, file=sys.stderr)
        sys.exit(84)
