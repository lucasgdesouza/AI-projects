README trabalho 1 - turma A

Lucas Fraga Balbinot - 00585249

Lucas Gomes de Souza - 00580466

Exercício 1:

Valores iniciais que resultaram na melhor execução da regressão linear:

b = 0; w = 0; alpha = 0.01; num_iterations = 800;

Melhor erro quadrático médio = 8.534952236591986

Conclusões: 
  Concluímos que há diversas formas de implementar as funções requisitadas, e muitas são boas (convergem e encontram a reta adequada ao dataset). Dessa forma, com uma implementação boa, realmente não há razão para se preocupar com os valores de b e w, uma vez que o algoritmo irá encontrar uma reta que faça um bom ajuste. Ainda assim, foi necessário testar diferentes valores para o alpha e o num_iterations. Tanto um alpha muito pequeno (< 0.001) quanto um muito grande (> 0.1) resultaram num gráfico divergente, o que nos levou a considerar o valor 0.01 como a melhor opção. Ao passo que, para o num_iterations, valores menores que 100 convergiram, porém lentamente. Enquanto valores maiores do que 800 não alteraram a reta significativamente para compensar o número de iterações. Em suma, escolhemos o valor 800, o qual adequou a reta ao dataset e compensou o número de iterações, convergindo, na nossa visão, melhor do que nas demais escolhas.

Exercício 2:

**Trabalho_redes_neurais - Características de Datasets**

MNIST - 28x28x1 (Grayscale), 10 classes (Números de 0 a 9), 70000 amostras (60000 de treino, 10000 de teste)

Fashion MNIST - 28x28x1 (Grayscale), 10 classes(Baseadas em tipos de roupas), 70000 amostras (60000 de treino, 10000 de teste)

Cifer 10 - 32x32x3 (Colorida), 10 classes, 60000 amostras (50000 de treino, 10000 de teste)

Cifer 100 - 32x32x3 (Colorida), 20 classes, 60000 amostras (50000 de treino, 10000 de teste)

**Seção de testes**

Aqui serão listados alguns testes feitos nos datasets, com cinco para cada caso. A configuração inicial de cada dataset é explicitamente baseada no exemplo de cifar10 providenciado préviamente pelo professor, com modificações nas escalas de cor e classes dependendo das necessidades de cada caso. Quaisquer mudanças de configuração serão observadas nos datasets que seguirem. Cada dataset rodará por 10 epochs.

**Testes de Cifar10**

Dataset 1 - Configuração "padrão". Acurácia calculada: 64,25%. Tempo total de execução: 6 minutos e 40 segundos

Dataset 2 - Modificação em pooling, dobrando suas proporções originais para [4,4].  Acurácia calculada: 64,82%. Tempo total de execução: 6 minutos e 12 segundos.

Dataset 3 - Modificação em pooling, reduzindo suas proporções originais para [1,1]. Acurácia calculada: 57,88%. Tempo total de execução: 12 minutos e 58 segundos.

Dataset 4 - Pooling retornado a [2,2]. Aumentar número de neurônios em dense para dobro do original. Acurácia calculada: 65,77%. Tempo total de execução: 10 minutos e 48 segundos.

Dataset 5 - Reduzir número de neurônios de dense pela metade do original. Acurácia calculada: 60,89%. Tempo total de execução: 6 minutos e 32 segundos.

Conclusões de teste: Este primeiro teste foi voltado a analisar alguns elementos básicos do sistema, e como alterá-los permite afetar o cálculo da acurácia. Pelos dados iniciais, o Pooling aparenta possuir uma relação inversa para tempo e diretamente proporcional para Acurácia: ou seja,poolings maiores aparentam ser mais precisos e mais rápidos, e menores mais lentos e imprecisos. Quanto a neurônios, um número reduzido deles parece indicar um tempo menor de execução, enquanto que um maior aparenta demonstrar mais tempo, com o tempo menor possuindo menor precisão e o maior maior precisão, indicando proporcionalidade entre os elementos.

**Testes de Cifar100**

Dataset 1 - Configuração "padrão": Acurácia calculada: 13,30%. Tempo total de execução: 1 minuto e 20 segundos.

Dataset 2 - Para verificar se as conclusões vistas anteriormente em Cifar10 se aplicam aqui, iremos dobrar o pooling e os neurônios. Acurácia calculada: 18,27%. Tempo total de execução: 1 minuto e 17 segundos.

Dataset 3 - Agora, iremos reverter as mudanças do sistema para o estado original e criar uma segunda camada Pooling2D igual à primeira. Acurácia calculada: 16,38%. Tempo total de execução: 1 minuto e 16 segundos.

Dataset 4 - Agora retiramos uma camada pool e testamos o que ocorre se houver duas camadas de 64 neurônios. Acurácia calculada: 18,16%. Tempo total de execução: 1 minuto e 28 segundos.

Dataset 5 - Com essas considerações, tentemos combinar as propostas de 3 e 4 para ver o que ocorre. Acurácia calculada: 18,01%. Tempo total de execução: 1 minuto e 15 segundos.

Conclusões de teste: Como notado previamente, as conclusões de Cifar10 aparentam carregar para o Cifar100 sem grandes divergências. Apesar disso, notavelmente não há grande diferença de tempo entre cada caso comparado com os casos de Cifar10: pesquisa em outros materiais indica que o número maior de divisões de Cifar100 pode ser responsável por essa situação, diluindo a porcentagem para a condição atual. Sendo assim, Cifar10 seria certamente mais "fácil" que Cifar100.

**Testes de Minst**
