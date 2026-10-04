import sys


class ScoreError(Exception):
    def __init__(self, erreur="score erreur"):
        super().__init__(erreur)


def ft_score_analytics():
    print("=== Player Score Analytics ===")
    i = 1
    if len(sys.argv) < 2:
        raise ScoreError(
            "No scores provided. Usage: python3"
            " ft_score_analytics.py <score1><score2> ..."
        )
    else:
        score = []
        while len(sys.argv) > i:
            try:
                entier = int(sys.argv[i])
                score.append(entier)
            except ValueError:
                print(f"Invalid parameter: {sys.argv[i]}")
            i += 1
        if len(score) < 1:
            raise ScoreError(
                "No scores provided. "
                "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )

    print(f"Scores processed: {score} ")
    print(f"Total players: {len(sys.argv) - 1}")
    print(f"Total score: {sum(score)}")
    print(f"Average score: {sum(score) / len(score)}")
    print(f"Hight score: {max(score)}")
    print(f"Low score: {min(score)}")
    print(f"Score range: {max(score) - min(score)}")


if __name__ == "__main__":
    try:
        ft_score_analytics()
    except ScoreError as e:
        print(f"{e}")
