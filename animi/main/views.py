from django.shortcuts import render
import random
import requests
from django.views.generic import TemplateView


def main_page(request):
    url_banner = "https://kodikapi.com/list?token=71d163b40d50397a86ca54c366f33b72&types=anime-serial,anime&sort=created_at&year=2023&limit=10&order=desc&with_material_data=true"
    url_updates = "https://kodikapi.com/list?token=71d163b40d50397a86ca54c366f33b72&types=anime-serial,anime&sort=updated_at&year=2023&with_material_data=true"
    url_popular = "https://kodikapi.com/list?token=71d163b40d50397a86ca54c366f33b72&types=anime-serial,anime&sort=imdb_ratingt&with_material_data=true"

    response_banner = requests.get(url_banner)
    response_updates = requests.get(url_updates)
    response_popular = requests.get(url_popular)

    data_banner = response_banner.json().get('results', [])
    data_updates = response_updates.json().get('results', [])
    data_popular = response_popular.json().get('results', [])

    banner = []
    updates = []
    populars = []

    banner_set = set()
    updates_set = set()
    populars_set = set()

    for result in data_banner:
        title = result.get('title', '')
        year = result.get('year', '')
        poster_url = result.get('material_data', {}).get('poster_url', '')
        screenshots = result.get('screenshots', [])
        random_screenshot = random.choice(screenshots) if screenshots else None
        rating = result.get('material_data', {}).get('shikimori_rating', '')
        genre = ', '.join(result.get('material_data', {}).get('anime_genres', []))
        description = result.get('material_data', {}).get('description', '')

        if rating == 0:
            rating = 'N/A'

        if title not in banner_set:
            banner_set.add(title)
            banner.append({'title': title, 'year': year, 'poster_url': poster_url, 'rating': rating,
                           'screenshot': random_screenshot, 'genre': genre, 'description': description})

    for result in data_updates:
        title = result.get('title', '')
        year = result.get('year', '')
        poster_url = result.get('material_data', {}).get('poster_url', '')
        rating = result.get('material_data', {}).get('shikimori_rating', '')

        if rating == 0:
            rating = 'N/A'

        if title not in updates_set:
            updates_set.add(title)
            updates.append({'title': title, 'year': year, 'poster_url': poster_url, 'rating': rating})

    for result in data_popular:
        title = result.get('title', '')
        year = result.get('year', '')
        poster_url = result.get('material_data', {}).get('poster_url', '')
        rating = result.get('material_data', {}).get('shikimori_rating', '')

        if rating == 0:
            rating = 'N/A'

        if title not in populars_set:
            populars_set.add(title)
            populars.append({'title': title, 'year': year, 'poster_url': poster_url, 'rating': rating})

    if banner:
        banner[2]['active'] = 'active'

    return render(request, 'main/main_page.html', {'updates': updates, 'populars': populars, 'banner': banner})


def player_page(request, pk):
    url = f'https://kodikapi.com/search?token=71d163b40d50397a86ca54c366f33b72&types=anime,anime-serial&limit=1&title={pk}&with_material_data=true'
    response = requests.get(url)
    data = response.json().get('results', [])

    anime_data = []
    anime_set = set()

    for result in data:
        title = result.get('title', '')
        year = result.get('year', '')
        poster_url = result.get('material_data', {}).get('poster_url', '')
        screenshots = result.get('screenshots', [])
        rating = result.get('material_data', {}).get('shikimori_rating', '')
        genre = ', '.join(result.get('material_data', {}).get('anime_genres', []))
        description = result.get('material_data', {}).get('description', '')
        duration = result.get('material_data', {}).get('duration', '')
        kodik_player = result.get('link', '')

        if rating == 0:
            rating = 'N/A'

        if title not in anime_set:
            anime_set.add(title)
            anime_data.append(
                {'title': title, 'year': year, 'poster_url': poster_url, 'rating': rating, 'screenshots': screenshots,
                 'genre': genre, 'description': description, 'duration': duration, 'player': kodik_player})

    return render(request, 'main/player_page.html', {'anime_data': anime_data})


def genres_page(request, pk):
    url = f'https://kodikapi.com/list?token=71d163b40d50397a86ca54c366f33b72&types=anime,anime-serial&anime_genres={pk}&with_material_data=true'
    response = requests.get(url)
    data = response.json().get('results', [])

    genre = pk

    anime_data = []
    anime_set = set()

    for result in data:
        title = result.get('title', '')
        year = result.get('year', '')
        poster_url = result.get('material_data', {}).get('poster_url', '')
        rating = result.get('material_data', {}).get('shikimori_rating', '')

        if rating == 0:
            rating = 'N/A'

        if title not in anime_set:
            anime_set.add(title)
            anime_data.append({'title': title, 'year': year, 'poster_url': poster_url, 'rating': rating})

    return render(request, 'main/genres_page.html', {'anime_data': anime_data, 'genre_name': genre})


def search_page(request, pk):
    url = f'https://kodikapi.com/search?token=71d163b40d50397a86ca54c366f33b72&title={pk}&types=anime,anime-serial&with_material_data=true'
    response = requests.get(url)
    data = response.json().get('results', [])

    search_title = pk

    anime_data = []
    anime_set = set()

    for result in data:
        title = result.get('title', '')
        year = result.get('year', '')
        poster_url = result.get('material_data', {}).get('poster_url', '')
        rating = result.get('material_data', {}).get('shikimori_rating', '')

        if rating == 0:
            rating = 'N/A'

        if title not in anime_set:
            anime_set.add(title)
            anime_data.append({'title': title, 'year': year, 'poster_url': poster_url, 'rating': rating})

    return render(request, 'main/search_page.html', {'anime_data': anime_data, 'search_title': search_title})


class AdsTxtView(TemplateView):
    template_name = 'ads.txt'
    content_type = 'text/plain'