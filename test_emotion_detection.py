from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        statement1 = "I am glad this happened"
        emotion1 = emotion_detection(statement1)['dominant_emotion']

        statement2 = "I am really mad about this"
        emotion2 = emotion_detection(statement2)['dominant_emotion']

        statement3 = "I feel disgusted just hearing about this"
        emotion3 = emotion_detection(statement3)['dominant_emotion']

        statement4 = "I am so sad about this"
        emotion4 = emotion_detection(statement4)['dominant_emotion']

        statement5 = "I am really afraid that this will happend"
        emotion5 = emotion_detection(statement5)['dominant_emotion']

        self.assertEqual(emotion1, "joy")
        self.assertEqual(emotion2, "anger")
        self.assertEqual(emotion3, "disgust")
        self.assertEqual(emotion4, "sadness")
        self.assertEqual(emotion5, "fear")

unittest.main()