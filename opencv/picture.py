#cv2をインポート
import cv2

#"hisyo.jpg"を変数"filename"に代入
filename = "hisyo.jpg"
#ファイルから画像データを読み込む関数
img = cv2.imread(filename)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
#画像をウィンドウに表示する関数
cv2.imshow("image", img)
#キーイベントを待つ関数。0の場合はキーが押されるまで待つ）
cv2.waitKey(0)
