# Sentiment Analysis Made Easy

Sentiment analysis plays a crucial role in understanding the opinions of people and enhancing customer experience for businesses. Being one of the key aspects of Natural Language Processing(NLP), sentiment analysis is a process of analyzing digital text to determine its emotional states such as positive, negative or neutral. Here, we dive deeper into implementing a pre-trained BERT model and deploying it using the StreamLit framework from the HuggingFace hub.

## What is BERT?

BERT stands for Bidirectional Encoder Representations from Transformers and was introduced under the research paper titled "[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)" by Google's AI research team in 2018. It transformed the AI language processing and the way machines understood text. Unlike the traditional models, BERT analyses text bi-directionally to understand the context from the preceding and following words. With the help of a two-step process involving pre-training and fine-tuning BERT can predict missing words in sentences and adapt to various language tasks. Thus making it versatile for different use cases such as sentiment analysis, QnA, Name Entity Recognition(NER) and many more.

As we have gained an overview of the BERT model, let's begin with the implementation of the same.

### Working with data and dependencies

The first step is to activate the GPU on the Google Colab notebook and install the necessary dependencies, such as `datasets`, `transformers`, and `huggingface_hub`, to facilitate model training and deployment. Next, we download the [IMDB movie review](https://huggingface.co/datasets/imdb) dataset and split it into test and train data, which will then be tokenized using the DistilBERT tokenizer.

### Working with the DistilBERT Model

Now that the data is ready, it's time to begin training of BERT model for sentiment analysis. As the BERT model is bulky and quite slow, DistilBERT is used for this project due to the limitations of computational resources and memory in Colab.

<details data-node-type="hn-details-summary"><summary>DistilBERT</summary><div data-type="detailsContent"><a target="_blank" rel="noopener noreferrer nofollow" href="https://huggingface.co/docs/transformers/model_doc/distilbert" style="pointer-events: none">DistilBERT</a> is the distilled version of the BERT model proposed by HuggingFace trained in the technique of knowledge distillation. This allows the model to retain the performance of the original BERT model while having fewer parameters.</div></details>

#### **Training**

We will be using classification tasks for sentiment analysis that enable the transfer of knowledge from DistilBERT to the custom model.

* We import the `AutoModelForSequenceClassification` class from the `transformers` library. This class is designed for sequence classification tasks and is compatible with models like BERT.
    
* We create an instance of the model by calling `AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)`. Here, "distilbert-base-uncased" refers to the pre-trained DistilBERT model, and `num_labels=2` specifies that we are performing binary sentiment classification (positive or negative sentiment).
    
* We import `TrainingArguments` and `Trainer` API from the `transformers` library. The `TrainingArguments` class allows us to define training-related settings.
    
* We set `repo_name` to the desired name of the repository where the trained model will be stored.
    
* We create an instance of `TrainingArguments` by specifying various training-related settings such as learning rate, batch sizes, gradient accumulation, number of epochs, and more. These settings impact the training process and performance.
    
* We set `push_to_hub=True` to indicate that we want to push the trained model to the Hugging Face model hub.
    
* We initiate the training process using the `.train()` method of the `trainer` instance.
    
* The model begins training based on the specified training arguments and the provided datasets.
    
* The training loop involves forward and backward passes, gradient updates, and optimization steps.
    

#### Evaluation

* We define a custom function `compute_metrics` that takes the evaluation predictions (`eval_pred`) as input.
    
* Inside the function, we load the accuracy and F1 score metrics using `load_metric("accuracy")` and `load_metric("f1")`.
    
* We extract the logits and labels from `eval_pred` and calculate the predictions by selecting the index with the maximum value along the last axis (using `np.argmax(logits, axis=-1)`).
    
* We calculate the accuracy and F1 score by passing the predictions and labels to the respective metric calculators and returning them as a dictionary.
    
* After training, we evaluate the model's performance using the `.evaluate()` method of the `trainer` instance.
    
* This step calculates and displays metrics like accuracy and F1 score based on the evaluation dataset.
