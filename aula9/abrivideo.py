import cv2

video = cv2.VideoCapture('videogravado.avi')

if video.isOpened() == False:
    print('Erro ao abrir o video')


while video.isOpened():
   ret, frame = video.read()

   if ret == True:
     cv2.imshow('frame', frame)
       
     if cv2.waitKey(5) & 0xFF == ord('s'):
       break
         
   else:
       break

video.release()
cv2.destroyAllWindows()