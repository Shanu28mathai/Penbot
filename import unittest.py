import unittest
from unittest.mock import patch, MagicMock
import json
from penbot import find_subdomains, scan_vulnerabilities, ai_prioritize_vulnerabilities, generate_report, Penbot

class TestPenBot(unittest.TestCase):

    @patch('penbot.dns.resolver.resolve')
    def test_find_subdomains(self, mock_resolve):
        mock_resolve.side_effect = lambda x, y: True
        domain = "example.com"
        expected_subdomains = ['www.example.com', 'mail.example.com', 'ftp.example.com', 'dev.example.com', 'api.example.com', 'shop.example.com']
        result = find_subdomains(domain)
        self.assertEqual(result, expected_subdomains)

    @patch('penbot.requests.get')
    def test_scan_vulnerabilities(self, mock_get):
        mock_response = MagicMock()
        mock_response.headers = {'Server': 'Apache/2.4.1'}
        mock_response.text = '<html></html>'
        mock_response.url = 'https://example.com'
        mock_get.return_value = mock_response

        url = "https://example.com"
        expected_vulnerabilities = ["Potential outdated server detected: Apache/2.4.1"]
        result = scan_vulnerabilities(url)
        self.assertEqual(result, expected_vulnerabilities)

    def test_ai_prioritize_vulnerabilities(self):
        vulnerabilities = ["Potential outdated server detected: Apache/2.4.1", "Potential XSS vulnerability detected in response."]
        expected_prioritization = {
            "high_severity": ["Potential outdated server detected: Apache/2.4.1", "Potential XSS vulnerability detected in response."],
            "low_severity": []
        }
        result = ai_prioritize_vulnerabilities(vulnerabilities)
        self.assertEqual(result, expected_prioritization)

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('penbot.json.dump')
    def test_generate_report(self, mock_json_dump, mock_open):
        domain = "example.com"
        subdomains = ['www.example.com']
        vulnerabilities = {"high_severity": ["Potential XSS vulnerability detected in response."], "low_severity": []}
        
        generate_report(domain, subdomains, vulnerabilities)
        
        mock_open.assert_called_with(f"{domain}_report.json", "w")
        mock_json_dump.assert_called_once()

class TestPenbot(unittest.TestCase):
    def setUp(self):
        self.penbot = Penbot()

    def test_save_and_get_file(self):
        self.penbot.save_file('test.txt', 'Hello, World!')
        content = self.penbot.get_file('test.txt')
        self.assertEqual(content, 'Hello, World!')

    def test_get_nonexistent_file(self):
        content = self.penbot.get_file('nonexistent.txt')
        self.assertIsNone(content)

    def test_test_file(self):
        self.penbot.save_file('test.txt', 'Hello, World!')
        result = self.penbot.test_file('test.txt', lambda content: 'World' in content)
        self.assertTrue(result)

    def test_test_file_nonexistent(self):
        result = self.penbot.test_file('nonexistent.txt', lambda content: 'World' in content)
        self.assertFalse(result)

    def test_display_logo(self):
        self.assertEqual(self.penbot.logo, "brutnow")

    def test_end_message(self):
        with patch('builtins.print') as mocked_print:
            self.penbot.end_message()
            mocked_print.assert_called_with("Happy hacking!")

    def test_ai_prioritize_vulnerabilities(self):
        vulnerabilities = ["Potential outdated server detected: Apache/2.4.1", "Potential XSS vulnerability detected in response."]
        expected_prioritization = {
            "high_severity": ["Potential outdated server detected: Apache/2.4.1", "Potential XSS vulnerability detected in response."],
            "low_severity": []
        }
        result = self.penbot.ai_prioritize_vulnerabilities(vulnerabilities)
        self.assertEqual(result, expected_prioritization)

if __name__ == '__main__':
    with open('PenBot/test_results.txt', 'w') as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
