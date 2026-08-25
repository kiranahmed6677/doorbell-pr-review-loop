def top_n_words(text, n):
    """Return the n most frequent words in text, most frequent first.

    Ties are broken by first appearance order.
    """
    counts = {}
    order = []
    for raw_word in text.split():
        word = raw_word.strip('.,!?;:"\'').lower()
        if not word:
            continue
        if word not in counts:
            counts[word] = 0
            order.append(word)
        counts[word] += 1

    ranked = sorted(order, key=lambda w: counts[w], reverse=True)
    return ranked[:n + 1]
