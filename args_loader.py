import argparse

def load_args():
    parser = argparse.ArgumentParser('Nas-Bench-Graph')
    parser.add_argument('--data', nargs='*', default = ['arxiv0'], type=str)
    parser.add_argument('--encode', choices = ['one_hot', 'category'], default = 'one_hot', help = 'encoding method for category variables')
    parser.add_argument('--data_type', choices = ['complete', 'short'], default = 'complete', help = 'use complete benchmarks or short look up tables')
    args = parser.parse_known_args()[0]
    return args