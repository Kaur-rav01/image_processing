import cv2
img=cv2.imread(r'C:\Users\DELL\Downloads\source.png')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaussBlur=cv2.GaussianBlur(gray_img,(21,21),0)  #gray image as input for blur image
threshold_img=cv2.threshold(gray_img,150,255,cv2.THRESH_BINARY)[1] #thresholding image means sketching  #blur image as input for thresholding image ... 
#dst=cv2.threshold(src,thresholdvalue,maximum threshold value,binary type)[1] #[1] pass image in next line
cv2.imshow("threshold image",threshold_img)
cv2.imshow("guassian iamge",gaussBlur)
cv2.imshow("gray image",gray_img)
cv2.imshow("original image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()