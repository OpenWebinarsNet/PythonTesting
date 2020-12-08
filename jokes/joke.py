import dataclasses
from typing import Dict, Optional


@dataclasses.dataclass
class Joke:
    category: str
    type: str
    joke: str
    flags: Dict[str, bool]
    id: str
    lang: str

    def __str__(self) -> str:
        return self.joke
