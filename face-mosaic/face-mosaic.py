import cv2


# 画像読み込み
image = cv2.imread("mosaic-sample.jpg")


# 顔検出器の読み込み
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


# 画像をグレースケールに変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 顔の検出
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


# 各顔にモザイクをかける
for (x, y, w, h) in faces:
    # 顔の領域を切り抜く
    face = image[y:y+h, x:x+w]


    # モザイク処理
    face = cv2.resize(face, (10, 10), interpolation=cv2.INTER_LINEAR)
    face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)


    # モザイクをかけた顔を元の画像に貼り付ける
    image[y:y+h, x:x+w] = face


# モザイクをかけた画像を保存
cv2.imwrite("mosaic-output.jpg", image)