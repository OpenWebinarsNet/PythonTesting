import dataclasses
from typing import Dict, Optional


@dataclasses.dataclass
class Joke:
    category: str
    type: str
    setup: Optional[str]
    delivery: Optional[str]
    joke: Optional[str]
    flags: Dict[str, bool]
    id: str
    lang: str

    def __str__(self) -> str:
        joke = self.joke or (f'{self.setup} \n {self.delivery}')
        return joke
