from django.contrib.sessions.middleware import SessionMiddleware


class AnimeSessionMiddleware(SessionMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)

        self.session_objects = {
            "anime_details": {},
            "anime_episode": "",
            "anime_episodes": {},
            "anime_search_results": {},
            "anime_search_query": "",
            "episode_links": {},
            "recent_episodes": {},
            "top_airing": {},
        }

    def __call__(self, request):
        for key, value in self.session_objects.items():
            if key not in request.session:
                self.fetch_data(request, key, value)

        request.get_anime_details = lambda: self.get_session_object(
            request, "anime_details"
        )
        request.get_anime_episode = lambda: self.get_session_object(
            request, "anime_episode"
        )
        request.get_anime_episodes = lambda: self.get_session_object(
            request, "anime_episodes"
        )
        request.get_anime_search_results = lambda: self.get_session_object(
            request, "anime_search_results"
        )
        request.get_anime_search_query = lambda: self.get_session_object(
            request, "anime_search_query"
        )
        request.get_episode_links = lambda: self.get_session_object(
            request, "episode_links"
        )

        request.get_recent_episodes = lambda: self.get_session_object(
            request, "recent_episodes"
        )
        request.get_top_airing = lambda: self.get_session_object(request, "top_airing")

        return self.get_response(request)

    def fetch_data(self, request, key, value):
        request.session[key] = value

    def get_session_object(self, request, key):
        if key in request.session:
            return request.session[key]
        return None

    def set_session_object(self, request, key, value):
        request.session[key] = value

    def clear_session(self, request):
        for key in self.session_objects:
            request.session[key] = None
            request.session.modified = True
