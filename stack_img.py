# %%
# 合併圖片
import cv2
import numpy as np
import glob

# %%



def resize(img):
    return cv2.resize(img,(300, 1000))


# image1 = cv2.imread(f"chamber/1.png")
# image2 = cv2.imread(f"chamber/2.png")
# image3 = cv2.imread(f"chamber/3.png")
# image4 = cv2.imread(f"chamber/4.png")
# image5 = cv2.imread(f"chamber/5.png")

# image6 = cv2.imread(f"chamber/6.png")
# image7 = cv2.imread(f"chamber/7.png")
# image8 = cv2.imread(f"chamber/8.png")
# image9 = cv2.imread(f"chamber/9.png")
# image10 = cv2.imread(f"chamber/10.png")

# image11= cv2.imread(f"chamber/11.png")
# image12 = cv2.imread(f"chamber/12.png")
# image13 = cv2.imread(f"chamber/13.png")
# image14 = cv2.imread(f"chamber/14.png")
# image15 = cv2.imread(f"chamber/15.png")

# image16= cv2.imread(f"chamber/16.png")
# image17 = cv2.imread(f"chamber/17.png")
# image18 = cv2.imread(f"chamber/18.png")
# image19 = cv2.imread(f"chamber/19.png")
# image20 = cv2.imread(f"chamber/20.png")

# image21= cv2.imread(f"chamber/21.png")
# image22 = cv2.imread(f"chamber/22.png")
# image23 = cv2.imread(f"chamber/23.png")
# image24 = cv2.imread(f"chamber/24.png")
# image25 = cv2.imread(f"chamber/25.png")


# vmerge1  = resize(np.vstack((image1, image2, image3, image4, image5)))
# vmerge2  = resize(np.vstack((image6, image7, image8, image9, image10)))
# vmerge3  = resize(np.vstack((image11, image12, image13, image14, image15)))
# vmerge4  = resize(np.vstack((image16, image17, image18, image19, image20)))
# vmerge5  = resize(np.vstack((image21, image22, image23, image24, image25)))

# # vmerge2  = np.vstack((im3, im4))

# hmerge = np.hstack((vmerge1, vmerge2, vmerge3, vmerge4, vmerge5))



# # cv2.imshow("test1", hmerge)
# cv2.imwrite('output.png', hmerge)
# cv2.imshow("All", hmerge)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# %%

image1 = cv2.imread(f"33demo/map_1.png")
image2 = cv2.imread(f"33demo/map_2.png")
image3 = cv2.imread(f"33demo/map_3.png")
image4 = cv2.imread(f"33demo/map_4.png")
image5 = cv2.imread(f"33demo/map_5.png")

image6 = cv2.imread(f"33demo/map_6.png")
image7 = cv2.imread(f"33demo/map_7.png")
image8 = cv2.imread(f"33demo/map_8.png")
image9 = cv2.imread(f"33demo/map_9.png")
image10 = cv2.imread(f"33demo/map_10.png")

image11= cv2.imread(f"33demo/map_11.png")
image12 = cv2.imread(f"33demo/map_12.png")

vmerge1  = resize(np.vstack((image1, image2, image3)))
vmerge2  = resize(np.vstack((image4, image5, image6)))
vmerge3  = resize(np.vstack((image7, image8, image9)))
vmerge4  = resize(np.vstack((image10, image11, image12)))

hmerge = np.hstack((vmerge1, vmerge2, vmerge3, vmerge4))

cv2.imwrite('33demo/output.png', hmerge)
cv2.imshow("All", hmerge)

cv2.waitKey(0)
cv2.destroyAllWindows()

# %%


