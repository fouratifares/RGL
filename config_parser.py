import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=2)
parser.add_argument('--T', type=int, default=int(1e5))
parser.add_argument('--reps', type=int, default=20)
parser.add_argument('--k', type=int, default=4)
parser.add_argument('--sol', type=list, default=[2])


args, unknown = parser.parse_known_args()
