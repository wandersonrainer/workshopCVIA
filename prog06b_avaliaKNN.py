import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#carrega dados
df = pd.read_csv("datasetCSV.csv")
X = df[['r', 'g', 'b']]
y = df['label']

#divide em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#treina modelo
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

#predicao e avaliacao
y_pred = modelo.predict(X_test)

print("Acuracia:", accuracy_score(y_test, y_pred))
print("\nRelatorio de Classificacao:\n", classification_report(y_test, y_pred))

matriz = confusion_matrix(y_test, y_pred, labels=modelo.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=matriz, display_labels=modelo.classes_)
disp.plot(cmap='Blues')
plt.title("Matriz de Confusao - KNN")
plt.show()
