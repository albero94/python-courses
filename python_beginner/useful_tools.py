import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename:str) -> str:
    return filename[filename.index(".") + 1:]

def roll_dice(num:int) -> int:
    return random.randint(1, num)