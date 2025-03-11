import torch
import os, json, shutil
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video
from huggingface_hub import InferenceClient
from google.colab import drive

def generate_json():
  client=InferenceClient(provider='hf-inference', api_key='hf_APIKEY')
  messages=[
    {
      "role":"user",
      "content":"""Your task is to generate 6 scenes each of 6 seconds on the topic of Mughal Empire.
                    Each scene should have a title and be atleast 200 words. Do not include the word count.
                    The response should be in json format."""
    }
  ]
  completion=client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=messages
  )
  output=completion.choices[0].message.content
#  print(output)
  with open('output_file_1.json','w') as f:
    json.dump(json.loads(output),f,indent=4)
  return output

def generate_video_from_text(prompt, output_path, num_frames=64):
    # Load the pipeline (if not already loaded)
    pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
    pipe.enable_model_cpu_offload()
    pipe.enable_vae_slicing()

    # Generate video frames
    video_frames = pipe(prompt, num_frames=num_frames).frames[0]
    # Export to video file
    export_to_video(video_frames, output_path)
    print(f"Video saved to: {output_path}")

mughal_scenes_json=generate_json()
print(mughal_scenes_json)

# Example usage with your JSON file:
drive.mount('/content/drive')
output_folder = "/content/drive/My Drive/GeneratedVideos/"
os.makedirs(output_folder, exist_ok=True)

with open('/content/output_file_1.json', 'r') as f:
    scenes_data = json.load(f)

for i, scene in enumerate(scenes_data):
    prompt = scene['scene']
    video_path = os.path.join(output_folder, f"mughal_scene_{i + 1}.mp4")
    generate_video_from_text(prompt, video_path)
