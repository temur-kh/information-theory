import os
import glob2
from math import log2
from collections import Counter

DATA_PATH = './data/'
DIRECTORIES = ('exe', 'pdf', 'doc', 'png', 'jpg')


def get_files(folder_path, file_type):
    file_paths = []
    regex = '*.{}'.format(file_type)
    regex_path = os.path.join(folder_path, regex)
    for file in glob2.glob(regex_path):
        file_paths.append(file)
    return file_paths


def calculate_entropy(probs):
    entropy = 0
    for prob in probs:
        entropy += prob * log2(1.0 / prob)
    return entropy


def evaluate_entropy(file_path):
    with open(file_path, 'rb') as file:
        bytes_list = file.read()
        cnt = Counter(bytes_list)
        total_bytes = len(bytes_list)
        probs = []
        for byte, count in cnt.most_common():
            prob = count * 1.0 / total_bytes
            probs.append(prob)
        entropy = calculate_entropy(probs)
    return entropy


def evaluate_entropies(file_paths, file_type):
    print("Evaluating average entropy for {} files of type {}".format(len(file_paths), file_type))
    entropies = []
    for file_path in file_paths:
        entropy = evaluate_entropy(file_path)
        entropies.append(entropy)
    print("Entropies per file:", entropies)
    avg_entropy = sum(entropies) / len(entropies)
    print("Average Entropy for files of type {}: {}".format(file_type, avg_entropy))


if __name__ == "__main__":
    for dir in DIRECTORIES:
        print("Files of type {}".format(dir))
        folder_path = os.path.join(DATA_PATH, dir)
        file_type = dir
        file_paths = get_files(folder_path, file_type)
        evaluate_entropies(file_paths, file_type)
        print()

