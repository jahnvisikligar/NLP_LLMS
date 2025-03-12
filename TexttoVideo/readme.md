This project is an assignment for text to video synthesis.

**Code Explanation:**

Generating Historical Documentary Videos Using AI

This script automates the generation of historical documentary videos on the Mughal Empire using AI-based text generation and text-to-video models. The process consists of two main steps:

1. Generating a JSON file with six scenes, each describing a historical event related to the Mughal Empire.

2. Creating videos from the text using a diffusion-based text-to-video model.

**Method Breakdown**

1. Generating JSON with Historical Scene Descriptions

Function: generate_json()

Uses the Hugging Face Inference API (InferenceClient) to generate structured text output based on the given prompt.

Sends a request to the mistralai/Mistral-7B-Instruct-v0.2 model, instructing it to generate six scenes, each at least 200 words long.

The model responds with a JSON object containing scene titles and descriptions.

This JSON is saved to a file (output_file_1.json) for later use.

Key Components

InferenceClient: A Hugging Face API wrapper for sending prompts and receiving responses from hosted models.

messages: Defines the structure of the prompt given to the model.

json.dump(): Converts the response into a formatted JSON file.

---

2. Generating Videos from Text Descriptions

Function: generate_video_from_text(prompt, output_path, num_frames=64)

Uses the "damo-vilab/text-to-video-ms-1.7b" model from Hugging Face’s DiffusionPipeline.

Converts the input text (prompt) into a sequence of frames.

Exports the generated frames into a video file.

Key Components

DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b"): Loads the pre-trained text-to-video model.

enable_model_cpu_offload(): Moves model computations to the CPU to optimize memory usage.

enable_vae_slicing(): Further optimizes memory by processing parts of the image separately.

export_to_video(video_frames, output_path): Saves the generated frames as a video file.

---

3. Running the Full Pipeline

Mounting Google Drive for Storage

drive.mount('/content/drive') mounts Google Drive to store generated videos.

The script creates a folder "/content/drive/My Drive/GeneratedVideos/" to store output.

Reading the JSON File and Generating Videos

The script loads the generated JSON (output_file_1.json).

Iterates through the six scenes, extracting each scene’s description as input (prompt).

Calls generate_video_from_text() to generate and save videos to Google Drive

**How to Use This Code**

1. Run the script in Google Colab (since it relies on Google Drive and Hugging Face APIs).

2. Replace "hf_APIKEY" with your actual Hugging Face API key.

3. Execute the script:

It first generates the JSON file with Mughal Empire scene descriptions.

Then, it uses this JSON to create six historical documentary-style videos.

The videos are automatically saved in Google Drive.

---

**Expected Output**

A JSON file (output_file_1.json) containing six detailed Mughal Empire scene descriptions.

Six AI-generated videos (one per scene) stored in the GeneratedVideos folder in Google Drive.

This method allows efficient text-to-video conversion, making it useful for creating AI-driven historical documentaries, educational content, and storytelling applications.
