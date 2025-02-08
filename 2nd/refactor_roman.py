def to_roman(n: int) -> str:
    """
    1〜9 の整数をローマ数字に変換する関数。

    Args:
        n (int): 変換する数字（1〜9）。0 はローマ数字として定義されていません。

    Returns:
        str: ローマ数字

    Raises:
        ValueError: nが0の場合、または1〜9以外の場合。
    """
    if n == 0:
        raise ValueError("There is no Roman numeral for ZERO")
    if not 1 <= n <= 9:
        raise ValueError("Input must be between 1 and 9")
    
    roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return roman_numerals[n - 1]


