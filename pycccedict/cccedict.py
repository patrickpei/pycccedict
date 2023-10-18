"""CC-CEDICT."""

import gzip
from pathlib import Path
from typing import Dict, List, Optional, TextIO, Union

class CcCedict:
    """CC-CEDICT."""

    def __init__(self) -> None:
        path = Path(__file__).parent / 'data' / 'cedict_1_0_ts_utf-8_mdbg.txt.gz'
        with gzip.open(path, mode='rt') as file:
            self._parse_file(file)

    def get_definitions(self, chinese: str) -> Optional[List]:
        """Gets definitions."""
        return self._get_field(field='definitions', chinese=chinese)

    def get_pinyin(self, chinese: str) -> Optional[str]:
        """Gets pinyin."""
        return self._get_field(field='pinyin', chinese=chinese)

    def get_simplified(self, chinese: str) -> Optional[str]:
        """Gets simplified."""
        return self._get_field(field='simplified', chinese=chinese)

    def get_traditional(self, chinese: str) -> Optional[str]:
        """Gets traditional."""
        return self._get_field(field='traditional', chinese=chinese)

    def get_entry(self, chinese: str) -> Optional[Dict]:
        """Gets an entry."""
        # Check simplified.
        if chinese in self.simplified_to_index:
            i = self.simplified_to_index[chinese]
            return self.entries[i]

        # Check traditional.
        if chinese in self.traditional_to_index:
            i = self.traditional_to_index[chinese]
            return self.entries[i]

        return None

    def get_entries(self) -> List:
        """Gets all entries."""
        return self.entries

    def _get_field(self, field: str, chinese: str) -> Union[str, List, None]:
        """Gets field."""
        entry = self.get_entry(chinese)
        if entry is None:
            return None

        return entry[field]

    def _parse_file(self, file: TextIO) -> None:
        self.entries = []
        self.simplified_to_index = {}
        self.traditional_to_index = {}
        i = 0

        for line in file:
            entry = self._parse_line(line)
            if entry is None:
                continue

            # Add entry.
            self.entries.append(entry)

            # Share entries for simplified and traditional.
            simplified = entry['simplified']
            traditional = entry['traditional']
            self.simplified_to_index[simplified] = i
            self.traditional_to_index[traditional] = i
            i += 1

    def _parse_line(self, line: str) -> Optional[Dict]:
        # Skip comments.
        if line.startswith('#'):
            return None

        # Strip whitespace and trailing slash.
        line = line.strip()
        line = line.rstrip('/')

        # Get chinese parts.
        chinese, english = line.split('/', maxsplit=1)
        chinese = chinese.strip()
        traditional_and_simplified, pinyin = chinese.split('[')
        traditional_and_simplified = traditional_and_simplified.strip()
        traditional, simplified = traditional_and_simplified.split()

        # Remove brackets around pinyin.
        pinyin = pinyin[:-1]

        # Get english definitions.
        senses = english.split('/')
        glosses = [sense.split(';') for sense in senses]
        definitions = [definition for gloss in glosses for definition in gloss]

        return {
            'traditional': traditional,
            'simplified': simplified,
            'pinyin': pinyin,
            'definitions': definitions,
        }
