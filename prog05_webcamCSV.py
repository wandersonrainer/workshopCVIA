import cv2

#abre a webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

print("\nINSTRUCOES:")
print("Posicione o objeto no centro da imagem e pressione:")
print("   V - vermelho")
print("   A - azul")
print("   E - verde")
print("   L - laranja")
print("   P - preto")
print("   B - branco")
print("   X - vazio (sem cor definida)")
print("   Q - sair\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    altura, largura, _ = frame.shape
    centro_x, centro_y = largura // 2, altura // 2

    #obtem valores BGR do ponto central
    b, g, r = frame[centro_y, centro_x]

    #mostra a imagem com ponto central marcado
    cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 0), -1)
    cv2.putText(frame, "Pressione a tecla da cor", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.imshow("Coleta RGB - Pressione a tecla", frame)

    tecla = cv2.waitKey(1) & 0xFF

    if tecla == ord('q'):
        break
    elif tecla == ord('v'):
        print(f"{r},{g},{b},vermelho")
    elif tecla == ord('a'):
        print(f"{r},{g},{b},azul")
    elif tecla == ord('e'):
        print(f"{r},{g},{b},verde")
    elif tecla == ord('l'):
        print(f"{r},{g},{b},laranja")
    elif tecla == ord('p'):
        print(f"{r},{g},{b},preto")
    elif tecla == ord('b'):
        print(f"{r},{g},{b},branco")
    elif tecla == ord('x'):
        print(f"{r},{g},{b},vazio")

cap.release()
cv2.destroyAllWindows()
