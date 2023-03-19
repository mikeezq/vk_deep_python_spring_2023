from unittest import TestCase, mock

import pytest

from hw_01.tasks.predict_message import SomeModel, predict_message_mood


class TestPredictMessage(TestCase):
    def setUp(self):
        self.model = SomeModel(0)

    def test_model_predict(self):
        test_message = "some message"
        expected_results = ["отл", "неуд", "норм", "норм", "норм"]
        with mock.patch("hw_01.tasks.predict_message.SomeModel.predict") as mock_predict:
            mock_predict.side_effect = 1, 0.2, 0.6, 0.8, 0.3

            for expected_result in expected_results:
                self.assertEqual(predict_message_mood(test_message, self.model), expected_result)

            with pytest.raises(ValueError, match="Message can't be empty"):
                predict_message_mood("", self.model)

            self.assertEqual(mock_predict.call_count, 5)
