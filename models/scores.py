from typing import List
from models.db import db
from models.score import Score


class Scores:

	def get_top_5(self) -> List[Score]:
		return db.get_scores(limit=5)

	def get_scores(self):
		return db.get_scores()

	def append(self, status, level, score, kills):
		db.insert_score(Score(
			status=status,
			level=level,
			score=score,
			kills=kills,
		))


scores = Scores()
