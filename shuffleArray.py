import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--seed", "-s", help="input seed")
parser.add_argument("--length", "-l", help="input array length")

args = parser.parse_args()
np.random.seed(int(args.seed))

arr = np.arange(int(args.length))
np.random.shuffle(arr)


print(arr+1)

print("The current array is generated with the following libraries:")
print("numpy version:", np.__version__)
print("argparse version:", argparse.__version__)
print("python version:", sys.version)
print("--------------------------------")
print("The first array, has been generated with the following libraries:")
print("numpy version: 1.19.5")
print("argparse version: 1.1")
print("python version: 3.9.1")
print("--------------------------------")