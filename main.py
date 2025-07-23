import random
import pandas as pd
from bcolors import BColors
import sys

length = len(sys.argv)
args = sys.argv
category = ""

if length == 3:
    category = args[2]
elif length == 2:
    print()
    flag = args[1]
    if (flag != "--category"):
        print("Supply the --category flag!")
    elif (flag == "--category"):
        print("Supply the category for the --category flag!")
        print("Like this:")
        print("--category Job_Board")
        print("--category Industry")
    sys.exit()
elif length == 1:
    print("Use the program like this:")
    print("python .\\main.py --category Job_Boards")
    print("python .\\main.py --category Industries")
    sys.exit()

search_message = "Search for IT jobs in ->"

match category:
    case "Job_Board":
        df = pd.read_csv("./data/jobs_boards.csv")
        job_boards_series = df["Job_Boards"]
        job_boards = job_boards_series.to_list()
        job_board = random.choice(job_boards)

        df = pd.read_csv("./data/states.csv")
        states_series = df["States"]
        states = states_series.to_list()
        state = random.choice(states)
        print(search_message)
        print("Job Board: " + BColors.LIGHT_CYAN + job_board + BColors.END)
        print("State: " + state)
    case "Industry":
        df = pd.read_csv("./data/industries.csv")
        industries_series = df["Industries"]
        industries = industries_series.to_list()
        industry = random.choice(industries)
        print(search_message)
        print("Industry: " + BColors.LIGHT_RED + industry + BColors.END)
    case _:
        print("Error: category not in categories!")