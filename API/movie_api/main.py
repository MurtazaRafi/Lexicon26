
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Part 1
movies = [
    {"id": 1, "title": "Dune", "director": "Frank Herbert", "year": 1965},
    {"id": 2, "title": "Neuromancer", "director": "William Gibson", "year": 1984},
    {"id": 3, "title": "The Hobbit", "director": "J.R.R. Tolkien", "year": 1937},
    {"id": 4, "title": "Foundation", "director": "Isaac Asimov", "year": 1951},
]

class Movie(BaseModel):
    title: str
    director: str
    year: int

def find_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    if director:
        return [movie for movie in movies if director.lower() in movie["director"].lower()]
    if year:
        return [movie for movie in movies if year == movie["year"]]
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)

@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {'id': new_id, 'title': movie.title, 'director': movie.director, 'year': movie.year}
    movies.append(new_movie)
    return new_movie

@app.put("/movies/{movie_id}")
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing['title'] = movie.title
    existing['director'] = movie.director
    existing['year'] = movie.year
    return existing


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    movies.remove(existing)

# Part 2

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, changes: MovieUpdate):
    movie = find_movie(movie_id)
    update_data = changes.model_dump(exclude_unset=True)

    for key, val in update_data.items():
        movie[key] = val

    return movie

# 3. 
# 422 and 404

# 4.
# Put for updating is needed for all the fields and patch for only some field