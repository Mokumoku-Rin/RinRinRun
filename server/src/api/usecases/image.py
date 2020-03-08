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

    user_image_color = decode_base64_to_ndarray(user_base64_image)
    user_image_gray = cv2.cvtColor(user_image_color, cv2.COLOR_BGR2GRAY)

    database_image_url = get_image_url(landmark_id)['img_url']
    database_image_binary = requests.get(database_image_url).content
    database_image_color = convert_binary_to_ndarray(database_image_binary)
    database_image_gray = cv2.cvtColor(
        database_image_color, cv2.COLOR_BGR2GRAY)

    # ORB検出器を使う
    orb = cv2.ORB_create()

    # kpが特徴量, desが特徴量ベクトル
    kp1, des1 = orb.detectAndCompute(user_image_gray, None)
    kp2, des2 = orb.detectAndCompute(database_image_gray, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 特徴量ベクトル同士をBrute-Forceでマッチング
    matches = bf.match(des1, des2)

    dist = [m.distance for m in matches]
    # 類似度を計算する
    ret = sum(dist) / len(dist)

    return ret
