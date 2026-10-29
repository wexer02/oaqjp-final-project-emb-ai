"""Unit tests for the five required emotions, formatting, and status 400.

Watson HTTP responses are mocked: these tests validate application logic,
not the availability or accuracy of the live Watson service.
"""

import unittest
from unittest.mock import Mock, patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify the required outputs independently of Watson network access."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_emotion_detector(self, mock_post):
        """Check the five required phrases against controlled Watson responses."""
        cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for text, expected in cases:
            with self.subTest(expected=expected):
                scores = dict.fromkeys(("anger", "disgust", "fear", "joy", "sadness"), 0.01)
                scores[expected] = 0.96
                mock_post.return_value = Mock(status_code=200)
                mock_post.return_value.json.return_value = {
                    "emotionPredictions": [{"emotion": scores}]
                }
                result = emotion_detector(text)
                self.assertEqual(result["dominant_emotion"], expected)
                self.assertEqual(result, {**scores, "dominant_emotion": expected})

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_status_400(self, mock_post):
        """Watson status 400 must produce six None values."""
        mock_post.return_value = Mock(status_code=400)
        self.assertTrue(all(value is None for value in emotion_detector("invalid").values()))

    def test_blank_input(self):
        """Blank input returns the invalid-result format without a network call."""
        self.assertIsNone(emotion_detector(" ")["dominant_emotion"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
