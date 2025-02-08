def to_roman(num: int) -> str:
    """
    1〜3999 の整数をローマ数字に変換する関数。

    Args:
        num (int): 変換する整数（1〜3999）

    Returns:
        str: ローマ数字に変換された文字列

    Raises:
        ValueError: num が 1〜3999 の範囲にない場合
    """
    if not (0 < num < 4000):
        raise ValueError("The range of numbers that can be converted is 1 to 3999")
    
    # 各桁の対応表を用意
    thousands = ["", "M", "MM", "MMM"]
    hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return (
        thousands[num // 1000] +
        hundreds[(num % 1000) // 100] +
        tens[(num % 100) // 10] +
        ones[num % 10]
    )


if __name__ == '__main__':
    print(to_roman(int(input("数値を入力して："))))