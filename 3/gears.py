#!/usr/bin/env python3

from typing import NamedTuple

Matrix = NamedTuple("Matrix", w=int, h=int, data=list[list[str]])
SymbolSet = set[tuple[int, int]]

def read(file_name: str) -> Matrix:
  data = list(map(lambda s: list(s.strip()), open(file_name)))
  h = len(data)
  w = len(data[0])
  return Matrix(w, h, data)

def find_symbols(m: Matrix) -> SymbolSet:
  s = SymbolSet()
  for y in range(m.h):
    for x in range(m.w):
      c = m.data[y][x]
      if c != "." and not c.isdigit():
        s.add((x, y))
  return s

def adjacent_symbol(symbols: SymbolSet, x: int, y: int) -> bool:
  for dx in range(-1,2):
    for dy in range(-1,2):
      if (x+dx, y+dy) in symbols:
        return True
  return False

def process(m: Matrix) -> list[str]:
  numbers = []
  symbols = find_symbols(m)
  buf = ""
  usable = False

  for y in range(m.h):
    for x in range(m.w):
      c = m.data[y][x]
      if c.isdigit():
        buf += c
        if adjacent_symbol(symbols, x, y):
          usable = True
      if not c.isdigit() or x == m.w-1:
        if buf != "" and usable:
          numbers.append(buf)
        buf = ""
        usable = False

  return numbers

def solution(file_name: str) -> int:
  return sum(map(int, process(read(file_name))))

def test():
  assert solution("test/1") == 4361

if __name__ == "__main__":
  print(solution("input"))
