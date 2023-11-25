import tmdbsimple as tmdb
from pprint import pprint

tmdb.API_KEY = "f29645dc692d15a6de6d45d24f7d776c"
tmdb.REQUESTS_TIMEOUT = (2, 5)  # seconds, for connect and read specifically

search = tmdb.Search()
search_response = search.movie(query="The Matrix")  # Response for search
print(search_response)  # get original_title and release_date

for i in search_response:
    print(search_response["results"][i]["release_date"], end=":")
    print(search_response["results"][i]["original_title"])

print(search_response["results"][0]["original_title"])