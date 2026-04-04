#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Proqramın adını (index 0) siyahıdan çıxarırıq
    count = len(argv)

    # Birinci hissə: arqumentlərin sayını və düzgün sonluğu çap edirik
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))

    # İkinci hissə: hər bir arqumenti öz mövqeyi ilə çap edirik
    for i in range(count):
        print("{:d}: {}".format(i + 1, argv[i]))
