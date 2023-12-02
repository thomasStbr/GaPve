from googlesearch import search
from itertools import islice

query = "amd.com"

# Set the number of results you want
num_results = 10

for url in islice(search(query), num_results):
    print(url)
