# stable-diffusion-docker

<figure align="center">
<img src="batman-logo.jpeg" alt="Batman logo">
<figcaption><b>batman logo</b><br/><i>100 steps,
    prompt_strength: 0.6,
    guidance_scale: 7.5,
    seed: 7</i></figcaption>
</figure>

## Run [stable diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion) text-to-image generator locally

### Prerequisites

- [Docker](https://docs.docker.com/)
- [CUDA-enabled Nvidia GPU](https://developer.nvidia.com/cuda-gpus)
- Install nvidia-docker2
    - `sudo apt install -y nvidia-docker2`

### Test Nvidia docker installation

`docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi`

#### Sample output

```
Mon Sep  5 19:47:04 2022       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI xxx.xx.xx    Driver Version: xxx.xx.xx    CUDA Version: xx.x     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0 Off |                  N/A |
| N/A   42C    P8    N/A /  N/A |      6MiB /  4096MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+

```

### Run

- Pull and run the latest docker image to run server

`docker run -d -p 5000:5000 --gpus=all r8.im/stability-ai/stable-diffusion`

- Generate an image
    - Python CLI
        - `./run.py`
    - using cURL

```bash
 curl http://localhost:5000/predictions -X POST -H "Content-Type: application/json" \
  -d '{"input": {
    "prompt": "A penguin shaped computer",
    "width": "512",
    "height": "512",
    "prompt_strength": "0.8",
    "num_outputs": "1",
    "num_inference_steps": "50",
    "guidance_scale": "7.5",
    "seed": "3"
  }}
```
