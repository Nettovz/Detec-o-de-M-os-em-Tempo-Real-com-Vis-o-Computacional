import cv2
import mediapipe as mp

wCAM, hCam = 840, 336


video = cv2.VideoCapture(0)
video.set(3, wCAM)
video.set(4, hCam)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands = 2)
mpDraw = mp.solutions.drawing_utils

while True:
    chek, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pointos = []
    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x*w), int(cord.y*h)
                cv2.putText(img, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 0)

    cv2.imshow("imagem", img)
    cv2.waitKey(5)
