import unittest
from unittest.mock import patch

from jokes.joke import Joke
from jokes.joke_service import JokeService
from jokes.tests.unit.joke_factory import JokesAPIFactory


@patch('jokes.joke_service.requests')
class TestJokeService(unittest.TestCase):

    def setUp(self) -> None:
        self.joke_factory = JokesAPIFactory()

    def test_get_one_random_joke(self, requests_mock):
        requests_mock.get.return_value.json.return_value = self.joke_factory.create_api_jokes('random', 1)
        mock_result = requests_mock.get.return_value

        joke_service = JokeService()
        result = joke_service.get_jokes()

        self.assertIsInstance(result[0], Joke)
        self.assertEqual(requests_mock.get.return_value.json.return_value, result[0].__dict__)

        requests_mock.get.assert_called_once_with(joke_service.HOST_URL.format(topic='Any', amount=1))

        mock_result.raise_for_status.assert_called_once()
        mock_result.json.assert_called_once()

    def test_get_ten_programming_jokes(self, requests_mock):
        mocked_jokes = self.joke_factory.create_api_jokes('programming', 10)
        requests_mock.get.return_value.json.return_value = mocked_jokes

        joke_service = JokeService()
        result = joke_service.get_jokes(topic='programming', amount=10)

        self.assertIsInstance(result, list)

        for i, joke in enumerate(result):
            self.assertEqual(mocked_jokes['jokes'][i], joke.__dict__)
