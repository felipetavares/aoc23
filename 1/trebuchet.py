from typing import Iterable

def parse(file_name: str) -> Iterable[str]:
  return map(lambda line: "".join(filter(str.isdigit, line)), open(file_name))

def find_digits(obfuscated_coords: Iterable[str]) -> Iterable[int]:
  return map(lambda coord: int(coord[0] + coord[-1]), obfuscated_coords)

def solve(file_name: str) -> int:
  return sum(find_digits(parse(file_name)))

def test():
  assert solve("test/1") == 142

if __name__ == "__main__":
  print(solve("input"))
