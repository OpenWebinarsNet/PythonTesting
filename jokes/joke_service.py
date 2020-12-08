from typing import List, Any, Dict

from pip._vendor import requests

from jokes.joke import Joke


class JokeService:

    HOST_URL = 'https://sv443.net/jokeapi/v2/joke/{topic}?amount={amount}&type=single'

    def get_jokes(self, topic: str = 'Any', amount: int = 1) -> List[Joke]:
        result = requests.get(self.HOST_URL.format(topic=topic, amount=amount))
        result.raise_for_status()

        body = result.json()
        if result.ok and not body['error']:
            jokes = self._parse_jokes(body)
            return jokes

    def _parse_jokes(self, body: Dict[str, Any]) -> List[Joke]:
        jokes__api = body.get('jokes')
        if jokes__api:
            jokes = [Joke(**joke) for joke in jokes__api]
        else:
            body.pop('error')
            jokes = [Joke(**body)]
        return jokes

