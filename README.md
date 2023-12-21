# 各メンバーの役割

|役割|名前(k00000)|内容|
|---|---|---|
|Web|北沢直暉(k22044)|アップロード画像、画像処理済み閲覧|
|Web|胡田哲志(k22024)|ファイルダウンロードンターフェース|
|画像処理|大屋萌奈(k22027)|リーダー、READサポートなど|
|画像処理|加藤大地(k22035)|顔検出して枠で囲う|
|画像処理|青島巧典(k22003)|ディレクトリ監視から角画像処理呼び出しをするプログラム|
|画像処理|佐伯祐人(k22058)|Cannyフィルタによる輪郭抽出|
|画像処理|西田拓磨(k21092)|顔検出してモザイク|

#　決め事
```
lecture11
├─ static
│   ├─ style.css
│   │
│   ├─ processed
│   │    ├─ Mosaic
│   │    ├─ Frame
│   │    ├─ Carry
│   │    ├─ Grayscale
│   │
│   └─ uploads
│        ├─ Mosaic
│        ├─ Frame
│        ├─ Carry
│        ├─ Grayscale
│
├─ temolates
│   └─ index.html
│
├─ function
│   ├─ MosaicImg.py
│   ├─ FrameImg.py
│   ├─ CarryImg.py
│   ├─ GrayscaleImg.py
│
├─ main.py
├─ README.md
├─ .DS_Store
├─ .python-version
├─ 

```
- 加工した画像は ../static/uploads/xxx/xxx.png に保存してください
Mosaic = モザイク画像
Frame  = 枠
Carry  = Carryフィルタ
Grayscale = グレースケール

- 保存した加工前の画像は ../static/processed/xxx/xxx.png に保存してください
Mosaic = モザイク画像
Frame  = 枠
Carry  = Carryフィルタ
Grayscale = グレースケール

- 関数名
モザイク画像 MosaicImg()
枠 FrameImg()
Carryフィルタ CarryImg()
グレースケール　GrayscaleImg()

- 画像名
モザイク画像 MosaicImg
枠 FrameImg
Carryフィルタ CarryImg
グレースケール　GrayscaleImg




## システムの動作確認方法
ここからmainを確認できます
<https://github.com/2023AIT-OOP2-G15/lecture11>

動かしたい場合は、ブランチをmainにしてターミナルで起動

## 使用するライブラリのバージョン



<!-- 
# メモ 
|画像処理|大屋萌奈(k22027)|顔検出してモザイク|
|画像処理|加藤大地(k22035)|顔検出して枠で囲う|
|画像処理|青島巧典(k22003)|Cannyフィルタによる輪郭抽出|
|画像処理|佐伯祐人(k22058)|画像のグレースケール化(できれば２値化も)|
|画像処理|西田拓磨(k21092)|計算済み機械学習モデルの用いた物体検出と画像ないへの名前の埋め込み(機械学習モデルのライブラリはなんでも良い)|
-->