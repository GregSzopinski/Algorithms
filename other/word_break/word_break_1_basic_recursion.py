def word_break(s: str, word_list: list) -> bool:
    """
    Return True if s can be segmented into one or more words from word_list
    This algorithm is a naive variant of Leetcode's Word Break 1
    https://leetcode.com/problems/word-break/
    It won't pass leetcode's tests, due to limited speed but still is a good starting point
    """
    if s in word_list:
        return True

    for word in word_list:
        if s[0:len(word)] == word and word_break(s[len(word):], word_list):
            return True

    return False
