#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.even_code import generate_round
from brain_games.games.even_code import DESCRIPTION


def main():
    run_game(generate_round, DESCRIPTION)


if __name__ == '__main__':
    main()