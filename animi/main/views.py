import requests
from django.shortcuts import render
import random
from time import perf_counter
from django.views.generic import TemplateView

base_image_url = 'https://anilibria.tv'


class AnilibriaParser:
    def __init__(self):
        self.base_url = 'https://api.anilibria.tv/v3'
        self.base_image_url = 'https://anilibria.tv'

    def get_genres_list(self):
        url = f'{self.base_url}/genres'
        response = requests.get(url)
        if response.status_code == 200:
            start_time = perf_counter()
            result = response.json()
            end_time = perf_counter()
            print(f'Elapsed time: {end_time - start_time:.02f} sec')
            return result
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None

    def get_anime_by_code(self, anime_code):
        url = f'{self.base_url}/title?code={anime_code}'
        response = requests.get(url)
        if response.status_code == 200:
            start_time = perf_counter()
            result = response.json()
            end_time = perf_counter()
            print(f'Elapsed time: {end_time - start_time:.02f} sec')
            return result
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None

    def get_anime_list_by_genre(self, anime_genre):
        url = f'{self.base_url}/title/search?genres={anime_genre}&limit=-1'
        response = requests.get(url)
        if response.status_code == 200:
            start_time = perf_counter()
            result = response.json()
            end_time = perf_counter()
            print(f'Elapsed time: {end_time - start_time:.02f} sec')
            return result
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None

    def search_anime_by_request(self, anime_request):
        url = f'{self.base_url}/title/search?search={anime_request}&limit=-1'
        response = requests.get(url)
        if response.status_code == 200:
            start_time = perf_counter()
            result = response.json()
            end_time = perf_counter()
            print(f'Elapsed time: {end_time - start_time:.02f} sec')
            return result
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None

    def get_banner_content(self):
        url = f'{self.base_url}/title/changes?items_per_page=5'
        response = requests.get(url)
        if response.status_code == 200:
            start_time = perf_counter()
            result = response.json()
            end_time = perf_counter()
            print(f'Elapsed time: {end_time - start_time:.02f} sec')
            return result
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None

    def get_changes_content(self):
        url = f'{self.base_url}/title/changes?items_per_page=15'
        response = requests.get(url)
        if response.status_code == 200:
            start_time = perf_counter()
            result = response.json()
            end_time = perf_counter()
            print(f'Elapsed time: {end_time - start_time:.02f} sec')
            return result
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None

    def get_updates_content(self):
        url = f'{self.base_url}/title/updates?items_per_page=15'
        response = requests.get(url)
        if response.status_code == 200:
            start_time = perf_counter()
            result = response.json()
            end_time = perf_counter()
            print(f'Elapsed time: {end_time - start_time:.02f} sec')
            return result
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None


class KodikParser:
    def __init__(self):
        self.base_url = 'https://kodikapi.com'
        self.rating_service_names = ['kinopoisk_rating', 'imdb_rating', 'shikimori_rating', 'mydramalist_rating']

    def get_rating_by_code(self, anime_code):
        url = f'{self.base_url}/search?token=71d163b40d50397a86ca54c366f33b72&types=anime,anime-serial&limit=1&title={anime_code}&with_material_data=true'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                result = data['results'][0]
                material_data = result.get('material_data')
                if material_data:
                    for rating_service_name in self.rating_service_names:
                        rating = material_data.get(rating_service_name)
                        if rating is not None and rating != 0:
                            return rating
                return '-'
            return None
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None

    def get_screenshots_by_code(self, anime_code, mode=None):
        url = f'{self.base_url}/search?token=71d163b40d50397a86ca54c366f33b72&types=anime,anime-serial&limit=1&title={anime_code}&with_material_data=true'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                result = data['results'][0]
                screenshots = result.get('screenshots')
                if screenshots:
                    if mode == 'random':
                        return random.choice(screenshots)
                    else:
                        return screenshots
                return None
            return None
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None

    def get_player_by_code(self, anime_code):
        url = f'{self.base_url}/search?token=71d163b40d50397a86ca54c366f33b72&types=anime,anime-serial&limit=1&title={anime_code}&with_material_data=true'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                player = data['results'][0]['link']
                if player:
                    return player
                return None
            return None
        else:
            print(f'Error when receiving data. Error code status: {response.status_code}')
            return None


