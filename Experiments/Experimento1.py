import os
import mlflow
mlflow.set_tracking_uri(
    "sqlite:///D:/Maestria%20DS/Ciclo%20III/C03_MLOps/Project_example/project-python-test2/mlflow.db"
)

print("CWD:", os.getcwd())
print("tracking_uri:", mlflow.get_tracking_uri())

import mlflow

mlflow.set_experiment("MyExperiment")

with mlflow.start_run(run_name="run_abc"):
    # Params (no se repiten)
    mlflow.log_param("param1", 12)
    mlflow.log_param("param2", 3)

    # Metrics (sí se pueden ir actualizando)
    mlflow.log_metric("foo1", 21)
    mlflow.log_metric("foo2", 22)
    mlflow.log_metric("foo3", 23)

    # Artifact
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Hello world!")
    mlflow.log_artifact("output.txt")