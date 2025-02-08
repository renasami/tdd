# 仕様

* ~~1桁の数値において、入力された値のローマ数字を返す~~
* 0より小さい値が入力された場合、エラーを返す
* ~~9より大きい場合、エラーを返す~~
* 1~3999の場合、ローマ数字を返す
* 4000以上の場合、エラーを返す


# テスト
```
python3 -m unittest test_red_roman.py
python3 -m unittest test_green_roman.py
python3 -m unittest test_refactor_roman.py
```

# テストケース

正常系
* 入力 1 → 出力 "I"
* 入力 4 → 出力 "IV"
* 入力 9 → 出力 "IX"
* 入力 40 → 出力 "XL"
* 入力 50 → 出力 "L"
* 入力 90 → 出力 "XC"
* 入力 100 → 出力 "C"
* 入力 400 → 出力 "CD"
* 入力 500 → 出力 "D"
* 入力 900 → 出力 "CM"
* 入力 58 → 出力 "LVIII"
* 入力 1994 → 出力 "MCMXCIV"
* 入力 3999 → 出力 "MMMCMXCIX"
異常系
* 入力 0 → ValueError を発生させる
* 入力 -1 → ValueError を発生させる
* 入力 4000 → ValueError を発生させる