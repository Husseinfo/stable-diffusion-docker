#!/bin/env python
from base64 import b64decode
from sys import stderr

from requests import post

_url = 'http://localhost:5000/predictions'
prompt = input('Enter a prompt:\n') or 'batman logo'

data = {"input": {
    "prompt": prompt,
    "width": "256",
    "height": "256",
    "prompt_strength": "0.6",
    "num_outputs": "1",
    "num_inference_steps": "100",
    "guidance_scale": "7.5",
    "seed": "7"
}}

response = post(_url, json=data)

if response.status_code != 200:
    print(f'Error {response.status_code}: {response.text}', file=stderr)
    exit()

for i, image in enumerate(response.json()['output']):
    with open(f'image_{i + 1}.jpeg', 'wb') as f:
        f.write(b64decode(image.split(',')[-1]))

print('Done!')
