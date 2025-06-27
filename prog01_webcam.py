import cv2

#abre a webcam do sistema
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame")
        break

    #mostra o video em tempo real
    cv2.imshow('Webcam - Pressione Q para sair', frame)

    #sai do loop se apertar a tecla q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#libera a camera e fecha a janela
cap.release()
cv2.destroyAllWindows()