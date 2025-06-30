import cv2
import time  #para gerar nome do arquivo com timestamp

#abre a webcam do sistema
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

print("Pressione a barra de espaco para tirar uma foto.")
print("Pressione a tecla 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame")
        break

    #mostra o video em tempo real
    cv2.imshow('Webcam - Pressione Q para sair | Barra de espaco para foto', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    #salva a imagem se pressionar a barra de espaco
    elif key == 32:  #32 = codigo ASCII da barra de espaco
        nome_arquivo = f"foto_{int(time.time())}.jpg"
        cv2.imwrite(nome_arquivo, frame)
        print(f"Foto salva como {nome_arquivo}")

#libera a camera e fecha a janela
cap.release()
cv2.destroyAllWindows()
