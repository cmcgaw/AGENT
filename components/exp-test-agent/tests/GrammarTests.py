import unittest

from Grammar.SequenceParser import SequenceParser


class GrammarTests(unittest.TestCase):

    def setUp(self):
        self.parser = SequenceParser("../Grammar/seq.g")

    def test_flow_reconstruction(self):
        # Arrange.
        to_parse = "OBSERVE TEXTBOX LASTNAME TRY INVALID_LONG LASTNAME CLICK COMMIT OBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

    def test_flow_reconstruction_learned_el_class(self):
        # Arrange.
        to_parse = "OBSERVE LEARNED_ELCLASS_NCLS LASTNAME TRY INVALID_LONG LASTNAME CLICK COMMIT OBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

    def test_flow_clean(self):
        # Arrange.
        to_parse = "OBSERVE REQUIRED TEXTBOX FIRST_NAME " + \
                   "OBSERVE REQUIRED TEXTBOX LAST_NAME " + \
                   "OBSERVE REQUIRED TEXTBOX EMAIL " + \
                   "OBSERVE REQUIRED TEXTBOX PASSWORD " + \
                   "OBSERVE REQUIRED TEXTBOX CONFIRM_PASSWORD " + \
                   "OBSERVE REQUIRED TEXTBOX PRIMARY_PHONE_NUMBER " + \
                   "TRY VALID USERNAME " + \
                   "TRY INVALID PASSWORD " + \
                   "CLICK COMMIT " + \
                   "OBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

    def test_flow_reconstruction_sign_in_screen(self):
        # Arrange.
        to_parse = "OBSERVE TEXTBOX EMAIL TRY INVALID_LONG EMAIL CLICK COMMIT OBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

        # Arrange.
        to_parse = "OBSERVE TEXTBOX EMAIL TRY VALID EMAIL CLICK COMMIT NOTOBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

        # Arrange.
        to_parse = "OBSERVE TEXTBOX EMAIL " + \
                   "TRY VALID EMAIL " + \
                   "CLICK COMMIT " + \
                   "NOTOBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

        # Arrange.
        to_parse = "OBSERVE TEXTBOX PASSWORD " + \
                   "TRY INVALID_LONG PASSWORD " + \
                   "CLICK COMMIT " + \
                   "OBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

        # Arrange.
        to_parse = "OBSERVE TEXTBOX USERNAME " + \
                   "OBSERVE TEXTBOX PASSWORD " + \
                   "TRY VALID USERNAME " + \
                   "TRY INVALID PASSWORD " + \
                   "CLICK COMMIT " + \
                   "OBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

        # Arrange.
        to_parse = "OBSERVE REQUIRED TEXTBOX FIRST_NAME " + \
                   "OBSERVE REQUIRED TEXTBOX LAST_NAME " + \
                   "OBSERVE REQUIRED TEXTBOX EMAIL " + \
                   "OBSERVE REQUIRED TEXTBOX PASSWORD " + \
                   "OBSERVE REQUIRED TEXTBOX CONFIRM_PASSWORD " + \
                   "OBSERVE REQUIRED TEXTBOX PRIMARY_PHONE_NUMBER " + \
                   "TRY VALID USERNAME " + \
                   "TRY INVALID PASSWORD " + \
                   "CLICK COMMIT " + \
                   "OBSERVE ERRORMESSAGE"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

    def test_flow_parens(self):
        # Arrange.
        to_parse = "OBSERVE SCREEN SIGN_IN TRY BLANK USERNAME CLICK COMMIT OR( OBSERVE ERRORMESSAGE , OBSERVE DISABLED COMMIT )"

        # Act.
        test_flow = self.parser.parse(to_parse)

        # Assert.
        self.assertEqual(to_parse, str(test_flow))

    def test_flow_sequences(self):
        with open('strings.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('#') or line == "":
                continue
            print(line)
            test_flow = self.parser.parse(line)
            self.assertEqual(line, str(test_flow))
