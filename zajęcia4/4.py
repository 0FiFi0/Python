import csv
import statistics
import webbrowser
import random

yr = "2002"
sets_in_year = []
set_urls = []

with open('sets.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row["year"] == yr:
            sets_in_year.append(int(row["num_parts"]))
            set_urls.append(row["img_url"])
print(sets_in_year)
print(len(sets_in_year))
print(statistics.median(sets_in_year))
print(statistics.mean(sets_in_year))
url = random.choice(set_urls)
webbrowser.open(url)




