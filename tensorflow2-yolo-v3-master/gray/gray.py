import cv2

# 画像を読み込みます。
path = 'input1.jpg'
img = cv2.imread(path)

# 画像を加工します。
# 例えば、以下のようにすると、画像をグレースケールに変換できます。
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 画像を保存します。
cv2.imwrite('output1.jpg', gray_img)
