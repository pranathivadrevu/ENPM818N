import yaml
import os

# Load YAML file
input_file = "../opentelemetry-demo/kubernetes/opentelemetry-demo.yaml"
output_dir = "k8s-deployment"

# Define folders for resource types
resource_folders = {
    "ConfigMap": "ConfigMaps",
    "Secret": "Secrets",
    "Deployment": "Deployments",
    "Service": "Services",
    "Namespace": "Namespace",
}

# Create output directories
for folder in resource_folders.values():
    os.makedirs(os.path.join(output_dir, folder), exist_ok=True)

# Split YAML into separate files organized by resource type
with open(input_file, 'r') as file:
    docs = list(yaml.safe_load_all(file))

for doc in docs:
    if doc and "kind" in doc:
        kind = doc["kind"]
        name = doc["metadata"]["name"]
        folder = resource_folders.get(kind, None)
        
        if folder:
            output_path = os.path.join(output_dir, folder, f"{kind.lower()}-{name}.yaml")
            with open(output_path, 'w') as out_file:
                yaml.dump(doc, out_file)
