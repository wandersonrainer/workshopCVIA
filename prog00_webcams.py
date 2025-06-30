import cv2

for i in range(6):  #testa as cameras de 0 a 5
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Webcam encontrada no indice: {i}")
        cap.release()
    else:
        print(f"Nenhuma webcam no indice: {i}")
