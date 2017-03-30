# Regalias: [Elona](http://ylvania.org/elona)-like alias generator

:jp: Currently, it only supports to generate Japanese aliases.

**Example**

```sh
$ regalias  # 引数を渡さずに実行すると...
王国の記憶  # 異名をランダムに生成します

$ regalias
結末の水平線  # != 王国の記憶

$ regalias
やさしすぎた略奪者
```

```sh
$ regalias @  # 引数に名前を渡して実行すると...
奇跡を呼ぶ幻術使い @  # その名前に対応する異名を生成します

$ regalias マニ
ダイヤモンドの妹 マニ  # !?

$ regalias エヘカトル
ザ・ヒットマン エヘカトル  # うみみゃぁ！

$ regalias エヘカトル
ザ・ヒットマン エヘカトル  # 名前付き異名の生成結果は常に同一です！
```


### :gem: Usage

```sh
usage: regalias [-h] [--version] [name]

Elonalike Alias Generator

positional arguments:
  name        seed of alias

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```


### :gem: Thanks

Special thanks to [Noa (aka Rfish)](http://ylvania.org) for giving license to use Elona's ndata in this project.


### :panda_face: Author

| [![Letla Fox](https://github.com/letla.png?size=96)](https://www.letla.net) |
|:---:|
| [Letla Fox](https://www.letla.net) |


### :gem: License

Apache License 2.0
