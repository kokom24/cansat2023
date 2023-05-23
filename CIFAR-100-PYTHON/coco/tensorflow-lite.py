import tensorflow as tf

# TensorFlowモデルを読み込む
loaded_model = tf.keras.models.load_model('model_mobile.h5')

# TensorFlow Lite Converterを作成
converter = tf.lite.TFLiteConverter.from_keras_model(loaded_model)

# 変換オプションを設定（例: オプティマイズ、量子化）
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]

# TensorFlow Liteモデルに変換
tflite_model = converter.convert()

# TensorFlow Liteモデルを保存
with open('model_mobile.tflite', 'wb') as f:
    f.write(tflite_model)

print("1")