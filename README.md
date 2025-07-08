# Text-Summarization-tool

*COMPANY: CODTECH IT SOLUTIONS

*NAME: AYUSH MACHHINDRA KAUTE

*INTERN ID: CT04DF1740

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEEKS

*MENTOR: NEELA SANTOSH

OUTPUT:
<img width="1532" height="503" alt="Image" src="https://github.com/user-attachments/assets/29a60e21-d671-40d9-b3a4-e4c096af7b31" />

Description:
The provided Python script uses a pre-trained transformer-based model to summarize long text into a concise, coherent summary. This is a common task in Natural Language Processing (NLP) called abstractive text summarization. Unlike extractive summarization (which picks sentences from the original), abstractive models generate completely new sentences based on the original context.

1. Importing Libraries

from transformers import pipeline
import nltk
Here, we import two libraries:

transformers: From Hugging Face, this library contains powerful pre-trained models like BERT, GPT, and BART.
nltk: The Natural Language Toolkit, commonly used for text processing. While it’s included here, it's not essential for this specific summarization task.
nltk.download('punkt')
This downloads the Punkt tokenizer data, which is used for sentence tokenization in NLTK. It’s not directly used in the rest of the script, so you can optionally remove it.

2. Loading the Summarization Pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
This line loads the summarization pipeline using the "facebook/bart-large-cnn" model. This model is:

Based on the BART (Bidirectional and Auto-Regressive Transformers) architecture
Pre-trained on large corpora of news articles
Fine-tuned for summarizing documents
The pipeline() function abstracts away the complex model loading and tokenization steps, making summarization as simple as calling a function.

3. Defining the Article to Summarize

article_text = """India’s stock market... diversified portfolios."""
This multi-line string contains a sample article or paragraph about India’s stock market. It discusses:

Growth of the Indian stock market
Rise in retail investor participation
Importance of strategic investment planning
Forecasts for India's economy
The need for financial literacy

This is the input that we want the model to summarize.

4. Generating the Summary

summary = summarizer(article_text, max_length=100, min_length=30, do_sample=False)
This is the core operation. The summarizer() function processes the input text and returns a summary. Let’s understand the parameters:

max_length=100: The summary will be capped at 100 tokens (words/subwords).
min_length=30: The summary will be at least 30 tokens.
do_sample=False: Disables random sampling. The output will be deterministic, using beam search for accuracy.
The result is stored in a variable named summary, which is a list of dictionaries. Each dictionary has a key 'summary_text' containing the generated summary.

5. Displaying the Results

print("Original Text:\n", article_text)
print("\n🔍 Summary:\n", summary[0]['summary_text'])
This prints the original article and the generated summary to the console. The summary variable is a list with one dictionary, so summary[0]['summary_text'] accesses the final summarized text.

🔍 Why Use This Approach?
This script shows how easy it is to use transformers for summarization. Compared to building a model from scratch, this method offers:

Speed: No training required — just load and use.
Accuracy: Pre-trained on large, high-quality datasets.
Scalability: Can be used on long articles, reports, and documents.

✅ Conclusion
In summary, this Python script demonstrates how to perform abstractive text summarization using a pre-trained model (facebook/bart-large-cnn) from Hugging Face Transformers. With just a few lines of code, you can reduce long paragraphs into short, meaningful summaries. This is useful for news apps, academic research tools, content curation, and more. The pipeline abstraction allows non-experts to leverage state-of-the-art NLP without worrying about the underlying architecture.


