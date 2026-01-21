"""Module for text indentation based on punctuation"""

def text_indentation(text):
    """Print text with 2 new lines after '.', '?', ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    end_chars = ".?:"
    i = 0
    while i < len(text):
        line = ""
        while i < len(text) and text[i] not in end_chars:
            line += text[i]
            i += 1
        if i < len(text):
            line += text[i]  # add the punctuation
            i += 1
        print(line.strip())
        if line.strip():
            print()
