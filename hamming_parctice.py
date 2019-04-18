import random
import numpy as np
import pandas as pd

def hamming (a, b):
    return len([i for i in filter(lambda x: x[0] != x[1], zip(a,b))])




