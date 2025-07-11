import random
import pandas as pd
from bcolors import BColors

categories = ["Job_Board", "Industries"]

# Make it so that there is a 20% chance of getting the Job_Board category
# and a 80% chance of getting the Industries category
sample_categories = random.sample(categories, counts=[2, 8], k = 10)
category = random.choice(sample_categories)

search_message = "Search for IT jobs in ->"

match category:
    case "Job_Board":
        df = pd.read_csv("./data/jobs_boards.csv")
        job_boards_series = df["Job_Boards"]
        job_boards = job_boards_series.to_list()
        job_board = random.choice(job_boards)
        print(search_message)
        print("Job Board: " + BColors.LIGHT_CYAN + job_board + BColors.END)
    case "Industries":
        df = pd.read_csv("./data/industries.csv")
        industries_series = df["Industries"]
        industries = industries_series.to_list()
        industry = random.choice(industries)
        print(search_message)
        print("Industry: " + BColors.LIGHT_RED + industry + BColors.END)
    case _:
        print("Error: category not in categories!")