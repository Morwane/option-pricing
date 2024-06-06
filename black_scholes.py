import math
from scipy.stats import norm

# Définir les variables
S = 42  # Prix du sous-jacent
K = 40  # Prix d'exercice
T =1  # Temps jusqu'à l'échéance (en années)
r = 0.1  # Taux sans risque (annualisé)
vol=0.6  # Volatilité (σ/sigma, annualisée)

# Formule pour d1
# d1 est une variable intermédiaire utilisée dans le modèle Black-Scholes
# Elle tient compte du prix actuel du sous-jacent, du prix d'exercice, du temps jusqu'à l'échéance,
# du taux sans risque et de la volatilité
d1 = (math.log(S / K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))

# Formule pour d2
# d2 est une autre variable intermédiaire dans le modèle Black-Scholes
# Elle est simplement d1 diminuée de la volatilité ajustée pour le temps
d2 = d1 - vol * math.sqrt(T)

# Calculer le prix d'un Call
# La formule Black-Scholes pour une option d'achat européenne
# S * norm.cdf(d1) est la valeur attendue du sous-jacent actualisée
# K * math.exp(-r * T) * norm.cdf(d2) est la valeur actualisée de l'exercice de l'option
C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

# Afficher le prix de l'option Call
print(f"Le prix de l'option Call est: {C:.2f}")

# Calculer le prix d'un Put
# La formule Black-Scholes pour une option de vente européenne
# K * math.exp(-r * T) * norm.cdf(-d2) est la valeur actualisée de l'exercice de l'option
# S * norm.cdf(-d1) est la valeur attendue du sous-jacent actualisée
P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Afficher le prix de l'option Put
print(f"Le prix de l'option Put est: {P:.2f}")

# Fonction pour calculer le prix d'une option Call européenne avec le modèle Black-Scholes
def black_scholes_call(S, K, T, r, vol):
    d1 = (math.log(S / K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))
    d2 = d1 - vol * math.sqrt(T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

# Fonction pour calculer le prix d'une option Put européenne avec le modèle Black-Scholes
def black_scholes_put(S, K, T, r, vol):
    d1 = (math.log(S / K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))
    d2 = d1 - vol * math.sqrt(T)
    return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Calculer le prix des options en utilisant les fonctions
call_price = black_scholes_call(S, K, T, r, vol)
put_price = black_scholes_put(S, K, T, r, vol)

# Afficher les résultats des fonctions
print(f"Le prix de l'option Call européenne avec fonction est: {call_price:.2f}")
print(f"Le prix de l'option Put européenne avec fonction est: {put_price:.2f}")
