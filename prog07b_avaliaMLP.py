import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

#carregamento do dataset
df = pd.read_csv("datasetCSV.csv")
X = df[['r', 'g', 'b']]
y = df['label']

#divisao em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#criacao e treinamento do MLP
modelo = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)

#avaliacao
y_pred = modelo.predict(X_test)
print("Relatório de Classificacao:\n", classification_report(y_test, y_pred))

#matriz de confusao
matriz = confusion_matrix(y_test, y_pred, labels=modelo.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=matriz, display_labels=modelo.classes_)
disp.plot(cmap='Oranges')
plt.title("Matriz de Confusao - MLP")
plt.show()
