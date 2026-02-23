import pickle
data = {'id': 1, 'nombre': 'ejemplo', 'valores': [10, 20, 30]}
#Save
#with open('datos.pkl', 'wb') as f:
#    pickle.dump(data, f)
# Load
with open('datos.pkl', 'rb') as f:
    data_cargada = pickle.load(f)
    print(data_cargada)