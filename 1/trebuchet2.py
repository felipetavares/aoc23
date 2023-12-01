#!/usr/bin/env python3

from typing import Iterable
import re

DIGITS = {
  "one": "1", "two": "2", "three": "3",
  "four": "4", "five": "5", "six": "6",
  "seven": "7", "eight": "8", "nine": "9"
}

# NOTE: On 3.12 we could use the new "type" syntax
DigitsLine = Iterable[str]

def parse(file_name: str) -> Iterable[DigitsLine]:
  digits_regexp = "(?=(" + "|".join(DIGITS.keys()) + "|\\d))"
  return map(lambda line: re.findall(digits_regexp, line), open(file_name))

def translate_digits(lines: Iterable[DigitsLine]) -> Iterable[DigitsLine]:
  return map(lambda line: map(lambda digit: DIGITS.get(digit, digit), line), lines)

def find_digits(obfuscated_coords: Iterable[DigitsLine]) -> Iterable[int]:
  return map(lambda coord: int(coord[0] + coord[-1]), map(list, obfuscated_coords))

def solve(file_name: str) -> int:
  return sum(find_digits(translate_digits(parse(file_name))))

def test_input():
  assert solve("test/2") == 281

if __name__ == "__main__":
  print(solve("input"))
