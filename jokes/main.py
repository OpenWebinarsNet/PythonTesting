from argparse import ArgumentParser

from jokes.joke_service import JokeService

if __name__ == '__main__':
    parser = ArgumentParser(description='Hilarious application to get funny moments in your life')
    parser.add_argument('--amount', default=1, type=int, help='specify the amount of jokes you want to find')
    parser.add_argument('--topic', default='Any', type=str, help='specify the topic of the jokes you want to find')

    arguments = parser.parse_args()

    joke_service = JokeService()
    jokes = joke_service.get_jokes(topic=arguments.topic, amount=arguments.amount)

    for index, joke in enumerate(jokes):
        print(str(joke))
        print('------------------')
