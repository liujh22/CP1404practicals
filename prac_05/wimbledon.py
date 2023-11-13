"""
Read .csv file and generate summary
"""

FILENAME = "wimbledon.csv"


def main():
    data = read_data(FILENAME)
    champions, countries = process_data(data)
    display_data(champions, countries)

champion_to_count
country_list
def display_data(champion, country):
    print(f"Wimbledon Champions:")
    print(f"{champion} {}")