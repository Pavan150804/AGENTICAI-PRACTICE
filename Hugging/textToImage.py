import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("zieves/LCM-runwayml-stable-diffusion-v1-5", dtype=torch.bfloat16)

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]
image.save("astonout.png")


import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-schnell"
)

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"

image = pipe(prompt).images[0]

image.save("astronaut.png")
image.show()