from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import PorterStemmer

app = Flask(__name__)

# Load and preprocess the CSV data
stemmer = PorterStemmer()
data = pd.read_csv('chatbot_data.csv', encoding='utf-8')  # Read the CSV file with UTF-8 encoding

# Print columns to verify
print(data.columns)  # Optional: Check the actual column names in your CSV

# Ensure column names are correct; adjust if necessary
data.columns = ['Question', 'Response']  # Rename columns if needed

# Apply preprocessing to the 'Question' column
data['Question'] = data['Question'].apply(lambda x: ' '.join([stemmer.stem(word) for word in nltk.word_tokenize(x.lower())]))

# Fit TF-IDF model
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['Question'])

def get_response(user_input):
    # Preprocess user input
    user_input_processed = ' '.join([stemmer.stem(word) for word in nltk.word_tokenize(user_input.lower())])
    
    # Transform user input using the same TF-IDF vectorizer
    user_vec = vectorizer.transform([user_input_processed])
    
    # Compute cosine similarity
    similarities = cosine_similarity(user_vec, tfidf_matrix)
    index = similarities.argmax()
    
    # Check for similarity threshold
    if similarities[0, index] > 0.2:
        return data.iloc[index]['Response']
    else:
        return "I don't have an answer for that. Can you please ask something else?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_chatbot_response():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
