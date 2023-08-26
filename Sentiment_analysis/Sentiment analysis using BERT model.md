# Sentiment analysis using the BERT model

I used the BERT model to implement sentiment analysis in this project. I used PyTorch and the Hugging Face transformers library to fine-tune a pre-trained DistilBERT model. The model was trained on a small dataset of 10,000 IMDB movie reviews.

Preprocessing the data with the DistilBERT tokenizer, defining the model architecture and evaluation metrics, and training the model with a TrainingArguments object were all part of the project. Gradient accumulation and a learning rate schedule were used in the training process.

The model's performance was evaluated on a separate test dataset, and the evaluation metrics computed included accuracy and F1-score. The trained model was then shared and accessible via the Hugging Face Hub.

Finally, I used the Pipeline API and the uploaded model to perform sentiment analysis on new data. The final sentiment model accurately classified the polarity of a given text as positive or negative. This project allowed me to demonstrate my natural language processing, machine learning, and deep learning abilities.

Streamlit App: https://js21-sentiment-analysis-with-streamlit.hf.space/

![streamlit-app-2023-08-26-20-08-53-_copy_](https://github.com/jahnvisikligar/NLP_projects/assets/83291068/5df68dee-4d35-406b-9f08-c2e2d51703ca)

