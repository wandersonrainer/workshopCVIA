import cv2
import numpy as np

#abre a webcam do sistema
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame")
        break

    #ponto central da imagem
    altura, largura, _ = frame.shape
    centro_x, centro_y = largura // 2, altura // 2

    #extrai os valores BGR do ponto central (OpenCV usa BGR)
    b, g, r = frame[centro_y, centro_x]

    #marca o ponto central na imagem
    cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 0), -1)

    #exibe os valores R, G e B na tela (invertendo BGR para RGB)
    texto = f"R: {r}  G: {g}  B: {b}"
    cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    #imagem em tempo real
    cv2.imshow('RGB em tempo real - Q para sair', frame)

    #fecha janela grafica
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#libera a camera e fecha a janela
cap.release()
cv2.destroyAllWindows()
