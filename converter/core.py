# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re

class CaseConverter:
    @staticmethod
    def to_words(text):
        """Splits text into a list of words, handling various separators."""
        # Replace non-alphanumeric with space
        text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
        # Handle camelCase/PascalCase splitting: "camelCase" -> "camel Case"
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
        # Handle acronyms like "XMLParser" -> "XML Parser"
        text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)
        
        return [w.lower() for w in text.split() if w]

    @staticmethod
    def convert(text, target_case):
        words = CaseConverter.to_words(text)
        if not words:
            return ""

        if target_case == 'snake':
            return "_".join(words)
        
        elif target_case == 'kebab':
            return "-".join(words)
        
        elif target_case == 'camel':
            return words[0] + "".join(w.title() for w in words[1:])
        
        elif target_case == 'pascal':
            return "".join(w.title() for w in words)
        
        elif target_case == 'upper':
            return "_".join(words).upper()
        
        elif target_case == 'constant':
            return "_".join(words).upper() # Alias for upper snake case
            
        elif target_case == 'sentence':
            return " ".join(words).capitalize()

        elif target_case == 'title':
            return " ".join(w.title() for w in words)
            
        return text

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
