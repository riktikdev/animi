from fastapi import FastAPI, HTTPException, Query
import json
import random

app = FastAPI(
    title='AniMi API'
)


def filter_title(title, search_query, year_filter, genres_filter):
    if search_query:
        # Поиск по имени или описанию
        titles = title.get('titles')
        description = title.get('description')
        if titles and titles.get('ru') and search_query.lower() in titles['ru'].lower():
            return True
        if description and search_query.lower() in description.lower():
            return True

    if year_filter is not None:
        # Фильтр по году выхода
        if title.get('year') == year_filter:
            return True

    if genres_filter:
        # Фильтр по жанрам
        genres = [genre.strip().lower() for genre in genres_filter.split(',')]
        if any(genre in title['genres'].lower() for genre in genres):
            return True

    return False


def load_data():
    with open('data.json', 'r', encoding='utf-8') as file:
        return json.load(file)


@app.get('/title')
async def get_title(id: int = Query(None), code: str = Query(None)):
    if id is None and code is None:
        raise HTTPException(status_code=400, detail='Please provide either "id" or "code" parameter')

    data = load_data()

    if id is not None:
        for title in data:
            if title['id'] == id:
                return {'status': 200, 'data': title}

    if code is not None:
        for title in data:
            if title['code'] == code:
                return {'status': 200, 'data': title}

    raise HTTPException(status_code=404, detail='Title not found')


@app.get('/title/random')
async def get_random():
    data = load_data()

    if data:
        random_title = random.choice(data)
        return {'status': 200, 'data': random_title}

    raise HTTPException(status_code=404, detail='No titles found')


@app.get('/title/search')
async def search_title(search: str = Query(None), year: int = Query(None), genres: str = Query(None),
                       limit: int = Query(None)):
    data = load_data()
    filtered_titles = [title for title in data if filter_title(title, search, year, genres)]

    if not filtered_titles:
        raise HTTPException(status_code=404, detail='No matching titles found')

    if limit is not None and limit > 0:
        filtered_titles = random.sample(filtered_titles, min(limit, len(filtered_titles)))

    return {'status': 200, 'data': filtered_titles}
