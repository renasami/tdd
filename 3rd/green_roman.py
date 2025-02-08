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
    
    # 各桁に分解
    thousands = num // 1000
    hundreds  = (num % 1000) // 100
    tens      = (num % 100) // 10
    ones      = num % 10

    result = ""

    # 千の位の処理
    if thousands == 1:
        result += "M"
    elif thousands == 2:
        result += "MM"
    elif thousands == 3:
        result += "MMM"

    # 百の位の処理
    if hundreds == 1:
        result += "C"
    elif hundreds == 2:
        result += "CC"
    elif hundreds == 3:
        result += "CCC"
    elif hundreds == 4:
        result += "CD"
    elif hundreds == 5:
        result += "D"
    elif hundreds == 6:
        result += "DC"
    elif hundreds == 7:
        result += "DCC"
    elif hundreds == 8:
        result += "DCCC"
    elif hundreds == 9:
        result += "CM"

    # 十の位の処理
    if tens == 1:
        result += "X"
    elif tens == 2:
        result += "XX"
    elif tens == 3:
        result += "XXX"
    elif tens == 4:
        result += "XL"
    elif tens == 5:
        result += "L"
    elif tens == 6:
        result += "LX"
    elif tens == 7:
        result += "LXX"
    elif tens == 8:
        result += "LXXX"
    elif tens == 9:
        result += "XC"

    # 一の位の処理
    if ones == 1:
        result += "I"
    elif ones == 2:
        result += "II"
    elif ones == 3:
        result += "III"
    elif ones == 4:
        result += "IV"
    elif ones == 5:
        result += "V"
    elif ones == 6:
        result += "VI"
    elif ones == 7:
        result += "VII"
    elif ones == 8:
        result += "VIII"
    elif ones == 9:
        result += "IX"

    return result



if __name__ == '__main__':
    print(to_roman(int(input("数値を入力して："))))