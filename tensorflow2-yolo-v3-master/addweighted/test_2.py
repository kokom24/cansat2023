import cv2
import numpy as np

# 入力画像を読み込む
img1 = cv2.imread('human_5.jpg')
img2 = cv2.imread('dummy_10.jpg')
img3 = cv2.imread('dummy_8.jpg')

# 画像をグレースケールに変換する
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# 画像をぼかす
blur1 = cv2.GaussianBlur(gray1, (25, 25), 0)
blur2 = cv2.GaussianBlur(gray2, (25, 25), 0)
blur3 = cv2.GaussianBlur(gray3, (25, 25), 0)

# 画像を2値化する
_, threshold1 = cv2.threshold(blur1, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
_, threshold2 = cv2.threshold(blur2, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
_, threshold3 = cv2.threshold(blur3, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# 輪郭を検出する
contours1, _ = cv2.findContours(threshold1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(threshold2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours3, _ = cv2.findContours(threshold3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 最大面積の輪郭を取得する
max_contour1 = max(contours1, key=cv2.contourArea)
max_contour2 = max(contours2, key=cv2.contourArea)
max_contour3 = max(contours3, key=cv2.contourArea)

# 背景を削除するマスクを作成する
mask1 = np.zeros(img1.shape[:2], np.uint8)
cv2.drawContours(mask1, [max_contour1], -1, 255, -1)
mask2 = np.zeros(img2.shape[:2], np.uint8)
cv2.drawContours(mask2, [max_contour2], -1, 255, -1)
mask3 = np.zeros(img3.shape[:2], np.uint8)
cv2.drawContours(mask3, [max_contour3], -1, 255, -1)

# 背景を除いた画像を取得する
result1 = cv2.bitwise_and(img1, img1, mask=mask1)

# 結果画像を保存する
cv2.imwrite('result_1.jpg', result1)

result2 = cv2.bitwise_and(img2, img2, mask=mask2)
cv2.imwrite('result_2.jpg', result2)

result3 = cv2.bitwise_and(img3, img3, mask=mask3)
cv2.imwrite('result_3.jpg', result3)