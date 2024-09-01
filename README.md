# MangaMiner
 A FastAPI application that integrates with MangaReader for manga scraping. It provides endpoints for searching, retrieving manga info, and fetching pages, along with a genre list and latest manga updates


# Manga Miner API

This is a FastAPI-based web application for scraping manga information from various sources including Manganato, Mangareader, Mangapill, and Asurascans.

![mangaminer](https://github.com/user-attachments/assets/3954d9e8-e5e9-40d1-978c-094dd61f7a15)


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/riy4z/MangaMiner.git
    cd MangaMiner-main
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:
    ```bash
    fastapi dev main.py
    ```


## API Endpoints

### Homepage
- **GET /**: Welcome message.
  ```json
  {
      "message": "Welcome to the Manga scraper, have fun scraping weebs"
  }

## Sources Supported
1. [Mangareader](https://mangareader.tv/)


### Mangareader
- **GET /mangareader/search/{path}**: Search manga by query.
- **GET /mangareader/info/{path}**: Get manga info by ID.
- **GET /mangareader/pages/{path}**: Get manga pages by ID.
- **GET /mangareader/genre-list**: Get the list of genres.
- **GET /mangareader/latest/{path}**: Get the latest manga by genre.


## Example Queries

- **Mangareader Search**: `GET /mangareader/search/jujutsu_kaisen`
- **Mangareader Latest by Genre**: `GET /mangareader/latest/Action`


## Responses

![image](https://github.com/user-attachments/assets/a627edcf-0225-4dab-8604-c6811e1d10b5)



## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
