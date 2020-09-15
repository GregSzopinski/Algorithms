def memoize(s: str, word_list: list, memo: dict) -> bool:
    """Helper used  for caching already checked elements of the recursive tree"""
    if s in word_list:
        return True
    # check if we have already solved the sub-problem in recursive tree
    elif s in memo:
        return memo[s]

    for word in word_list:
        if s[0:len(word)] == word and memoize(s[len(word):], word_list, memo):
            memo[s] = True
            return True
    memo[s] = False
    return False


def word_break(s: str, word_list: list) -> bool:
    """Return True if s can be segmented into one or more words from word_list"""
    memo = dict()
    return memoize(s, word_list, memo)
