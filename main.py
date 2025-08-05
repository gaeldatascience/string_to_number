import re

def string_to_number(sentence):
    """Convert a string representation of a number to its integer value.
    
    This function parses English words representing numbers and converts them
    to their corresponding integer value. It supports numbers from zero to
    billions, including compound numbers with hundreds, thousands, millions,
    and billions.
    
    Args:
        sentence (str): A string containing the English representation of a number.
            The string should be in lowercase and can contain words like "one",
            "twenty", "hundred", "thousand", "million", "billion", etc.
    
    Returns:
        int: The integer value corresponding to the input string.
    
    Examples:
        >>> string_to_number("twenty three")
        23
        >>> string_to_number("one hundred twenty three")
        123
        >>> string_to_number("five thousand six hundred seventy eight")
        5678
        >>> string_to_number("one million two hundred thousand")
        1200000
        >>> string_to_number("three billion four hundred million")
        3400000000
    """
    digits_dic = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19
    }
    
    dozens_dic = {
        "twenty": 20, "thirty": 30, "forty": 40,
        "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90,
    }

    threshold_dic = {
        "hundred": 100,
        "thousand": 1_000,
        "million": 1_000_000,
        "billion": 1_000_000_000,
    }

    # Normalize the input string
    sentence = sentence.replace("-", " ").replace(",", " ")

    big_scales = ["thousand", "million", "billion"]
    pattern    = r"\b(" + "|".join(map(re.escape, big_scales)) + r")\b"
    
    tokens = [t.strip() for t in re.split(pattern, sentence) if t.strip()]

    total = 0
    current = 0

    for token in tokens:
        if token in big_scales:
            current *= threshold_dic[token]
            total += current
            current = 0
        else:
            for word in token.split():
                if word in digits_dic:
                    current += digits_dic[word]
                elif word in dozens_dic:
                    current += dozens_dic[word]
                elif word == "hundred":
                    current *= threshold_dic[word]

    total += current
    return total


if __name__ == "__main__":
    s = input("Enter a number in words: ").strip().lower()
    if not s:
        s = "one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine"
    result = string_to_number(s)
    print(f"{s} → {result:,}")