
import os
import tensorflow as tf
if tf.test.is_gpu_available():
    print('GPU is available-----------------------------------------')
else:
    print("GPU is not available+++++++++++++++++++++++++++++++++++++++++++++++")
'''
# 创建一个随机 tensor 数组
random_tensor = tf.random_uniform([5, 5], minval=0, maxval=1)

# 将 tensor 发送到 GPU
with tf.device('/gpu:0'):
    random_tensor_gpu = tf.identity(random_tensor)

# 运行并输出 tensor 的设备
with tf.Session() as sess:
    result = sess.run(random_tensor_gpu)
    print("Random Tensor:")
    print(result)
    print("Device for random_tensor_gpu:", random_tensor_gpu.device)
'''
