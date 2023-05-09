import cv2

# 2つの画像を読み込む
path1='human_1.jpg'
path2='dummy_8.jpg'
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# 画像1の大きさに合わせて、画像2のサイズを変更する
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# 画像を重ね合わせる
result = cv2.addWeighted(img1, 1.0, img2, 0.1, 0)


# 結果画像を新しいファイルとして保存する
cv2.imwrite('result.jpg', result)

