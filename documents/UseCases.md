# Project

To develop an e-lexcon of French language

# Use Cases

#### 1. Parse a word - the app takes a word as input and returns morphological parse information, such as part of speech (incl. gender or verb group, etc.), meaning in English, word origin(if possible).

Input: `aimer`
Output: `aimer` `verbe` `1` `amare` `latin`


Input: `cheval`
Output: `cheval, chevaux` `nom` `masculin` `caballus, rosse` `latin populaire`

Input: `difficile`
Output: `difficile` `adjectif` `difficilis` `latin`

Input: `cet`
Output: `ce, cette, ces` `adjectif` `*ecce istum, istam, d'où cet, cette, etc.` `latin populaire`

#### 2. verb conjugation - the app takes a infinitive verb and returns all conjugation.
See https://la-conjugaison.nouvelobs.com/

#### 3. Phonology - the app takes a string and read aloud.

Input: `Je t'aime.`
Output: pronounced sound of the Input

