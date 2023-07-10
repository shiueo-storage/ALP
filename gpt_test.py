import json
import requests

from huggingface_hub.inference_api import InferenceApi

inerference = InferenceApi(repo_id="gpt2-large", token="secet")

input_string = "what"
ttt = {"max_length": 45}
res = inerference(input_string, ttt)
print(res)
