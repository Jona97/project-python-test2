import joblib
import numpy as np
# Simulating a big array for a model or large dataset
#big_array = np.zeros((1000, 1000))
# Save
#joblib.dump(big_array, 'model_test.joblib', compress=3)
# Load
modelo_cargado = joblib.load('model_test.joblib')
print(modelo_cargado.shape)