import cloudpickle
# lambda function( standard pickle doesn't always support well)
mi_lambda = lambda x: x ** 2
# Serializing
squared_serialized = cloudpickle.dumps(mi_lambda)
# Loading
#nueva_lambda = cloudpickle.loads(squared_serialized)
#print(nueva_lambda(5)) # Output: 25