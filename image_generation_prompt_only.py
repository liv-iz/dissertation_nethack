import requests
import random
import pandas as pd

file_location = 'nethack_tileset/Data_Gathering/GPT/GPT Descriptions/GPT Second Run CSV'
tileset_prompts = pd.read_csv("nethack_tileset/Data_Gathering/Data preparation/all_prompts_second_run.csv")
seed_number = random.randint(1, 2147483647)

for index, row in tileset_prompts.sample(10).iterrows():
    prompt = row['technical']
    title = row['Title']
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/core",
        headers={
            "authorization": f"Bearer sk-DcG6VTH5po2qHsNUD8r4UbNxMHHnrihly6cPhFshie10Ykm9",
            "accept": "image/*"
        },
        files={
            "none": ''
        },
        data={
            "prompt": f"{prompt}",
            "seed": f"{seed_number}",
            "output_format": "png",
        },
    )

    if response.status_code == 200:
        filename = f"Generation/technical_prompt_only/5/{title}_{seed_number}.png"
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(str(response.json()))
