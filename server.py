"""
 emotion_detector server app 
"""
from flask import request, render_template, Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders index.html
    returns dictionary of emotions
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_serve():
    """
    Calls emotion_detector app 
    args: text_to_analyze
    returns dictionary of emotions
    """
    text_to_analyse =  request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!.'
    return f"""For the given statement, the system response is 'anger': {response.get('anger')}
    , 'disgust': {response.get('disgust')}, 'fear': {response.get('fear')}, 'joy': {response.get('joy')} and 'sadness': 
    {response.get('sadness')}. The dominant emotion is {response.get('dominant_emotion')}."""



if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
