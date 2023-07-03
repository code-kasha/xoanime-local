import json
import requests


from django.shortcuts import render, redirect
from django.urls import reverse


def clear(request):
    request.session.clear()
    return redirect("/")


def index(request):
    context = {}
    return render(request, "index.html", context)


def search_anime(request):
    page = request.GET.get("page")
    if not page:
        page = 1
    query = request.GET.get("query")
    url = f"http://localhost:3000/anime/gogoanime/{query}"
    if not request.session.get("anime_search_results"):
        request.session["anime_search_results"] = requests.get(url).json()
        request.session["anime_search_query"] = query
    elif request.session["anime_search_query"] != query:
        request.session["anime_search_results"] = requests.get(url).json()
        request.session["anime_search_query"] = query
    return render(request, "anime/search.html")


def paginate_search(request, page):
    query = request.session.get("anime_search_query")
    print(request)
    page = page
    request.session["anime_search_results"] = requests.get(
        f"http://localhost:3000/anime/gogoanime/{query}?page={page}"
    ).json()
    return render(request, "anime/search.html")


def recent_episodes(request):
    page = request.GET.get("page")
    if not page:
        page = 1
    url = f"http://localhost:3000/anime/gogoanime/recent-episodes?page={page}"
    if (
        not request.session.get("recent_episodes")
        or request.session.get("recent_episodes")["currentPage"] != page
    ):
        request.session["recent_episodes"] = requests.get(url).json()
    return render(request, "anime/recent.html")


def top_airing(request):
    page = request.GET.get("page")
    if not page:
        page = 1
    url = f"http://localhost:3000/anime/gogoanime/top-airing?page={page}"
    if (
        not request.session.get("top_airing")
        or request.session.get("top_airing")["currentPage"] != page
    ):
        request.session["top_airing"] = requests.get(url).json()
    return render(request, "anime/top.html")


def anime_details(request):
    id = request.GET.get("id")
    url = f"http://localhost:3000/anime/gogoanime/info/{id}"
    if (
        not request.session.get("anime_details")
        or request.session["anime_details"]["id"] != id
    ):
        request.session["anime_details"] = requests.get(url).json()
        request.session["anime_episodes"] = request.session["anime_details"]["episodes"]
        del request.session["anime_details"]["episodes"]
    return render(request, "anime/details.html")


def watch_anime(request):
    if request.session.get("anime_episodes"):
        first_episode = request.session["anime_episodes"][0]
        play_url = reverse("play") + f"?id={first_episode['id']}"
        return redirect(play_url)


def watch_episode(request):
    id = request.GET.get("id")
    details_url = f"http://localhost:3000/anime/gogoanime/info/{id}"
    request.session["anime_details"] = requests.get(details_url).json()
    request.session["anime_episodes"] = request.session["anime_details"]["episodes"]
    del request.session["anime_details"]["episodes"]
    last_episode = request.session["anime_episodes"][-1]
    play_url = reverse("play") + f"?id={last_episode['id']}"
    return redirect(play_url)


def play_episode(request):
    id = request.GET.get("id")
    links = f"http://localhost:3000/anime/gogoanime/watch/{id}"
    episode_list = request.session.get("anime_episodes")
    selected_episode = next(
        (episode for episode in episode_list if episode["id"] == id), None
    )
    if (
        not request.session.get("anime_episode")
        or request.session.get("anime_episode")["id"] != id
    ):
        request.session["anime_episode"] = selected_episode
        episode_links = requests.get(links).json()
        sources = episode_links.get("sources", [])
        request.session["episode_links"] = json.dumps({"sources": sources})

    return render(request, "anime/watch.html")


def video_proxy(request, url):
    pass
