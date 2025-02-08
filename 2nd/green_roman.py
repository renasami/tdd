
# 最小限の実装(関数のみの実装)
def to_roman(n: int) -> str:
    if n == 0:
        raise ValueError("There is no Roman numeral for ZERO")
    if n > 9:
        raise ValueError("Input must be between 1 and 9")
    if n == 1:
        return "I"
    if n == 2:
        return "II"
    if n == 3:
        return "III"
    if n == 4:
        return "IV"
    if n == 5:
        return "V"
    if n == 6:
        return "VI"
    if n == 7:
        return "VII"
    if n == 8:
        return "VIII"
    if n == 9:
        return "IX"
    


