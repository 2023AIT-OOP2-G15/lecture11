import cv2

filename = 'frame-sample.png'
    
# 画像ファイルパスから読み込み
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 顔検出用の学習済みモデルを読み込む
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 顔の検出
# 画像に対して顔のサイズが大きいとうまく検出できない
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 検出された顔に枠を描画
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

#画像を保存
cv2.imwrite("frame.png",img)

# 画像の表示(確認用)
 #cv2.imshow("Image", img)
# キー入力待ち(ここで画像が表示される)
#cv2.waitKey()