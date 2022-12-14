from typing import TextIO


def get_input(day: int) -> TextIO:
    # return file input for day
    # file format is dayXX.txt in inputs folder
    return open(f"inputs/day{day:02}.txt", "r")


def get_list(day: int) -> list:
    # return list of lines from input file
    return get_input(day).readlines()
