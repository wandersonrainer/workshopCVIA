import cv2
import numpy as np

#abre a webcam do sistema
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

#funcao para mapear valor RGB para nome de cor
def detectar_cor(r, g, b):
    if r > 120 and g > 120 and b > 120:
        return "Branco"
    elif r < 20 and g < 20 and b < 20:
        return "Preto"
    elif r > 100 and g < 40 and b < 40:
        return "Vermelho"
    elif r > 150 and g > 50 and b < 20:
        return "Laranja"
    elif r < 50 and g > 70 and b < 50:
        return "Verde"
    elif r < 10 and g < 80 and b > 70:
        return "Azul"
    else:
        return "Desconhecida"

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame")
        break

    #ponto central da imagem
    altura, largura, _ = frame.shape
    centro_x, centro_y = largura // 2, altura // 2

    #extrai valores BGR do ponto central
    b, g, r = frame[centro_y, centro_x]

    #detecta cor com base em RGB
    nome_cor = detectar_cor(r, g, b)

    #marca o ponto central e mostra o nome da cor
    cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 0), -1)
    cv2.putText(frame, f"Cor: {nome_cor}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)



    #imagem em tempo real
    cv2.imshow('Deteccao de cor (RGB) - Q para sair', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#libera a camera e fecha a janela
cap.release()
cv2.destroyAllWindows()
