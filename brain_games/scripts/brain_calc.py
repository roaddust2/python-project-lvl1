#!/usr/bin/env python3
from brain_games import brain_engine
from brain_games.games import brain_calc_engine


def main():
    brain_engine.play(brain_calc_engine)
    return


if __name__ == '__main__':
    main()
