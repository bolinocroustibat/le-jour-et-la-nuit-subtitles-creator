# Le Jour et la Nuit subtitles creator

Generate valid subtitles movie files in any language for the masterpiece movie "[Le Jour et la Nuit](https://en.wikipedia.org/wiki/Day_and_Night_(1997_film))" by [BHL](https://en.wikipedia.org/wiki/Bernard-Henri_L%C3%A9vy).


## Requirements

- Python 3.9 (not tested below 3.9, but it should be fine with 3.8)
- [Poetry](https://python-poetry.org/) (Python packaging manager)

If you don't use Poetry and want to install the Python dependencies manually, the Python requirements are:
- [googletrans](https://pypi.org/project/googletrans/)
- [typer](https://pypi.org/project/typer/)


## Configure

Open the file `config.py` and modify the following values if necessary:
- `OUTPUT_FILENAME`: the path and filename of the output subtitle files <ins>without the extension</ins>. The script will add the language and .srt extension by itself.
- `SOURCE_FILE_URL`: the URL of the source Google Doc with the dialogues transcribed in French, in CSV format (this shouldn't be changed).


## To run

In a terminal, do the following:

- Install Poetry

    - on MacOS, type:
    ```sh
    brew install poetry
    ```
    - on Debian/Ubuntu, type:
    ```sh
    apt-get install poetry
    ```
    - on Windows, use pip:
    ```
    pip install poetry
    ```


- Launch the subtitle creation

    Subtitle file will be exported in the path you defined in `config.py` as `OUTPUT_FILENAME`.

    To convert into French subtitles:
    ```sh
    poetry run python main.py fr
    ```

    To convert into Engligh subtitles:
    ```sh
    poetry run python main.py en
    ```

    To convert into Spanish subtitles:
    ```sh
    poetry run python main.py es
    ```

    etc.


## Available languages

```
'af': 'afrikaans'
'sq': 'albanian'
'am': 'amharic'
'ar': 'arabic'
'hy': 'armenian'
'az': 'azerbaijani'
'eu': 'basque'
'be': 'belarusian'
'bn': 'bengali'
'bs': 'bosnian'
'bg': 'bulgarian'
'ca': 'catalan'
'ceb': 'cebuano'
'ny': 'chichewa'
'zh-cn': 'chinese (simplified)'
'zh-tw': 'chinese (traditional)'
'co': 'corsican'
'hr': 'croatian'
'cs': 'czech'
'da': 'danish'
'nl': 'dutch'
'en': 'english'
'eo': 'esperanto'
'et': 'estonian'
'tl': 'filipino'
'fi': 'finnish'
'fr': 'french'
'fy': 'frisian'
'gl': 'galician'
'ka': 'georgian'
'de': 'german'
'el': 'greek'
'gu': 'gujarati'
'ht': 'haitian creole'
'ha': 'hausa'
'haw': 'hawaiian'
'iw': 'hebrew'
'he': 'hebrew'
'hi': 'hindi'
'hmn': 'hmong'
'hu': 'hungarian'
'is': 'icelandic'
'ig': 'igbo'
'id': 'indonesian'
'ga': 'irish'
'it': 'italian'
'ja': 'japanese'
'jw': 'javanese'
'kn': 'kannada'
'kk': 'kazakh'
'km': 'khmer'
'ko': 'korean'
'ku': 'kurdish (kurmanji)'
'ky': 'kyrgyz'
'lo': 'lao'
'la': 'latin'
'lv': 'latvian'
'lt': 'lithuanian'
'lb': 'luxembourgish'
'mk': 'macedonian'
'mg': 'malagasy'
'ms': 'malay'
'ml': 'malayalam'
'mt': 'maltese'
'mi': 'maori'
'mr': 'marathi'
'mn': 'mongolian'
'my': 'myanmar (burmese)'
'ne': 'nepali'
'no': 'norwegian'
'or': 'odia'
'ps': 'pashto'
'fa': 'persian'
'pl': 'polish'
'pt': 'portuguese'
'pa': 'punjabi'
'ro': 'romanian'
'ru': 'russian'
'sm': 'samoan'
'gd': 'scots gaelic'
'sr': 'serbian'
'st': 'sesotho'
'sn': 'shona'
'sd': 'sindhi'
'si': 'sinhala'
'sk': 'slovak'
'sl': 'slovenian'
'so': 'somali'
'es': 'spanish'
'su': 'sundanese'
'sw': 'swahili'
'sv': 'swedish'
'tg': 'tajik'
'ta': 'tamil'
'te': 'telugu'
'th': 'thai'
'tr': 'turkish'
'uk': 'ukrainian'
'ur': 'urdu'
'ug': 'uyghur'
'uz': 'uzbek'
'vi': 'vietnamese'
'cy': 'welsh'
'xh': 'xhosa'
'yi': 'yiddish'
'yo': 'yoruba'
'zu': 'zulu'
```

To display the available languages, do the following in a Python console:
```python
import googletrans
print(googletrans.LANGUAGES)
```
