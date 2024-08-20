from saltlint.linter.rule import Rule
import re

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
