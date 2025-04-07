"""A program to run the word guessing game, Wordle!"""

__author__: str = "730772722"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    max_turns: int = 6
    won: bool = False

    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        emoji_output: str = emojified(guess, secret)
        print(emoji_output)

        if guess == secret:
            won = True
        else:
            turns += 1

        if won:
            print(f"You won in {turns}/{max_turns}")
        else:
            print("X/6 - Sorry, try again tomorrow!")


def contains_char(search_string: str, character: str) -> bool:
    """Returns True if character is found in search_string, otherwise returns False."""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(search_string):
        if search_string[idx] == character:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji feedback for the guessed word."""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    idx: int = 0
    emoji_output: str = ""

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            emoji_output += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emoji_output += YELLOW_BOX
        else:
            emoji_output += WHITE_BOX
        idx += 1
    return emoji_output


def input_guess(expected_length: int) -> str:
    """Prompts user until guess meets expected length requirements."""
    guess: str = input(f"Enter a {expected_length} character word")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


if __name__ == "__main__":
    main(secret="codes")
