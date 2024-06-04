''' This function to start the Emotion Detector
    application using Flask and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")
@app.route("/emotionDetector")
def emot_detector():
    ''' This function receives text from the index.html file
        and runs the emotion_detector() function on the text.
        It then returns a response displaying each emotion detected and
        the score. If the text is invalid it displays a message.
    '''
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is \
            'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. \
            The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index():
    ''' This function returns the rendered index.html file
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
