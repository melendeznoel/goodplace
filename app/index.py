"""API Bootstrap"""

from .services import TalkingService

talk = TalkingService()

talk.append("Some data to append")
