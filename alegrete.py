import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    n = len(data)   # número de observações
    total_error = 0
    
    for i in range(n):
        x = data[i][0]  # área
        y = data[i][1]  # preço real
        
        y_pred = b + w * x   # valor previsto pela regressão
        error = (y - y_pred) ** 2  # erro quadrático dessa entrada
        
        total_error += error  # acumula os erros
    
    mse = total_error / n  # média dos erros quadráticos
    return mse


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    n = len(data)
    b_gradient = 0
    w_gradient = 0
    
    # calcula os gradientes somando contribuição de cada ponto
    for i in range(n):
        x = data[i][0]
        y = data[i][1]
        y_pred = b + w * x
        error = y - y_pred
        
        b_gradient += -2 * error
        w_gradient += -2 * x * error
    
    # tira a média
    b_gradient /= n
    w_gradient /= n
    
    # atualiza parâmetros
    b = b - alpha * b_gradient
    w = w - alpha * w_gradient
    
    return b, w


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
     # listas para guardar os valores de b e w a cada época
    b_history = [b]
    w_history = [w]
    
    for i in range(num_iterations):
        # atualiza b e w usando uma iteração da descida do gradiente
        b, w = step_gradient(b, w, data, alpha)
        
        # guarda os novos valores
        b_history.append(b)
        w_history.append(w)
    
    return b_history, w_history
