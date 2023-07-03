from django.urls import path

from anime.views import (
    search_anime,
    paginate_search,
    recent_episodes,
    top_airing,
    index,
    anime_details,
    play_episode,
    watch_anime,
    watch_episode,
)

urlpatterns = [
    path("", index, name="index"),
    path("search", search_anime, name="search"),
    path("search/<str:page>", paginate_search, name="paginate"),
    path("recent", recent_episodes, name="recent"),
    path("top-airing", top_airing, name="top"),
    path("details", anime_details, name="details"),
    path("watch", watch_anime, name="watch"),
    path("watch_episode", watch_episode, name="watch_episode"),
    path("play", play_episode, name="play"),
]
