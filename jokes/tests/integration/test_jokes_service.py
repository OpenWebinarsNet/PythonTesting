import unittest

from jokes.joke import Joke
from jokes.joke_service import JokeService


class TestJokeService(unittest.TestCase):

    def test_get_one_random_joke(self):

        joke_service = JokeService()
        result = joke_service.get_jokes()

        self.assertIsInstance(result[0], Joke)
        self.check_joke(result[0])

    def test_get_ten_programming_jokes(self):
        joke_service = JokeService()
        result = joke_service.get_jokes(topic='programming', amount=10)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 10)

        for joke in result:
            self.check_joke(joke)
            self.assertEqual(joke.category.lower(), 'programming')

    def check_joke(self, joke: Joke):
        self.assertIsInstance(joke.category, str)
        self.assertIsInstance(joke.type, str)
        self.assertIsInstance(joke.joke, str)
        self.assertIsInstance(joke.flags, dict)
        self.assertIsInstance(joke.id, int)
        self.assertIsInstance(joke.lang, str)
