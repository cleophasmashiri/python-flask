import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):

        response_joy = emotion_detector('I am glad this happened')
        self.assertEquals(response_joy.get('dominant_emotion'), 'joy')

        response_anger = emotion_detector('I am really mad about this')
        self.assertEquals(response_anger.get('dominant_emotion'), 'anger')

        response_disgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEquals(response_disgust.get('dominant_emotion'), 'disgust')

        response_sadness = emotion_detector('I am so sad about this')
        self.assertEquals(response_sadness.get('dominant_emotion'), 'sadness')

        response_fear = emotion_detector('I am really afraid that this will happen')
        self.assertEquals(response_fear.get('dominant_emotion'), 'fear')


unittest.main()        