def getInput(day: int) -> str:
    # return file input for day
    # file format is dayXX.txt in inputs folder
    return open(f"inputs/day{day:02}.txt", "r")