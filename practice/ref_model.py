#!/usr/bin/env python3
"""Reference model for the MAC unit: computes the correct answers in software.

Each output line is one clock cycle of input plus the expected accumulator:

    clr en a b expected

Usage:
    python3 ref_model.py random [--seed N]   # 8 dot products of 25 terms
    python3 ref_model.py overflow            # one dot product of 1,152 terms
    python3 ref_model.py overflow --chunk 511
"""

import argparse

ACC_MAX = 2**23 - 1   # 24-bit signed accumulator
ACC_MIN = -2**23


class XorShift32:
    """A tiny random number generator, so the same seed gives the same
    vectors on every computer and every Python version."""

    def __init__(self, seed):
        self.state = seed or 1

    def next(self):
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= x >> 17
        x ^= (x << 5) & 0xFFFFFFFF
        self.state = x
        return x

    def int8(self):
        # One value in four is an edge value, the rest are uniform.
        if self.next() % 4 == 0:
            return [-128, -1, 0, 1, 127][self.next() % 5]
        return self.next() % 256 - 128


def model(ops, saturate):
    """What the accumulator should hold after each operation."""
    acc = 0
    for clr, en, a, b in ops:
        if clr:
            acc = 0
        elif en:
            acc += a * b
            if saturate:
                acc = max(ACC_MIN, min(ACC_MAX, acc))
        yield acc


def random_ops(seed, dots=8, terms=25):
    rng = XorShift32(seed)
    for _ in range(dots):
        yield (1, 0, 0, 0)
        for _ in range(terms):
            yield (0, 1, rng.int8(), rng.int8())


def overflow_ops(terms=1152, chunk=None):
    # A bright patch of image (activation 100) meets a large weight (100).
    yield (1, 0, 0, 0)
    for i in range(terms):
        if chunk and i and i % chunk == 0:
            yield (1, 0, 0, 0)
        yield (0, 1, 100, 100)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("test", choices=["random", "overflow"])
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--chunk", type=int, default=None)
    args = parser.parse_args()

    if args.test == "random":
        ops = list(random_ops(args.seed))
    else:
        ops = list(overflow_ops(chunk=args.chunk))
    for (clr, en, a, b), expected in zip(ops, model(ops, saturate=True)):
        print(clr, en, a, b, expected)


if __name__ == "__main__":
    main()