def main_page(request):
    anilibria_parser = AnilibriaParser()
    kodik_parser = KodikParser()

    #sidebar_content = anilibria_parser.get_genres_list()
    banner_content = anilibria_parser.get_banner_content()
    changes_content = anilibria_parser.get_changes_content()
    updates_content = anilibria_parser.get_updates_content()

    banner_data = []
    changes_data = []
    updates_data = []

    for item in banner_content['list']:
        code = item['code']
        title = item['names']['ru']
        rating = kodik_parser.get_rating_by_code(code)
        year = item['season']['year']
        description = item['description']
        genres = ', '.join(item['genres'])
        poster = anilibria_parser.base_image_url + item['posters']['original']['url']
        screenshot = kodik_parser.get_screenshots_by_code(code, 'random')
        banner_data.append(
            {'code': code, 'title': title, 'rating': rating, 'year': year, 'description': description, 'genre': genres,
             'poster_url': poster, 'screenshot': screenshot})

    for item in changes_content['list']:
        code = item['code']
        title = item['names']['ru']
        rating = kodik_parser.get_rating_by_code(code)
        year = item['season']['year']
        poster = anilibria_parser.base_image_url + item['posters']['original']['url']
        changes_data.append({'code': code, 'title': title, 'rating': rating, 'year': year, 'poster_url': poster})

    for item in updates_content['list']:
        code = item['code']
        title = item['names']['ru']
        rating = kodik_parser.get_rating_by_code(code)
        year = item['season']['year']
        poster = anilibria_parser.base_image_url + item['posters']['original']['url']
        updates_data.append({'code': code, 'title': title, 'rating': rating, 'year': year, 'poster_url': poster})

    context = {
        #'genres_list': sidebar_content,
        'banner': banner_data,
        'changes': changes_data,
        'updates': updates_data,
    }

    return render(request, 'main/main_page.html', context)


def player_page(request, pk):
    anilibria_parser = AnilibriaParser()
    kodik_parser = KodikParser()

    #sidebar_content = anilibria_parser.get_genres_list()
    detail = anilibria_parser.get_anime_by_code(pk)

    title = detail['names']['ru']
    description = detail['description']
    genres = ', '.join(detail['genres'])
    year = detail['season']['year']
    duration = detail['type']['full_string']
    poster = anilibria_parser.base_image_url + detail['posters']['original']['url']
    screenshots = kodik_parser.get_screenshots_by_code(pk)
    rating = kodik_parser.get_rating_by_code(pk)
    player = kodik_parser.get_player_by_code(pk)

    context = {
        #'genres_list': sidebar_content,
        'title': title,
        'description': description,
        'genres': genres,
        'year': year,
        'duration': duration,
        'poster_url': poster,
        'screenshots': screenshots,
        'rating': rating,
        'player': player,
    }

    return render(request, 'main/player_page.html', context)


def search_page(request, pk):
    anilibria_parser = AnilibriaParser()
    kodik_parser = KodikParser()

    #sidebar_content = anilibria_parser.get_genres_list()
    search_content = anilibria_parser.search_anime_by_request(pk)

    result_content = []

    for item in search_content['list']:
        code = item['code']
        title = item['names']['ru']
        rating = kodik_parser.get_rating_by_code(code)
        year = item['season']['year']
        poster = anilibria_parser.base_image_url + item['posters']['original']['url']
        result_content.append({'code': code, 'title': title, 'rating': rating, 'year': year, 'poster_url': poster})

    context = {
        #'genres_list': sidebar_content,
        'search_title': pk,
        'search_results': result_content,
    }

    return render(request, 'main/search_page.html', context)


def genres_page(request, pk):
    anilibria_parser = AnilibriaParser()
    kodik_parser = KodikParser()

    #sidebar_content = anilibria_parser.get_genres_list()
    genres_content = anilibria_parser.get_anime_list_by_genre(pk)

    genres_data = []

    for item in genres_content['list']:
        code = item['code']
        title = item['names']['ru']
        rating = kodik_parser.get_rating_by_code(code)
        year = item['season']['year']
        poster = anilibria_parser.base_image_url + item['posters']['original']['url']
        genres_data.append({'code': code, 'title': title, 'rating': rating, 'year': year, 'poster_url': poster})

    context = {
        #'genres_list': sidebar_content,
        'genre_name': pk,
        'genres_results': genres_data,
    }

    return render(request, 'main/genres_page.html', context)


class AdsTxtView(TemplateView):
    template_name = 'ads.txt'
    content_type = 'text/plain'


class RobotsTxtView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


class SitemapXmlView(TemplateView):
    template_name = 'sitemap.xml'
    content_type = 'application/xml'


def terms_page(request):
    return render(request, 'main/terms.html')


def privacy_page(request):
    return render(request, 'main/privacy.html')


def copyright_page(request):
    return render(request, 'main/copyright.html')
