import base64

import cv2
import numpy as np
import requests
from db.landmarks import get_image_url
from usecases.firebase import fetch_landmark_image


def convert_binary_to_ndarray(binary):
    npimg = np.fromstring(binary, dtype=np.uint8)
    img = cv2.imdecode(npimg, 1)
    return img


def decode_base64_to_ndarray(image):
    img_binary = base64.b64decode(image)
    img = convert_binary_to_ndarray(img_binary)
    return img


def image_processing(image):
    resize_img = cv2.resize(image, (500, 500))
    gray_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
    return gray_img


def calc_image_similarity(user_base64_image, landmark_id):

    user_image = decode_base64_to_ndarray(user_base64_image)
    user_compare_image = image_processing(user_image)

    origin_filename = get_image_url(landmark_id)['img_path']
    origin_raw_image = fetch_landmark_image(origin_filename)
    origin_image = convert_binary_to_ndarray(origin_raw_image)
    origin_compare_image = image_processing(origin_image)

    # AKAZE検出器を使う
    akaze = cv2.AKAZE_create()

    # kpが特徴量, desが特徴量ベクトル
    kp1, des1 = akaze.detectAndCompute(user_compare_image, None)
    kp2, des2 = akaze.detectAndCompute(origin_compare_image, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 特徴量ベクトル同士をBrute-Forceでマッチング
    matches = bf.match(des1, des2)

    # 距離が100以下のものだけを抽出
    dist = [m.distance for m in matches if m.distance < 100]

    # 特徴量のマッチ数が0のとき、無限を返す
    if len(dist) == 0:
        return float('inf')

    # 類似度を計算する
    ret = sum(dist) / len(dist)

    return ret
