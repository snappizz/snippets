\version "2.17.97"

\include "definitions.ily"

\pointAndClickOff

music = \relative c' {
  \clef alto
  \time 3/4
  c4-.(\f\< d4-. es4-.) |
  \time 4/4
  fis8.---\trill\sfz\> e!16 d16->\niente r16 r8 c2-\prall |
  \time 2/2
  \clef treble
  r2-\fermata c8( eeh8)-^ \tuplet 3/2 { eeh8( gisih8 b')-! } |
}

<<
  \new Staff \with { instrumentName = "Feta" } \music
  \new Staff \with { \bravuraOn instrumentName = "Bravura" } \music
>>
