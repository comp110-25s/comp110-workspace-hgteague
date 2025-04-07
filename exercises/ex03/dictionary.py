"""Dictionary functions"""

__author__: str = "730772722"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of dictionary."""
    result: dict[str, str] = {}
    idx: int = 0
    dict_keys: list[str] = list(input_dict)

    while idx < len(dict_keys):
        key: str = dict_keys[idx]
        value: str = input_dict[key]

        search_idx: int = 0

        while search_idx < len(result):
            duplicate: str = list(result)[search_idx]
            if duplicate == value:
                raise KeyError("error message of your choice here!")
            search_idx += 1

        result[value] = key

        idx += 1

    return result


def count(values: list[str]) -> dict[str, int]:
    """Count how many times each string occurs in list."""
    result: dict[str, int] = {}
    idx: int = 0

    while idx < len(values):
        word: str = values[idx]

        count: int = 0
        search_idx: int = 0
        while search_idx < len(result):
            key: str = list(result)[search_idx]
            if key == word:
                count = result[key]
            search_idx += 1

        result[word] = count + 1
        idx += 1

    return result


def favorite_color(input_dict: dict[str, str]) -> str:
    """Return most frequent favorite color from a dictionary of names and colors."""
    color_counts: dict[str, int] = {}
    names: list[str] = list(input_dict)
    idx: int = 0

    while idx < len(names):
        color: str = input_dict[names[idx]]

        count: int = 0
        search_idx: int = 0
        while search_idx < len(color_counts):
            key: str = list(color_counts)[search_idx]
            if key == color:
                count = color_counts[key]
            search_idx += 1

        color_counts[color] = count + 1
        idx += 1

    max_color: str = ""
    max_count: int = 0
    search_idx = 0
    color_keys: list[str] = list(color_counts)

    while search_idx < len(color_keys):
        key: str = color_keys[search_idx]
        if color_counts[key] > max_count:
            max_count = color_counts[key]
            max_color = key
        search_idx += 1

    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins words by length into a dictionary where keys are word lengths and values are sets of words."""
    result: dict[int, set[str]] = {}
    idx: int = 0

    while idx < len(words):
        word: str = words[idx]
        length: int = len(word)

        key_exists: bool = False
        search_idx: int = 0

        while search_idx < len(list(result)):
            if list(result)[search_idx] == length:
                key_exists = True
            search_idx += 1

        if key_exists:
            existing_words: set[str] = result[length]
            temp_set: set[str] = set()
            temp_idx: int = 0
            existing_words_list: list[str] = list(existing_words)

            while temp_idx < len(existing_words_list):
                temp_set = temp_set | {existing_words_list[temp_idx]}
                temp_idx += 1

            temp_set = temp_set | {word}
            result[length] = temp_set
        else:
            result[length] = {word}

        idx += 1

    return result
