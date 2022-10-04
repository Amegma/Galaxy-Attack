from pathlib import Path
from models.score import Score
import sqlite3
import datetime as dt
from typing import List

from utils.appdata_dir import db_path


class Db:

	def __init__(self, file_path: Path | str) -> None:
		self.con = sqlite3.connect(file_path)
		self._init_db()

	def _init_db(self):
		create_table_query = """
			CREATE TABLE IF NOT EXISTS score (
				created_at INTEGER, -- Unix Epoch
				status INTEGER,
				level INTEGER,  
				score INTEGER,
				kills INTEGER
			)
		"""

		self.con.execute(create_table_query)
		self.con.commit()

	def get_scores(self, limit: int = 5) -> List[Score]:
		cur = self.con.execute(
			"""
				SELECT status, level, score, kills FROM score
				ORDER BY created_at DESC
				limit ?
			""",
			(limit, ),
		)

		records = cur.fetchall()
		scores = []
		for record in records:
			status, level, score, kills = record
			scores.append(Score(
				status=bool(status),
				level=level,
				score=score,
				kills=kills,
			))
		return scores

	def insert_score(self, score: Score):
		now = int(dt.datetime.now().timestamp())
		self.con.execute(
			"""
				INSERT INTO score (created_at, status, level, score, kills)
				VALUES (?, ?, ?, ?, ?)
			""",
			(now, score.status, score.level, score.score, score.kills),
		)
		self.con.commit()


db = Db(db_path())
