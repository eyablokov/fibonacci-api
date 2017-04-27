#!/usr/bin/env python3

def generate_sequence(size):
    sequence = [0, 1]
    if size < 3:
        return sequence[0: size]
    for index in range(2, size):
        sequence.append(sequence[index - 2] + sequence[index - 1])
    return sequence
