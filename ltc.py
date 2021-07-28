#!/usr/bin/env python3

# This script generates a list of LTC municipalities based on a
# list for a tour and lists of targets for each rider on the tour
#
# Rider data is provided in a file with the rider name
# Tour data is provided in a file indicated by a tour argument

import argparse


parser = argparse.ArgumentParser(description="Compare LTC tour with LTC target lists")
parser.add_argument(
    "--tour",
    dest="tour",
    type=argparse.FileType('r', encoding='utf-8'),
    required=True,
    help="File containing the tour municipalities",
)
parser.add_argument(
    "--riders",
    dest="riders",
    type=lambda arg: arg.split(','),
    required=True,
    help="Filenames of the riders partaking in the tour",
)


def main():
    args = parser.parse_args()

    tour_ms = set([s.rstrip() for s in args.tour.readlines()])

    riders_ms = {}
    targets_ms = {}
    for rider in args.riders:
        with open(rider, 'r') as r:
            riders_ms[rider] = set([s.rstrip() for s in r.readlines()])
        targets_ms[rider] = sorted(tour_ms.intersection(riders_ms[rider]))

    print("New tour municipalities for riders")

    for rider in args.riders:
        count = len(targets_ms[rider])
        print(f"{rider}: ({count}) {targets_ms[rider]}")


if __name__ == '__main__':
    main()
