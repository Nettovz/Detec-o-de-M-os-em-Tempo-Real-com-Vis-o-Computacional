import cv2

# Inicialize a captura de vídeo
cap_img = cv2.VideoCapture(0)

# Defina o tamanho desejado para a janela da câmera
largura_desejada = 640
altura_desejada = 480
cap_img.set(cv2.CAP_PROP_FRAME_WIDTH, largura_desejada)
cap_img.set(cv2.CAP_PROP_FRAME_HEIGHT, altura_desejada)

# Defina o zoom desejado (o valor pode variar de acordo com a câmera)
zoom = 2.5
cap_img.set(cv2.CAP_PROP_ZOOM, zoom)

while True:
    # Capture frame a frame
    ret, frame = cap_img.read()

    # Mostre o frame capturado
    cv2.imshow('frame', frame)

    # Saia do loop quando a tecla 's' for pressionada
    if cv2.waitKey(10) & 0xFF == ord('s'):
        break

# Libere o objeto de captura de vídeo e feche todas as janelas
cap_img.release()
cv2.destroyAllWindows()
