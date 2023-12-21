import cv2
import os
def Canny_recognition(img_test):
    img = cv2.imread(img_test,0)
    after_edges = cv2.Canny(img,100,200)
    new_dir = 'static'
    #os.makedirs(new_dir,exist_ok=True)
    cv2.imwrite(os.path.join('new_dir', 'after.png'),after_edges)
    