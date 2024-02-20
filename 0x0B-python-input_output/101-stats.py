#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


def print_stats(file_size, codes_metrics):
    """Print accumulated metrics.

    Args:
        file_size (int): The accumulated read file size.
        codes_metrics (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(file_size))
    for key in sorted(codes_metrics):
        print("{}: {}".format(key, codes_metrics[key]))


if __name__ == "__main__":
    import sys

    file_size = 0
    codes_metrics = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for line in sys.stdin:
            if c == 10:
                print_stats(file_size, codes_metrics)
                c = 1
            else:
                c += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if codes_metrics.get(line[-2], -1) == -1:
                        codes_metrics[line[-2]] = 1
                    else:
                        codes_metrics[line[-2]] += 1
            except IndexError:
                pass

        print_stats(file_size, codes_metrics)

    except KeyboardInterrupt:
        print_stats(file_size, codes_metrics)
        raise
