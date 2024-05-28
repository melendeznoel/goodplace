"""Tests for Talking Service"""

import unittest
import os

from src.talking_service import TalkingService

class TalkingServiceTestCase(unittest.TestCase):
    def test_append(self):
        os.environ["GCP_PROJECT_ID"] = "mock-project-id"
        os.environ["GCP_TOPIC_SUBSCRIPTION_NAME"] = "mock-sub-name"
        talking_service = TalkingService()

        self.assertEqual(talking_service.append(1), 1)