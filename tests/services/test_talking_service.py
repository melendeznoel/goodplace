"""Tests for Talking Service"""

import pytest
import os

from app.services import TalkingService

class TestTalkingService:
    def test_append(self):
        os.environ["GCP_PROJECT_ID"] = "mock-project-id"
        os.environ["GCP_TOPIC_SUBSCRIPTION_NAME"] = "mock-sub-name"

        talking_service = TalkingService()

        assert talking_service.append(1) == 1
