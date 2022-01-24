import numpy as np

import cv2

# 图片匹配返回1 不匹配返回0


def match_img_knn(queryImage, trainingImage, thread=0):
    """
    判断图片是否匹配

    :param queryImage: 待匹配的图片
    :param trainingImage: 模板图片
    :returns: 1 匹配
              0 不匹配
    :raises keyError: raises an exception
    """
    sift = cv2.xfeatures2d.SIFT_create()  # 创建sift检测器
    kp1, des1 = sift.detectAndCompute(queryImage, None)
    kp2, des2 = sift.detectAndCompute(trainingImage, None)
    # print(len(kp1))
    # 设置Flannde参数
    FLANN_INDEX_KDTREE = 1
    indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    searchParams = dict(checks=50)
    flann = cv2.FlannBasedMatcher(indexParams, searchParams)
    matches = flann.knnMatch(des1, des2, k=2)

    good = []

    # 设置好初始匹配值
    matchesMask = [[0, 0] for i in range(len(matches))]
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.1 * n.distance:  # 舍弃小于0.7的匹配结果
            matchesMask[i] = [1, 0]
            good.append(m)

    # s = sorted(good, key=lambda x: x.distance)

    drawParams = dict(matchColor=(0, 0, 255), singlePointColor=(
        255, 0, 0), matchesMask=matchesMask, flags=0)  # 给特征点和匹配的线定义颜色
    resultimage = cv2.drawMatchesKnn(
        queryImage,
        kp1,
        trainingImage,
        kp2,
        matches,
        None,
        **drawParams)  # 画出匹配的结果
    cv2.imshow('res', resultimage)
    cv2.waitKey(0)


    # print(len(good),thread)
    if len(good) > thread:
        # maxLoc = kp2[s[0].trainIdx].pt
        return 1
    else:
        return 0


def get_img_w_h(img, minloc):
    """
    计算最大点击坐标

    :param img: 待匹配的图片
    :param minloc: 最小点击位置
    :returns: 最大点击位置
    :raises keyError: raises an exception
    """
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    return width + minloc[0], height + minloc[1]




def match(temple, img):
    """

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    result = cv2.matchTemplate(temple, img, cv2.TM_SQDIFF_NORMED)
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)
    maxloc = get_img_w_h(img, minloc)
    return minloc, maxloc

def print_level(temple,minloc,maxloc):
    # print(minval, maxval, minloc, maxloc)
    cv2.rectangle(temple, minloc, maxloc, (255, 0, 0))
    cv2.imshow('img2', temple)
    cv2.waitKey(0)
if __name__ == "__main__":
    temple = cv2.imread("2691716.bmp", 1)
    img = cv2.imread("1.png", 1)

    if match_img_knn(temple, img):
        minloc, maxloc = match(temple, img)
        print_level(temple, minloc, maxloc)