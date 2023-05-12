from PIL import Image
import cv2
import numpy as np

# 画像を読み込み
img1 = Image.open('result_1.jpg').convert('RGBA')
img2 = Image.open('result_2.JPG').convert('RGBA')
img3 = Image.open('result_3.jpg').convert('RGBA')
img4 = Image.open('result_4.jpg').convert('RGBA')

# 画像をリサイズ
img1 = img1.resize((800, 600))
img2 = img2.resize((800, 600))
img3 = img3.resize((800, 600))
img4 = img4.resize((800, 600))

# 透過を50%にして重ね合わせる
new_img = Image.blend(img1, img2, 0.5)
new_img = Image.blend(new_img, img3, 0.5)
new_img = Image.blend(new_img, img4, 0.5)

# OpenCVの画像形式に変換
cv_img = cv2.cvtColor(np.asarray(new_img), cv2.COLOR_RGB2BGR)

# グレースケールに変換
gray_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

# ヒストグラム平坦化を適用する
equalized_img = cv2.equalizeHist(gray_img)

# 画像を保存
cv2.imwrite('result_a.png', equalized_img)