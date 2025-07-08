from transformers import pipeline
import nltk
nltk.download('punkt')

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Sample long article (feel free to load from file)

article_text = """India’s stock market has rapidly evolved into one of the world’s most dynamic capital markets,
driven by robust retail participation and growth in digital trading platforms.
As more investors seek long-term value creation, strategic planning around asset allocation and understanding risk remains key.
Market analysts project that India could become the third-largest economy by 2030,
further strengthening investor confidence.
As capital inflows increase, so does the need for stronger financial literacy and digital infrastructure.
While optimism remains high, experts also caution against short-term speculation and encourage diversified portfolios."""

# Generate summary
summary = summarizer(article_text, max_length=100, min_length=30, do_sample=False)

# Display results
print("Original Text:\n", article_text)
print("\n🔍 Summary:\n", summary[0]['summary_text'])
