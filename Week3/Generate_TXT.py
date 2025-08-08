with open("large_text.txt", "w") as f:
    for _ in range(230000):  # ~10MB total
        f.write("The quick brown fox jumps over the lazy dog.\n")