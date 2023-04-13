import os
import json
from chatgpt_wrapper import OpenAIAPI
from chatgpt_wrapper.core.config import Config
import requests
import time
import re
import ast


# API configurations and ENV variables
def getGPTReady():
    os.environ['OPENAI_API_KEY'] = "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"
    config = Config()
    config.set('browser.debug', True)
    return config


def requestSpotifyToken():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials",
            "client_id": "c090be5388f24dcc8f10d5390c2e3dc6",
            "client_secret": "4b63cf7ac1aa48549dd6bda6d20e3fa2"}
    response = requests.post(url=url, headers=headers, data=data)
    response = json.loads(response.text)
    return response["access_token"], response["token_type"]


def getSpotifyID(song_name: str, artist: str, access_token: str, token_type: str):
    url = f"https://api.spotify.com/v1/search?query=remaster%2520track%3A{song_name}%2520artist%3A{artist}&type=track&locale=en-US%2Cen%3Bq%3D0.9&offset=0&limit=1"
    headers = {"Authorization": f"{token_type}  {access_token}"}
    response = json.loads(requests.get(url=url, headers=headers).text)
    return response["tracks"]["items"][0]["external_urls"]["spotify"]


class Chatbot(OpenAIAPI):

    def __init__(self, purpose='songs', config=None, default_user_id=None):
        super().__init__(config, default_user_id)
        if purpose == 'songs':
            self.beginning_prompt = 'The following paragraph(s) describes an image.\n\n'
            self.end_prompt1 = '\n\nRecommend a list of {n_songs} songs that would be the most suitable background music of that image. '
            self.end_prompt2 = \
            'It is more important for the content of the songs to match than for the titles of the songs to match. '\
            'Please provide your answers as a list of JSON-like format (and say nothing else) that have 2 attributes: "title", "artist".'
            self.lastSpotifyCall = None
            self.access_token = None
            self.token_type = None

    def recommendSong(self, n_songs, caption: str, moods: list = None, genres: list = None):
        # progress = tqdm.tqdm(len(captions), ncols=75, desc='Collect ChatGPT')
        with open('chatgpt_songs.json', 'w') as f:
            f.write('')

        self.delete_conversation()
        answer = None

        mood_phrase = "The moods of the songs should be {mood_list}. ".format(
            mood_list=", ".join(moods)) if moods is not None else ""
        genre_phrase = "The genres of the songs should be {genre_list}. ".format(
            genre_list=", ".join(genres)) if genres is not None else ""
        question = self.beginning_prompt + caption + \
            self.end_prompt1.format(n_songs=n_songs) + \
            mood_phrase + genre_phrase + self.end_prompt2

        _, answer, _ = self.ask(question)
        answer = re.sub('  +', '', answer.strip().replace('\n', ''))

        if answer is not None and len(answer) > 0:
            answer = list(ast.literal_eval(answer))

            for id, data in enumerate(answer):
                song = dict(data)
                title_search = song["title"].replace(" ", "%20")
                artist_search = song["artist"].replace(" ", "%20")

                if self.lastSpotifyCall is None:
                    self.access_token, self.token_type = requestSpotifyToken()
                    self.lastSpotifyCall = time.time()
                elif time.time() - self.lastSpotifyCall >= 3600:
                    self.access_token, self.token_type = requestSpotifyToken()
                    self.lastSpotifyCall = time.time()

                spotify_link = getSpotifyID(song_name=title_search, artist=artist_search,
                                            access_token=self.access_token, token_type=self.token_type)
                insert_idx = spotify_link.find('track')
                song["spotify_link"] = spotify_link[:insert_idx] + "embed/" + spotify_link[insert_idx:] + "?utm_source=generator"

                answer[id] = song

            with open('chatgpt_songs.json', 'a') as f:
                json.dump(answer, f)

            return answer

        else:
            exit(0)


if __name__ == "__main__":
    caption = "A sad cat sitting at a table"
    moods = ["sad", "desperate", "depressed"]
    genres = ["ballad", "piano"]
    config = getGPTReady()
    chatbot = Chatbot(config=config)
    _ = chatbot.recommendSong(n_songs=2, caption=caption, moods=moods, genres=genres)