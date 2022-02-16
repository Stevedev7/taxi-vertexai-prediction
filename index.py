import os
import json
import pickle
import requests
import subprocess
import numpy as np
from dotenv import load_dotenv

load_dotenv()

ENDPOINT_ID = os.getenv("ENDPOINT_ID")
PROJECT_ID = os.getenv("PROJECT_ID")
KEY_PATH = os.path.join(os.getcwd(), 'vertexai_creds.json')
URL = f'https://us-central1-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/us-central1/endpoints/{ENDPOINT_ID}:predict'
os.system(f'gcloud auth activate-service-account --key-file {KEY_PATH}')
TOKEN = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode('utf-8').rstrip()

trip_seconds = 1532
trip_miles= 10.3
fare= 28.6
tolls = 0.0
extras= 0.0
payment_type= "Credit Card"
company = "Setare Inc"

data = {
    "trip_seconds": trip_seconds,
    "trip_miles":trip_miles,
    "fare": fare,
    "tolls": tolls,
    "extras": extras,
    "payment_type": payment_type,
    "company": company
}


input = [[j for (i, j) in data.items()]]

with open('column_transformer.pkl', 'rb') as f:
    ct = pickle.load(f)

input = ct.transform(input)

with open('standard-scaler.pkl', 'rb') as f:
    sc = pickle.load(f)

feature_names = sc.get_feature_names_out()

values = sc.transform(np.array(input.toarray()))

input_values = dict(zip(feature_names, values[0]))

response = requests.post(
    url=URL,
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    },
    data=json.dumps({"instances": values.tolist()})
)

# print(json.dumps({"instances": values.tolist()}))

print(response.json())

# print(values[0].tolist())
