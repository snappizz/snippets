'''
Converts SMuFL font metadata into a LilyPond include.
'''
import json
import textwrap

IN_FILENAME = 'bravura-0.7/bravura_metadata.json'
OUT_FILENAME = 'smufl-font-metadata.ily'

PREAMBLE = '''%{
Copyright (c) 2013, Steinberg Media Technologies GmbH (http://www.steinberg.net/), with Reserved Font Name "Bravura".
This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: http://scripts.sil.org/OFL
%}'''

content = json.load(open(IN_FILENAME, 'r'))

outfile = open(OUT_FILENAME, 'w')
outfile.write('\n\n'.join([textwrap.fill(par, 70) for par in PREAMBLE.splitlines()]) + '\n' * 3)

outfile.write("#(define smufl-engraving-defaults '(\n")
for name, value in content.get('engravingDefaults', {}).items():
    outfile.write('  ("{}" . {})\n'.format(name, value))
outfile.write('))\n\n')

outfile.write("#(define smufl-glyph-registration '(\n")
for name, value in content.get('glyphs', {}).items():
    outfile.write('  ("{}" . ('.format(name, value))
    outfile.write(' '.join(['("{}" . ({} . {}))'.format(name, value[0], value[1]) for name, value in value.items()]))
    outfile.write('))\n')
outfile.write('))')

outfile.close()
