import cv2
import numpy as np
import requests
import base64
from db.landmarks import get_image_url


def convert_binary_to_ndarray(binary):
    npimg = np.fromstring(binary, dtype=np.uint8)
    img = cv2.imdecode(npimg, 1)
    return img


def decode_base64_to_ndarray(image):
    img_binary = base64.b64decode(image)
    img = convert_binary_to_ndarray(img_binary)
    return img


def calc_image_similarity(user_base64_image, landmark_id):

    user_image = decode_base64_to_ndarray(user_base64_image)

    database_image_url = get_image_url(landmark_id)['img_url']
    database_image_binary = requests.get(database_image_url).content
    database_image = convert_binary_to_ndarray(database_image_binary)

    # A-KAZEとかいう検出器を使う
    akaze = cv2.AKAZE_create()

    # kpが特徴量, desが特徴量ベクトル
    kp1, des1 = akaze.detectAndCompute(user_image, None)
    kp2, des2 = akaze.detectAndCompute(database_image, None)

    bf = cv2.BFMatcher()

    # 特徴量ベクトル同士をBrute-Forceでマッチング
    matches = bf.match(des1, des2)

    dist = [m.distance for m in matches]
    # 類似度を計算する
    ret = sum(dist) / len(dist)

    return ret
