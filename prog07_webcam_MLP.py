import cv2
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import joblib

#carrega o dataset
df = pd.read_csv("datasetCSV.csv")
X = df[['r', 'g', 'b']]
y = df['label']

#normaliza os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#cria e treina o modelo MLP
modelo = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)
modelo.fit(X_scaled, y)

#abre a webcam
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

    #leitura dos valores BGR e converte para RGB
    b, g, r = frame[centro_y, centro_x]

    #prepara entrada com nomes de colunas
    entrada_rgb = pd.DataFrame([[r, g, b]], columns=['r', 'g', 'b'])

    #normaliza a entrada
    entrada_normalizada = scaler.transform(entrada_rgb)

    #predicao com o modelo
    cor_prevista = modelo.predict(entrada_normalizada)[0]

    #exibe resultado na tela
    cv2.circle(frame, (centro_x, centro_y), 5, (0, 0, 0), -1)
    texto = f"IA (MLP): {cor_prevista}"
    cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    #mostra a imagem
    cv2.imshow("Classificacao com IA (MLP)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
