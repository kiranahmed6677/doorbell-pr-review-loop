from doorbell import top_n_words


def test_basic_ranking():
    text = "the cat sat on the mat the cat ran"
    assert top_n_words(text, 2) == ["the", "cat"]


def test_n_larger_than_unique_words():
    text = "one two two three three three"
    assert top_n_words(text, 10) == ["three", "two", "one"]


def test_punctuation_and_case_are_normalized():
    text = "Hi! hi. HI, there there."
    assert top_n_words(text, 2) == ["hi", "there"]


def test_empty_text_returns_empty_list():
    assert top_n_words("", 3) == []


def test_n_zero_returns_empty_list():
    assert top_n_words("a b c", 0) == []
