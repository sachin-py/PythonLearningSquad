"""
==============================================================================
Language Translator Script using googletrans
==============================================================================

DESCRIPTION:
------------
This script takes a user-provided text input, detects its language, translates
it into a target language of the user's choice, and saves both the original and
translated text into a local file called 'language.txt'.

It uses the googletrans library (Google Translate API wrapper) to perform
language detection and translation.

LANGUAGE CODES (examples):
--------------------------
- en      → English
- hi      → Hindi
- es      → Spanish
- fr      → French
- de      → German
- it      → Italian
- pt      → Portuguese
- ru      → Russian
- zh-CN   → Chinese (Simplified)
- ja      → Japanese
- ko      → Korean
- ar      → Arabic

INSTALLATION:
-------------
Make sure you have the required package installed:
    pip install googletrans==4.0.0rc1

USAGE:
------
1. Run this script.
2. When prompted, enter the text you want to translate.
3. When prompted, enter the target language code.
4. The script will detect the input language, translate the text, display the
   result, and append both the input and translated text to 'language.txt'.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

==============================================================================

"""

from googletrans import Translator

# Initialize the Translator object
translator = Translator()

# Prompt the user to enter the text for translation
user_input = input('Enter the text: ')
if not user_input.strip():
    print("No input provided. Exiting.")
    exit()

# Detect the language of the input text
detected_language = translator.detect(user_input).lang
print('Detected Language is:', detected_language)

# Prompt the user to enter the target language code
target_language = input('Enter the target language (e.g., en, hi, es, fr): ')
if not target_language.strip():
    print("No target language provided. Exiting.")
    exit()

# Perform the translation
translated_text = translator.translate(
    user_input, src=detected_language, dest=target_language
).text

# Save the original and translated text to a file
with open('language.txt', 'a', encoding='utf-8') as f:
    f.write('\n')
    f.write('Input text: ' + user_input + '\n')
    f.write('Translated text: ' + translated_text + '\n')

# Display the translated text to the user
print('Translated text:', translated_text)
print("Translation saved to 'language.txt'.")
