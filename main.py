from fastapi import FastAPI, Response, Query
from src.MangaReader import Mangareader


app = FastAPI()

mangareader_genres = ["Action", "Adventure", "Comedy", "Cooking", "Doujinshi", "Drama", "Erotica", "Fantasy", "Gender Bender", "Harem", "Historical", "Horror", "Isekai", "Josei", "Manhua", "Manhwa", "Martial arts", "Mature", "Mecha", "Medical", "Mystery", "One shot", "Pornographic", "Psychological", "Romance", "School life", "Sci fi", "Seinen", "Shoujo", "Shounen ai", "Slice of life", "Smut", "Sports", "Supernatural", "Tragedy", "Webtoons", "Yaoi", "Yuri"]

@app.get("/")
def homepage():
    return {
        "message": "Welcome to the Manga scraper, have fun scraping weebs"
    }

@app.get("/mangareader/{category}/{path:path}")
def mangareader(category: str, path: str):
    if category == "search":
        return Mangareader().search(query=path)
    elif category == "info":
        return Mangareader().info(id=path)
    elif category == "pages":
        pages = Mangareader().pages(id=path)
        return pages
    elif category == "genre-list":
        return {
            "endpoint": "mangareader",
            "genres": mangareader_genres
        }
    elif category == "latest":
        return Mangareader().latest(genre=path)
    else:
        return {
            "detail": "Invalid parameter"
        }

