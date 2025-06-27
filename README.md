# workshopCVIA
Repositório referente ao workshop realizado no SENAI no dia 30/06/2026.

<img src="https://github.com/wandersonrainer/workshopCVIA/blob/main/fig07.png?raw=true" alt="Texto Alternativo" width="250">

Os códigos disponibilizados aqui são base para o workshop. Os programas e suas funções são:

- **prog00_webcams**: Programa que procura pelas webcams conectadas ao sistema, testando os índices de 0 a 5, e informa no terminal quais estão disponíveis para uso.

- **prog01_webcam**: Exibe o vídeo da webcam em tempo real utilizando OpenCV, permitindo encerrar a visualização ao pressionar a tecla "q".

- **prog02_webcamFOTO**: Captura e salva uma fotografia da webcam quando a barra de espaço é pressionada. O nome do arquivo é gerado automaticamente com base no timestamp.

- **prog03_webcamRGB**: Exibe os valores RGB do pixel central da imagem capturada pela webcam em tempo real, mostrando-os sobrepostos na imagem.

- **prog04_webcamCOR**: Realiza a detecção da cor predominante no ponto central da imagem com base em regras condicionais aplicadas aos valores RGB, classificando a cor como "vermelho", "azul", "verde", etc.

- **prog05_webcamCSV**: Permite coletar dados rotulados para montagem de um dataset. O usuário posiciona o objeto no centro da imagem e pressiona uma tecla associada à cor (ex: v para vermelho), o que imprime no terminal os valores RGB seguidos do rótulo da cor.

- **prog06_webcam_KNN**: Realiza a classificação da cor do ponto central da imagem em tempo real utilizando um modelo de KNN previamente treinado com um dataset CSV. A cor prevista é exibida sobre a imagem.

- **prog06b_avaliaKNN**: Avalia o desempenho do classificador KNN utilizando métricas como acurácia, matriz de confusão e relatório de classificação (precision, recall e f1-score), com divisão do dataset em treino e teste.

- **prog07_webcam_MLP**: Realiza a classificação da cor do ponto central da imagem em tempo real usando um modelo MLP (Perceptron Multicamadas) treinado com dados normalizados. A previsão é exibida sobre o vídeo da webcam.

- **prog07b_avaliaMLP**: Avalia o desempenho do classificador MLP com base no dataset CSV. Exibe relatório de classificação detalhado e a matriz de confusão para visualização da performance por classe.

