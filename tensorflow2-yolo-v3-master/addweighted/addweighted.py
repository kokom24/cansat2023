import cv2

# 2つの画像を読み込む
path1='human_1.jpg'
path2='dummy_8.jpg'
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
#3枚以上の場合
    #path1='human_1.jpg'
    #path2='dummy_8.jpg'
    #path3='image_3.jpg'
    #etc...
    #img1 = cv2.imread(path1)
    #img2 = cv2.imread(path2)
    #img3 = cv2.imread(path3)
    #etc...


# 画像1の大きさに合わせて、画像2のサイズを変更する
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
#3枚以上の場合
    #smallest_height = min(img1.shape[0], img2.shape[0], img3.shape[0],etc...)
    #smallest_width = min(img1.shape[1], img2.shape[1], img3.shape[1],etc...)
    #img1 = cv2.resize(img1, (smallest_width, smallest_height))
    #img2 = cv2.resize(img2, (smallest_width, smallest_height))
    #img3 = cv2.resize(img3, (smallest_width, smallest_height))
    #etc...


# 画像を重ね合わせる
result = cv2.addWeighted(img1, 0.5, img2, 0.3, 0)
#3枚以上の場合
    #result = cv2.addWeighted(img1, 0.5, img2, 0.3, 0)
    #result = cv2.addWeighted(result, 0.5, img3, 0.2, 0)
    #etc...



# 結果画像を新しいファイルとして保存する
cv2.imwrite('result.jpg', result)

