from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create the FastAPI app instance
app = FastAPI()

# Define the request/response model for a movie
class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int

# Dummy in-memory movie database
movies_db: List[Movie] = [
    Movie(id=1, title="The Shawshank Redemption", director="Frank Darabont", year=1994),
    Movie(id=2, title="The Godfather", director="Francis Ford Coppola", year=1972),
    Movie(id=3, title="Inception", director="Christopher Nolan", year=2010),
]

# Endpoint to list all movies
@app.get("/movies", response_model=List[Movie])
def list_movies():
    """Return all movies from the dummy database."""
    return movies_db

# Endpoint to add a new movie
@app.post("/movies", response_model=Movie, status_code=201)
def add_movie(movie: Movie):
    """Add a new movie to the dummy database."""
    # Check for duplicate movie ID before adding
    if any(existing_movie.id == movie.id for existing_movie in movies_db):
        raise HTTPException(status_code=400, detail="Movie with this ID already exists")

    movies_db.append(movie)
    return movie

# Endpoint to delete a movie by ID
@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    """Delete a movie from the dummy database by its ID."""
    for index, existing_movie in enumerate(movies_db):
        if existing_movie.id == movie_id:
            movies_db.pop(index)
            return

    # If the movie was not found, return 404
    raise HTTPException(status_code=404, detail="Movie not found")
