# シフト自動作成アプリの作成

## 概要
- 入力した条件に従い、一月分のシフトを自動で作成します。
- デスクトップバージョンもあります。[こちら](https://github.com/sou0913/shifter)

## 環境
Python 3.6

## 使用技術
- Pythonのフレームワークflaskを用いて作成しました。
- また、開発、デプロイにDockerを使うことに初挑戦しました。

## 制作理由
元々デスクトップバージョンで作成したものを、Webアプリとして作り直しました。
調整を重ね、最終的には実際にシフト制作に携わる方に使っていただくことを目的としています。

## 機能について
- 条件を入力すると、それに合ったシフトが作成されます。

<a href="https://gyazo.com/713b065be3b7d500e1e2df7ded2840b2"><img src="https://i.gyazo.com/713b065be3b7d500e1e2df7ded2840b2.gif" alt="Image from Gyazo" width="400"/></a>

<br>
- デスクトップ版で実装した希望休入力は、今の所未実装となっています。近いうちに実装いたします。
<br>

- 制作したシフト表は、Excelファイルとしてダウンロードできます。

<a href="https://gyazo.com/4ab036180b5e5644486ffc9d96f55b05"><img src="https://i.gyazo.com/4ab036180b5e5644486ffc9d96f55b05.gif" alt="Image from Gyazo" width="400"/></a>

## 制作で学んだこと
- Dockerを用いた開発の流れを知れたことは大きく、今後の開発にも積極的に利用していきたいです。
- Flaskについては、[こちら](https://github.com/sou0913/inu-neko)の犬猫判定アプリに引き続き二度目の利用となったので、だいぶ慣れてきているのを感じます。
