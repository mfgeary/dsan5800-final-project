from flask import Flask, request, jsonify, render_template
from homophone_utils import homophone_checker
import pandas as pd

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/check_homophone', methods=['POST'])
# def check_homophone():
#     data = request.json
#     sentence = data['sentence']
#     result_df = homophone_checker(sentence)
#     # Extract 'correct_sentence' from the DataFrame
#     correct_sentence = result_df.at[0, 'correct_sentence']
#     return jsonify({'correct_sentence': correct_sentence})

@app.route('/check_homophone', methods=['POST'])
def check_homophone():
    data = request.json
    sentence = data['sentence']
    # Homophone and spelling correction
    result_df = homophone_checker(sentence)
    homophone_corrected_sentence = result_df.at[0, 'correct_sentence']
    spelling_corrected_sentence = result_df.at[0, 'spelling_correct_sentence']
    return jsonify({
        'homophone_corrected_sentence': homophone_corrected_sentence,
        'spelling_corrected_sentence': spelling_corrected_sentence
    })

if __name__ == '__main__':
    app.run(debug=True)
