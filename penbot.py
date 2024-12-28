class Penbot:
    def __init__(self):
        self.files = {}
        self.logo = "brutnow"

    def save_file(self, filename, content):
        self.files[filename] = content

    def get_file(self, filename):
        return self.files.get(filename, None)

    def test_file(self, filename, test_func):
        content = self.get_file(filename)
        if content is None:
            return False
        return test_func(content)

    def test_and_save(self, filename, content, test_func):
        if test_func(content):
            self.save_file(filename, content)
            return True
        return False

    def display_logo(self):
        print(self.logo)

    def end_message(self):
        print("Happy hacking!")

    def ai_prioritize_vulnerabilities(self, vulnerabilities):
        high_severity = [v for v in vulnerabilities if "Potential" in v]
        low_severity = [v for v in vulnerabilities if "Potential" not in v]
        return {
            "high_severity": high_severity,
            "low_severity": low_severity
        }
