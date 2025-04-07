"""Test dictionary functions"""

__author__: str = "730772722"


import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use_case():
    """Test normal case: keys and values swapped."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_pair():
    """Test dictionary with one key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_duplicate_values():
    """Test case where duplicate values exist. Only first occurrence is kept."""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count_use_case():
    """Test counting occurrences of words in a list."""
    assert count(["apple", "banana", "apple", "orange", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "orange": 1,
    }


def test_count_empty_list():
    """Test an empty list should return an empty dictionary."""
    assert count([]) == {}


def test_count_single_occurrence():
    """Test when all elements appear only once."""
    assert count(["one", "two", "three"]) == {"one": 1, "two": 1, "three": 1}


def test_favorite_color_use_case():
    """Test finding the most frequent favorite color."""
    assert (
        favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "blue"}) == "blue"
    )


def test_favorite_color_tie():
    """Test tie case; should return the first encountered color."""
    assert (
        favorite_color(
            {"Alice": "red", "Bob": "blue", "Charlie": "red", "Dave": "blue"}
        )
        == "red"
    )


def test_favorite_color_single_person():
    """Test case with only one person."""
    assert favorite_color({"Alice": "purple"}) == "purple"


def test_bin_len_use_case():
    """Test grouping words by their length."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_duplicates():
    """Test case where words of the same length are repeated."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_empty():
    """Test case with an empty list should return an empty dictionary."""
    assert bin_len([]) == {}


if __name__ == "__main__":
    pytest.main()
