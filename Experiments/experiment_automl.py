# load the dataset from pycaret
from pycaret.datasets import
get_data
data = get_data('diamond')

# initialize setup
from pycaret.regression import *
s = setup(data, target = 'Price', transform_target = True, log_experiment = True,
experiment_name = 'diamond')

# compare all models
best = compare_models()

# check feature importance
plot_model(best, plot = 'feature')
           
# finalize the model
final_best = finalize_model(best)

# save model to disk
save_model(final_best, 'diamond-pipeline')

