# Advent of Code 2024 Solutions

![AOC Stars](https://img.shields.io/badge/AOC_Stars-50_⭐-gold?style=plastic&logo=python&logoColor=white)

My solutions for [Advent of Code 2024](https://adventofcode.com/2024), a series of programming puzzles released daily during December.

## Overview

Advent of Code is an annual set of Christmas-themed programming challenges that can be solved in any programming language. Each puzzle has two parts, with the second part unlocked after completing the first. Each part solved awards one star ⭐.

## Implementation Details

All solutions are implemented in Python. Most solutions use only the standard library, with occasional use of `tqdm` for progress bars (not required to run the solutions).

## Learning Journey

### Key Learnings
- Implemented and understood memoization using Python decorators for optimizing recursive solutions or repetitive computations
- Frequent practice with pathfinding algorithms (Dijkstra and A*) through various puzzle applications
- Day 14 was particularly interesting, learning about different approaches to find outlier patterns:
  - Some users analyzed compression rates of the image
  - Others plotted point distribution averages
  - I found the outlier in the custom metric of the problem
- Day 23 required to look up max clique algos, in particular [Bron-Kerbosch](https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm)


### Challenges Faced
- Day 21 was really hard, I started using Djikstra but I was not making it work for part 1, went back and did it the bruteforce way by trying all combinations. But then needed to optimise for part 2. I really struggled to wrap my head around the recursion so I had to look for hints.
- Day 23 was challenging but rewarding - required revisiting computer architecture concepts like Ripple Carry Adders for part 2
- Some of the harder problems required consulting the Reddit community for hints and approaches

### Community Experience
The AoC community, particularly on Reddit, has been incredibly helpful and encouraging. While I needed to look up hints for some of the more challenging problems, it was inspiring to see different approaches and solutions from other participants. The collaborative spirit of the community adds a great dimension to the problem-solving experience.

## Notes
- Input files are not included in the repository as per Advent of Code's request
- Each day's solution is contained in its own directory
