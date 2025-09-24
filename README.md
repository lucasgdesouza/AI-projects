README trabalho 1 - turma A

Lucas Fraga Balbinot -

Lucas Gomes de Souza - 00580466

Exercício 1:

Valores iniciais que resultaram na melhor execução da regressão linear:

b = 0; w = 0; alpha = 0.01; num_iterations = 800;

Melhor erro quadrático médio = 8.534952236591986

Conclusões: 
  Concluímos que há diversas formas de implementar as funções requisitadas, e muitas são boas (convergem e encontram a reta adequada ao dataset). Dessa forma, com uma implementação boa, realmente não há razão para se preocupar com os valores de b e w, uma vez que o algoritmo irá encontrar uma reta que faça um bom ajuste. Ainda assim, foi necessário testar diferentes valores para o alpha e o num_iterations. Tanto um alpha muito pequeno (< 0.001) quanto um muito grande (> 0.1) resultaram num gráfico divergente, o que nos levou a considerar o valor 0.01 como a melhor opção. Ao passo que, para o num_iterations, valores menores que 100 convergiram, porém lentamente. Enquanto valores maiores do que 800 não alteraram a reta significativamente para compensar o número de iterações. Em suma, escolhemos o valor 800, o qual adequou a reta ao dataset e compensou o número de iterações convergindo, na nossa visão, melhor do que nas demais escolhas.

Exercício 2:

**Trabalho_redes_neurais - Características de Datasets**

MNIST - 28x28x1 (Grayscale), 10 classes (Números de 0 a 9), 70000 amostras (60000 de treino, 10000 de teste)

Fashion MNIST - 28x28x1 (Grayscale), 10 classes(Baseadas em tipos de roupas), 70000 amostras (60000 de treino, 10000 de teste)

Cifer 10 - 32x32x3 (Colorida), 10 classes, 60000 amostras (50000 de treino, 10000 de teste)

Cifer 100 - 32x32x3 (Colorida), 20 classes, 60000 amostras (50000 de treino, 10000 de teste)
