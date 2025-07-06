import unittest
from unittest.mock import patch
from phonebridge.sms_reader import parse_sms_output, main

class TestSMSReader(unittest.TestCase):

    sample_raw_output = (
        "body=Hello world, address=+123456789, date=1627891234567\n"
        "body=Test message, address=+987654321, date=1627899876543\n"
    )

    def test_parse_sms_output(self):
        messages = parse_sms_output(self.sample_raw_output)
        self.assertEqual(len(messages), 2)
        self.assertIn("From: +123456789", messages[0])
        self.assertIn("Message: Hello world", messages[0])

    @patch('phonebridge.sms_reader.run_adb_query')
    def test_main(self, mock_run_adb_query):
        mock_run_adb_query.return_value = self.sample_raw_output
        # Capture printed output
        with unittest.mock.patch('builtins.print') as mock_print:
            main()
            # Check print called at least once
            self.assertTrue(mock_print.called)
            # You can also check if certain text was printed
            printed = " ".join(str(call.args[0]) for call in mock_print.call_args_list)
            self.assertIn("From: +123456789", printed)

if __name__ == '__main__':
    unittest.main()
