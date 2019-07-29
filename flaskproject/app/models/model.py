from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '166d285b00c7c31afd5fc98b33fec846'

tmdb.language = 'en'
tmdb.debug = True

from tmdbv3api import Movie
movie = Movie()

def movieSearch(movieName):
    search = movie.search(movieName)
    
    return search[1].title