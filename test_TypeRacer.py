from unittest import mock, TestCase
from unittest.mock import Mock

from TypeRacer import TypeRacer


class TestTypeRacer(TestCase):
    def testFormatTextToType_singleCharacterFirstWord(self):
        # Setup
        type_racer = TypeRacer(Mock())
        expected = "I am here"

        # Execution
        actual = type_racer.format_text_to_type(['I', 'am', 'here'])

        # Test
        self.assertEquals(actual, expected)

    def testFormatTextToType_punctuationInFirstWord(self):
        # Setup
        type_racer = TypeRacer(Mock())
        expected = "I've been there"

        # Execution
        actual = type_racer.format_text_to_type(["I", "'ve", "been", "there"])

        # Test
        self.assertEquals(actual, expected)

    def testFormatTextToType_multiCharacterFirstWord(self):
        # Setup
        type_racer = TypeRacer(Mock())
        expected = "They have been there"

        # Execution
        actual = type_racer.format_text_to_type(["T", "hey", "have", "been", "there"])

        # Test
        self.assertEquals(actual, expected)