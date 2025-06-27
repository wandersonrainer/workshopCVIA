import cv2
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

#carrega dataset com amostras rotuladas
df = pd.read_csv("datasetCSV.csv")

#prepara os dados
X = df[['r', 'g', 'b']]
y = df['label']

#treina o classificador KNN
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

#inicia a webcam
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    altura, largura, _ = frame.shape
    centro_x, centro_y = largura // 2, altura // 2
    b, g, r = frame[centro_y, centro_x]

    #usa a IA para prever a cor
    entrada = pd.DataFrame([[r, g, b]], columns=['r', 'g', 'b'])
    cor_prevista = modelo.predict(entrada)[0]

    #mostra resultado na imagem
    cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 0), -1)
    cv2.putText(frame, f"IA: {cor_prevista}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    cv2.imshow('Deteccao com IA (KNN)', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
