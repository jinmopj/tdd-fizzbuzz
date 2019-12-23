# TDD - FizzBuzz

## 参考URL
- https://channel9.msdn.com/Events/de-code/2017/DO03

## 問題
- 1から100までの数をプリントするプラグラムを書け。ただし、3の倍数のときは数の代わりに「Fizz」と、5の倍数のときは「Buzz」とプリントし、3と5両方の倍数の場合には、「FizzBuzz」とプリントすること。

## 前処理

### 改行
- 1から100までの数をプリントするプラグラムを書け。
- ただし、3の倍数のときは数の代わりに「Fizz」と、
- 5の倍数のときは「Buzz」とプリントし、
- 3と5両方の倍数の場合には、「FizzBuzz」とプリントすること。

### 要素に分ける
- 1から100までの数　＝＞　難しくはないけど面倒臭い
- を
- プリントする　＝＞　プリントしていることをテストせよ　＝＞　言語構造に深く食い込む　＝＞　難しい
- プラグラムを書け。　＝＞　自明

- ただし、　＝＞　「ただし」の後ろは例外、準正常系

- 3の倍数のときは数の代わりに「Fizz」と、
- 5の倍数のときは「Buzz」とプリントし、
- 3と5両方の倍数の場合には、「FizzBuzz」とプリントすること。

### TODOリストにする

- [ ] 1から100までの数
- [ ] プリントする

- ただし、

- [ ] 3の倍数のときは数の代わりに「Fizz」と、
- [ ] 5の倍数のときは「Buzz」とプリントし、
- [ ] 3と5両方の倍数の場合には、「FizzBuzz」とプリントすること。

### 優先順位をつけてソート

- ただし、

- [ ] 3の倍数のときは数の代わりに「Fizz」と、
- [ ] 5の倍数のときは「Buzz」とプリントし、　＝＞　プリントするはあとでテストするので削除
- [ ] 3と5両方の倍数の場合には、「FizzBuzz」とプリントすること。　＝＞　プリントするはあとでテストするので削除

- [ ] 1から100までの数　＝＞　できなくはないけど、面倒なので後ろに回す
- [ ] プリントする　＝＞　できなくはないけど、もうちょっと面倒なのでさらに後ろに回す

### 正常系を考える

- ただしの前に含まれていた正常系とは何だったけ？　＝＞　数をプリントする

- ただし、

- [ ] 3の倍数のときは数の代わりに「Fizz」と
- [ ] 5の倍数のときは「Buzz」と
- [ ] 3と5両方の倍数の場合には、「FizzBuzz」と

- [ ] 1から100までの数
- [ ] プリントする

### 重複を削除

- [ ] 数をプリントする　＝＞　プリントするはあとでやると言ったじゃん　＝＞　削除

- ただし、

- [ ] 3の倍数のときは数の代わりに「Fizz」と
- [ ] 5の倍数のときは「Buzz」と
- [ ] 3と5両方の倍数の場合には、「FizzBuzz」と

- [ ] 1から100までの数
- [ ] プリントする

### 準正常系から正常系を考える

- [ ] 数を　＝＞　数をどうするの？　＝＞　文字列にして返す

- ただし、

- [ ] 3の倍数のときは数の代わりに「Fizz」と　＝＞　3の倍数のときに文字列にして返す
- [ ] 5の倍数のときは「Buzz」と　＝＞　5の倍数のときに文字列にして返す
- [ ] 3と5両方の倍数の場合には、「FizzBuzz」と　＝＞　3と5両方の倍数の場合に文字列にして返す

- [ ] 1から100までの数
- [ ] プリントする

### 整理する

- [ ] 数を文字列にして返す

- ただし、

- [ ] 3の倍数のときは数の代わりに「Fizz」と返す
- [ ] 5の倍数のときは「Buzz」と返す
- [ ] 3と5両方の倍数の場合には、「FizzBuzz」と返す

- [ ] 1から100までの数
- [ ] プリントする

### 最終的なTODOリスト

#### 正常系
- [ ] 数を文字列にして返す
#### 準正常系
- [ ] 3の倍数のときは数の代わりに「Fizz」と返す
- [ ] 5の倍数のときは「Buzz」と返す
- [ ] 3と5両方の倍数の場合には、「FizzBuzz」と返す
#### その他
- [ ] 1から100までの数
- [ ] プリントする

## テストコードの書き方
- 必ず落ちる空のテストを書く　＝＞　テストコードのテスト
- テストコードのテストメソッド名は日本語で書く
- テストメソッドの構造は、前準備、実行、検証、(後片付け)の順で書くのが一般的
- TDDでは、逆でテストメソッドの構造は、ゴールから書いていく

## ユニットテストの実行

```
(venv)$ python3 -m unittest tests.test_main
```

##　TODOをさらに詳細にする

#### 正常系
- [ ] 数を文字列にして返す
    - [x] 1を渡したら文字列'1'を返す
    - [ ] 2を渡したら文字列'2'を返す

#### 準正常系
- [ ] 3の倍数のときは数の代わりに「Fizz」と返す
- [ ] 5の倍数のときは「Buzz」と返す
- [ ] 3と5両方の倍数の場合には、「FizzBuzz」と返す
#### その他
- [ ] 1から100までの数
- [ ] プリントする
