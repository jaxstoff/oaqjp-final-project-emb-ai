from EmotionDetection.emotion_detection import emotion_detector
import unittest
import ast

class TestEmotionDetection(unittest.TestCase):
    # uses ast.literal_eval because output from emotion_detector is not valid json so we can't use json.loads
    # why? because Task 3 said to do it that way!
    def test_emotion_detector(self):
        # Test case for joy
        result_1 = ast.literal_eval(emotion_detector('I am glad this happened'))
        self.assertEqual(result_1.get('dominant_emotion'), 'joy')
        # Test case for anger
        result_2 = ast.literal_eval(emotion_detector('I am really mad about this'))
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        # Test case for disgust
        result_3 = ast.literal_eval(emotion_detector('I feel disgusted just hearing about this'))
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        # Test case for sadness
        result_4 = ast.literal_eval(emotion_detector('I am so sad about this'))
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        # Test case for fear
        result_5 = ast.literal_eval(emotion_detector('I am really afraid that this will happen'))
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()