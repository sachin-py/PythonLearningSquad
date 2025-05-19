"""
====================================================================
Language Translator Script
====================================================================

DESCRIPTION:
------------
This Python script detects the language of user-provided input text,
translates it into a target language using Google Translate (via the
googletrans library), and saves both the original and translated text
into a file named 'language.txt'.

FEATURES:
---------
Detects the language of the input text.
Translates the text into a user-specified target language.
Saves input and translated text to 'language.txt' (UTF-8 encoded).

REQUIREMENTS:
-------------
- Python 3.x
- googletrans==4.0.0rc1

INSTALLATION:
-------------
To install the required package, run:
    pip install googletrans==4.0.0rc1

LANGUAGE CODES:
---------------
Here are some common language codes you can use:
- English:    en
- Hindi:      hi
- Spanish:    es
- French:     fr
- German:     de
- Italian:    it
- Portuguese: pt
- Russian:    ru
- Chinese:    zh-CN
- Japanese:   ja
- Korean:     ko
- Arabic:     ar

USAGE:
------
Run the script.
Enter the text you want to translate.
Enter the target language code (see above).
Check 'language.txt' for saved results.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

====================================================================
"""

from googletrans import Translator


def main():
    # Initialize the translator
    translator = Translator()

    # Prompt user for input text
    user_input = input('Enter the text to translate: ').strip()
    if not user_input:
        print("No text provided. Exiting.")
        return

    # Detect the language of the input text
    detected = translator.detect(user_input)
    source_language = detected.lang
    print(f'Detected Language: {source_language}')

    # Prompt user for target language code
    target_language = input(
        'Enter the target language code (e.g., en, hi, es): ').strip()
    if not target_language:
        print("No target language provided. Exiting.")
        return

    try:
        # Perform translation
        translated = translator.translate(
            user_input, src=source_language, dest=target_language)
        translated_text = translated.text
        print(f'Translated Text: {translated_text}')

        # Save to file
        with open('language.txt', 'a', encoding='utf-8') as file:
            file.write('\n')
            file.write(f'Input text: {user_input}\n')
            file.write(
                f'Translated ({source_language} → {target_language}): {translated_text}\n')

        print("Translation saved to 'language.txt'.")

    except Exception as e:
        print(f"An error occurred during translation: {e}")


if __name__ == "__main__":
    main()
