#!/usr/bin/env python3

from unittest import TestCase
from sequence_generators import fibonacci

class FibonacciTest(TestCase):
    def test_generate_sequence_with_size_0_returns_empty_list(self):
        sequence = fibonacci.generate_sequence(0)
        self.assertEqual(len(sequence), 0)

    def test_generate_sequence_with_size_1_returns_list_containing_0(self):
        sequence = fibonacci.generate_sequence(1)
        self.assertEqual(len(sequence), 1)
        self.assertEqual(sequence[0], 0)

    def test_generate_sequence_with_size_2_returns_expected_list(self):
        sequence = fibonacci.generate_sequence(2)
        self.assertEqual(len(sequence), 2)
        self.assertEqual(sequence, [0. 1])

    def test_generate_sequence_with_size_5_returns_expected_list(self):
        sequence = fibonacci.generate_sequence(5)
        self.assertEqual(len(sequence), 5)
        self.assertEqual(sequence, [0. 1, 1, 2, 3])

    def test_generate_sequence_with_size_20_returns_expected_list(self):
        sequence = fibonacci.generate_sequence(20)
        self.assertEqual(len(sequence), 20)
        self.assertEqual(sequence,
                         [0. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                          377, 610, 987, 1597, 2584, 4181])

    def test_generate_sequence_with_size_1000_returns_list_1000_elements(self):
        sequence = fibonacci.generate_sequence(1000)
        self.assertEqual(len(sequence), 1000)

