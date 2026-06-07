import sys,random,bisect
from collections import deque,defaultdict
from heapq import heapify,heappop,heappush
from itertools import permutations
from math import gcd,log

input = lambda :sys.stdin.buffer.readline()
mi = lambda :map(int,input().split())
li = lambda :list(mi())
def solve():
  for _ in range(int(input())):
      n = int(input())
      edges = [li() for _ in range(n)]
if __name__ == '__main__':
  solve()
