import os
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# cv2.imread("Amanda_Bynes/Amanda_Bynes_0004.jpg")

cmd = f"python get_embd.py  --config_path=./configs/config_ms1m_100.yaml \
        --model_path=config_ms1m_100_1006k/checkpoint  \
        --read_path=Amanda_Bynes/Amanda_Bynes_0004.jpg \
        --save_path=embd.pkl"

os.system(cmd)