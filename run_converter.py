# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from converter.core import CaseConverter

def main():
    parser = argparse.ArgumentParser(description="Text Case Converter")
    parser.add_argument("text", help="Input text (can be snake_case, camelCase, etc.)")
    parser.add_argument("--to", "-t", required=True, 
                        choices=['snake', 'kebab', 'camel', 'pascal', 'upper', 'constant', 'sentence', 'title'],
                        help="Target case format")
    
    args = parser.parse_args()

    result = CaseConverter.convert(args.text, args.to)
    print(result)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
