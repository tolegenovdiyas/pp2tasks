movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
'''
def imdb_movie(movie):
    imdb_score = movie.get('imdb', 0)
    return imdb_score > 5.5

for movie in movies:
    result = imdb_movie(movie)
    print(f"{movie['name']} - Is score of IMDB more than 5.5? {result}")
'''
#2
'''
def more_movies(movies):
    good_movies = [movie for movie in movies if movie.get('imdb', 0) > 5.5]
    return good_movies
good_movies = more_movies(movies)
for movie in good_movies:
    print(f"{movie['name']} - IMDB Score: {movie['imdb']}")
'''
#3
'''
def get_movies_by_category(movies, category_name):
    category_movies = [movie for movie in movies if movie.get('category', '').lower() == category_name.lower()]
    return category_movies

category_name = "romance"
romance_movies = get_movies_by_category(movies, category_name)
print(f"Movies in the {category_name} category:")
for movie in romance_movies:
    print(f"{movie['name']} - IMDB Score: {movie['imdb']}")
'''
#4
'''
def calculate_average_imdb_score(movies):
    imdb_scores = list(map(lambda movie: movie.get('imdb', 0), movies))
    valid_scores = list(filter(lambda score: score > 0, imdb_scores))
    
    if valid_scores:
        average_score = sum(valid_scores) / len(valid_scores)
        return average_score
    else:
        return 0.0
    
average_score = calculate_average_imdb_score(movies)
print(f"Average IMDB score for the movies: {average_score:.2f}")    
'''
#5
'''
def calculate_average_imdb_score_by_category(movies, category_name):
    category_movies = [movie for movie in movies if movie.get('category', '').lower() == category_name.lower()]
    if not category_movies:
        return 0.0

    imdb_scores = [movie.get('imdb', 0) for movie in category_movies]
    valid_scores = [score for score in imdb_scores if score > 0]

    if valid_scores:
        average_score = sum(valid_scores) / len(valid_scores)
        return average_score
    else:
        return 0.0
category_name = "romance"
average_score = calculate_average_imdb_score_by_category(movies, category_name)
print(f"Average IMDB score for {category_name} movies: {average_score:.2f}")
'''