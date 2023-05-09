from PIL import Image

# 画像ファイルを開く
im = Image.open('10m_back_f.jpg')

# 画像サイズを変更する
new_im = im.resize((40, 80))

# 変更後の画像を保存する
new_im.save('new_image.jpg')
