import cv2
import matplotlib.pyplot as plt

# 画像の読み込み
img = cv2.imread('result_1.jpg')
img2 = cv2.imread('result_2.jpg')

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ヒストグラムの取得
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])


# ヒストグラムの表示
plt.plot(hist)
plt.plot(hist2)
plt.xlim([0, 256])
plt.show()
