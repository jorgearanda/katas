# Tennis Kata

Write a Game class that can keep track of a single game of tennis.
The class must be initialized with the names of the players
(such as `Game('Player A', 'Player B')`),
and expose the following calls:

  * `Game.point(player)` - award a point to the player
  * `Game.score()` - report the current score in readable text (see below)
  * `Game.winner()` - report the winner of the game; `None` if still undecided

Score format:

  * A player's score progression is love (zero) -> 15 -> 30 -> 40 -> (match)
  * Scores are reported in format: `first_player_score-second_player_score`
    - Examples: `15-30`, `40-love`
  * A score of 0-0 is reported as `love all`
  * A score of 40-40 is reported as `deuce`
  * A player must win by a two-point differential. If a player is at 40,
    their opponent must score two points beyond 40 to win.
    In this case, a point over deuce is reported as `advantage player_name`
  * Game victory is reported as `player_name wins`.
    Subsequent points should be ignored for scoring
