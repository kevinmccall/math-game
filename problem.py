from dataclasses import dataclass


@dataclass
class Problem:
    prompt: str
    answer: int | str
