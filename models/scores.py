class Scores:
    def __init__(self):
        self.score_list = []

    def get_top_5(self):
        return sorted(self.score_list, key=lambda item: item['score'], reverse=True)

    def get_scores(self):
        return self.score_list

    def append(self, status, level, score, kills):
        self.score_list.append({
            "status": status,
            "level": level,
            "score": score,
            "kills": kills,
        })


scores = Scores()
