#!/usr/bin/env python3
from brain_games.engine import run_game


from brain_games.games import even_code


def main():
    run_game(even_code)


if __name__ == '__main__':
    main()
