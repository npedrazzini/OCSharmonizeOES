# Python script to harmonize East Slavic and Old Church Slavonic orthographies.
# Not all manuscript variants have been included
# since the script was used on a normalized text already (i.e. with reduced orthographic differences).
# Other transformations can be easily added under "variants = [..."

import re

file = open('filename.txt')
for line in file:
    variants = [
        (r'\bа', 'я'),
        (r'\Bии\B', 'и'),
        (r'ии\b', 'ь'),
        (r'ыи\b', 'ъ'),
        ('ꙑ', 'ы'),
        ('ѧ', 'я'),
        ('ꙗ', 'я'),
        ('ѩ', 'я'),
        ('ѣ', 'е'),
        ('є', 'е'),
        ('ѥ', 'е'),
        ('ѣ', 'е'),
        ('ѹ', 'у'),
        ('оу', 'у'),
        ('ѫ', 'у'),
        ('ꙋ', 'у'),
        ('ѭ̑', 'ю'),
        ('ѕ', 'з'),
        ('ꙁ', 'з'),
        ('і', 'и'),
        ('ї', 'и'),
        ('ѡ', 'о'),
        ('ѭ', 'ю')
        ]
    for old, new in variants:
        line = re.sub(old, new, line)

    # bring all TЪRT TЬRT variants to TRЪT TLЬT
    torttolt = [
        ('ьр', 'рь'),
        ('ър', 'ръ'),
        ('ьл', 'ль'),
        ('ъл', 'лъ')
    ]
    for old, new in torttolt:
        # condition: "ЪR ЬR is between consonants"
        # The addition of characters already replaced in the first part of the script
        # is technically superfluous, but added to facilitate future reuses
        if re.match(r'(?<![аеєиїоуѹꙋъыꙑьѣꙗѥюѫѭѧѩѵ])(?![аеєиїоуѹꙋъыꙑьѣꙗюѫѭѧѩѵ])', line):
            line = re.sub(old, new, line)
    print(line)