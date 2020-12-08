from typing import Dict, Any


class JokesAPIFactory:

    def create_api_jokes(self, topic: str = '', amount: int = 1) -> Dict[str, Any]:
        if amount == 1:
            joke = self._create_one_joke(topic)
            joke['error'] = False
        elif amount > 1:
            joke = {
                'error': False,
                'jokes': [self._create_one_joke(topic) for i in range(amount)]
            }
        else:
            raise Exception('You have to create at least one joke')

        return joke

    def _create_one_joke(self, topic: str) -> Dict[str, Any]:
        return {
            "category": f"{topic}",
            "type": "twopart",
            "joke": "TIL that changing random stuff until your program works is \"hacky\" and a \"bad coding practice\" but if you do it fast enough it's \"Machine Learning\" and pays 4x your current salary.",
            "flags": {
                "nsfw": True,
                "religious": False,
                "political": False,
                "racist": False,
                "sexist": False
            },
            "id": 158,
            "lang": "en"
        }
