import numpy as np

# Fonction pour calculer le prix d'une option Call américaine avec la méthode des arbres binomiaux
def binomial_tree_american_call(S, K, T, r, vol, N):
    # Calcul du pas de temps
    dt = T / N
    # Calcul des facteurs de montée et de descente
    u = np.exp(vol * np.sqrt(dt))
    d = 1 / u
    # Probabilité neutre au risque
    p = (np.exp(r * dt) - d) / (u - d)

    # Initialisation des prix à l'échéance
    prices = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        prices[i, N] = S * (u ** (N - i)) * (d ** i)

    # Initialisation des payoffs à l'échéance
    call_values = np.maximum(prices[:, N] - K, 0)

    # Remonter l'arbre pour calculer les prix des options
    for j in range(N - 1, -1, -1):
        for i in range(j + 1):
            early_exercise = prices[i, j] - K
            hold = np.exp(-r * dt) * (p * call_values[i] + (1 - p) * call_values[i + 1])
            call_values[i] = np.maximum(early_exercise, hold)
            prices[i, j] = S * (u ** (j - i)) * (d ** i)

    return call_values[0]

# Fonction pour calculer le prix d'une option Put américaine avec la méthode des arbres binomiaux
def binomial_tree_american_put(S, K, T, r, vol, N):
    # Calcul du pas de temps
    dt = T / N
    # Calcul des facteurs de montée et de descente
    u = np.exp(vol * np.sqrt(dt))
    d = 1 / u
    # Probabilité neutre au risque
    p = (np.exp(r * dt) - d) / (u - d)

    # Initialisation des prix à l'échéance
    prices = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        prices[i, N] = S * (u ** (N - i)) * (d ** i)

    # Initialisation des payoffs à l'échéance
    put_values = np.maximum(K - prices[:, N], 0)

    # Remonter l'arbre pour calculer les prix des options
    for j in range(N - 1, -1, -1):
        for i in range(j + 1):
            early_exercise = K - prices[i, j]
            hold = np.exp(-r * dt) * (p * put_values[i] + (1 - p) * put_values[i + 1])
            put_values[i] = np.maximum(early_exercise, hold)
            prices[i, j] = S * (u ** (j - i)) * (d ** i)

    return put_values[0]

# Variables pour les tests
S = 42  # Prix du sous-jacent
K = 40  # Prix d'exercice
T = 0.5  # Temps jusqu'à l'échéance (en années)
r = 0.1  # Taux sans risque (annualisé)
vol = 0.2  # Volatilité (annualisée)
N = 100  # Nombre de pas dans l'arbre binomial

# Calcul du prix de l'option Call américaine
call_price = binomial_tree_american_call(S, K, T, r, vol, N)

# Calcul du prix de l'option Put américaine
put_price = binomial_tree_american_put(S, K, T, r, vol, N)

# Affichage des résultats
print(f"Le prix de l'option Call américaine est: {call_price:.2f}")
print(f"Le prix de l'option Put américaine est: {put_price:.2f}")

