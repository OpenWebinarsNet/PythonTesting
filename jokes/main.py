from argparse import ArgumentParser

from jokes.joke_service import JokeService

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--amount', default=1, type=int)
    parser.add_argument('--topic', default='Any', type=str)

    arguments = parser.parse_args()

    joke_service = JokeService()
    jokes = joke_service.get_jokes(topic=arguments.topic, amount=arguments.amount)

    for index, joke in enumerate(jokes):
        print(f'joke {index + 1}')
        print(str(joke))
        print('------------------')
