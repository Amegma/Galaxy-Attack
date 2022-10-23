from dataclasses import dataclass


@dataclass
class Score:
	status: bool
	level: int
	score: int
	kills: int