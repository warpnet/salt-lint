import unittest
from saltlint.linter.rule import Rule
import re
from saltlint.rules import CompoundMatchSpacesRule
class CompoundMatchSpacesRule(Rule):
    id = '220'
    shortdesc = 'Ensure spaces around parentheses in compound matches'
    description = 'Compound matches should have spaces around parentheses to ensure proper parsing by Salt.'
    severity = 'HIGH'
    tags = ['formatting', 'compound-match']
    version_added = 'v0.9.2'
    
    regex = re.compile(r'\([^ ]|[^ ]\)')

    def match(self, file, line):
        if not file["path"].endswith("top.sls"):
            return self.regex.search(line)
        return None


class TestCompoundMatchSpacesRule(unittest.TestCase):
    def setUp(self):
        self.rule = CompoundMatchSpacesRule()
    
    def test_no_match_non_top_sls(self):
        file = {"path": "init.sls"}
        line = "some line without parentheses"
        self.assertIsNone(self.rule.match(file, line))

    def test_no_match_top_sls(self):
        file = {"path": "top.sls"}
        line = "No match (line)"
        self.assertIsNone(self.rule.match(file, line))

    def test_match_missing_space_after_open_paren(self):
        file = {"path": "some_state.sls"}
        line = "compound_match: G@os:(Ubuntu or CentOS)"
        self.assertIsNotNone(self.rule.match(file, line))
    
    def test_match_missing_space_before_close_paren(self):
        file = {"path": "some_state.sls"}
        line = "compound_match: G@os:( Ubuntu or CentOS)"
        self.assertIsNotNone(self.rule.match(file, line))
    
    def test_match_missing_spaces_both_sides(self):
        file = {"path": "some_state.sls"}
        line = "compound_match: G@os:(Ubuntu or CentOS )"
        self.assertIsNotNone(self.rule.match(file, line))
    
    def test_no_match_correct_spacing(self):
        file = {"path": "some_state.sls"}
        line = "compound_match: G@os: ( Ubuntu or CentOS )"
        self.assertIsNone(self.rule.match(file, line))

if __name__ == '__main__':
    unittest.main()
