#!/usr/bin/env python3

from typing import Iterable

lambda round: round.strip().split(", ")

RawCount = tuple[int, str]
RawRound = Iterable[RawCount]
RawGame = Iterable[RawRound]

Count = dict[str, int]
Round = Iterable[Count]
Game = Iterable[Round]

def parse_count(count: str) -> RawCount:
  elements = count.split(" ")
  return int(elements[0]), elements[1]

def parse_round(round: str) -> RawRound:
  return map(parse_count, round.strip().split(", "))

def parse_game(line: str) -> RawGame:
  return map(parse_round, line.split(": ")[1].split("; "))

def parse(file_name: str) -> Iterable[RawGame]:
  return map(parse_game, open(file_name))

def max_counts(games: Iterable[RawGame]) -> Iterable[Count]:
  def game_to_max_count(game: RawGame) -> Count:
    max_count: Count = {}
    for raw_round in game:
      for raw_count in raw_round:
        if raw_count[1] in max_count:
          if raw_count[0] > max_count[raw_count[1]]:
            max_count[raw_count[1]] = raw_count[0]
        else:
            max_count[raw_count[1]] = raw_count[0]
    return max_count

  return map(game_to_max_count, games)

def power_sum(games: Iterable[Count]) -> int:
  return sum(map(lambda g: g["red"] * g["green"] * g["blue"], games))

def solve(file_name: str) -> int:
  return power_sum(max_counts(parse(file_name)))

def test():
  assert solve("test/2") == 2286

if __name__ == "__main__":
  print(solve("input"))
