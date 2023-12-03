#!/usr/bin/env python3

from typing import NamedTuple
from math import prod

Matrix = NamedTuple("Matrix", w=int, h=int, data=list[list[str]])
GearSet = set[tuple[int, int]]
GearMap = dict[tuple[int, int], list[int]]

def read(file_name: str) -> Matrix:
  data = list(map(lambda s: list(s.strip()), open(file_name)))
  h = len(data)
  w = len(data[0])
  return Matrix(w, h, data)

def find_gears(m: Matrix) -> GearSet:
  s = GearSet()
  for y in range(m.h):
    for x in range(m.w):
      c = m.data[y][x]
      if c == "*":
        s.add((x, y))
  return s

def adjacent_gear(gears: GearSet, x: int, y: int) -> tuple[int, int] | None:
  for dx in range(-1,2):
    for dy in range(-1,2):
      if (x+dx, y+dy) in gears:
        return (x+dx, y+dy)

def process(m: Matrix) -> GearMap:
  ratios = GearMap()
  gears = find_gears(m)
  buf = ""
  usable = None

  for y in range(m.h):
    for x in range(m.w):
      c = m.data[y][x]
      if c.isdigit():
        buf += c
        adjacent = adjacent_gear(gears, x, y)
        if adjacent:
          usable = adjacent
      if not c.isdigit() or x == m.w-1:
        if buf != "" and usable:
          ratios.setdefault(usable, []).append(buf)
        buf = ""
        usable = None

  return ratios

def solution(file_name: str) -> int:
  return sum([ prod(map(int, gears))
               for _, gears in process(read(file_name)).items()
               if len(gears) == 2 ])

def test():
  assert solution("test/2") == 467835

if __name__ == "__main__":
  print(solution("input"))
