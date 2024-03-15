import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dataset import dataset  

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Tokenize text
    words = word_tokenize(text.lower())

    # Remove stop words and non-alphabetic characters
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # Lemmatize words
    words = [lemmatizer.lemmatize(word) for word in words]

    return ' '.join(words)

def respond_to_query(query, dataset):
    processed_query = preprocess_text(query)
    processed_questions = [preprocess_text(q) for q, _ in dataset]

    # Vectorize processed questions and query
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([processed_query] + processed_questions)
    query_vector = X[0]
    dataset_vectors = X[1:]

    # Calculate cosine similarity between query and dataset questions
    similarities = cosine_similarity(query_vector, dataset_vectors)[0]

    # Get index of most similar question
    most_similar_index = similarities.argmax()

    # Check if similarity is above a certain threshold
    if similarities[most_similar_index] > 0.3:  
        return dataset[most_similar_index][1]
    else:
        return "I'm sorry, I don't have an answer to that. Please wait while I connect you to a real person."

if __name__ == "__main__":
    while True:
        user_query = input("You: ")
        if user_query.lower() in ['exit', 'quit', 'goodbye', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = respond_to_query(user_query, dataset)
        print("Chatbot:", response)
