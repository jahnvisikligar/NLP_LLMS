import torch
import os, json, shutil
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video
from huggingface_hub import InferenceClient
from google.colab import drive

def generate_json():
    try:
        client = InferenceClient(provider='hf-inference', api_key='hf_APIKEY')
        messages = [
            {
                "role": "user",
                "content": """Your task is to generate 6 scenes each of 6 seconds on the topic of Mughal Empire.
                              Each scene should have a title and be at least 200 words. Do not include the word count.
                              The response should be in JSON format."""
            }
        ]
        completion = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=messages
        )
        output = completion.choices[0].message.content

        # Save JSON output
        with open('output_file_1.json', 'w') as f:
            json.dump(json.loads(output), f, indent=4)

        return output
    except Exception as e:
        print(f"Error in generate_json: {e}")
        return None

def generate_video_from_text(prompt, output_path, num_frames=64):
    try:
        # Load the pipeline
        pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
        pipe.enable_model_cpu_offload()
        pipe.enable_vae_slicing()

        # Generate video frames
        video_frames = pipe(prompt, num_frames=num_frames).frames[0]

        # Export to video file
        export_to_video(video_frames, output_path)
        print(f"Video saved to: {output_path}")

    except Exception as e:
        print(f"Error in generate_video_from_text: {e}")

try:
    mughal_scenes_json = generate_json()
    if mughal_scenes_json:
        print(mughal_scenes_json)
    else:
        raise ValueError("Failed to generate JSON. Skipping video generation.")
    
    # Mount Google Drive
    drive.mount('/content/drive')

    output_folder = "/content/drive/My Drive/GeneratedVideos/"
    os.makedirs(output_folder, exist_ok=True)

    # Load JSON file
    with open('/content/output_file_1.json', 'r') as f:
        scenes_data = json.load(f)

    # Generate videos from each scene
    for i, scene in enumerate(scenes_data):
        try:
            prompt = scene['scene']
            video_path = os.path.join(output_folder, f"mughal_scene_{i + 1}.mp4")
            generate_video_from_text(prompt, video_path)
        except KeyError:
            print(f"Error: 'scene' key not found in scene {i+1}. Skipping...")

except Exception as e:
    print(f"Unexpected error: {e}")
