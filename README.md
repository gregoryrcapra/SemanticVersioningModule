# SemanticVersioningModule

Python module implementing semantic versioning

### Semantic Versioning Format, as specified [here](https://semver.org/):

  - X.Y.Z, where X,Y,Z >= 0
  - no leading 0s
  - X is major version, Y is minor version, Z is patch version
  - strictly increasing numerically
  - 1.0.0 is initial state
  - when incrementing Y, Z set to 0
  - when incrementing Z, Y & Z set to 0

  - Pre-Release:
    - must be X.Y.Z followed only by hyphen and series of dot seperated identifiers
    - identifiers can only be in [0-9A-Za-z]
    - identifiers cannot be empty
    - these pre-releases have lower precedence than associated normal version, but higher than non-pre-release with lower precedence X.Y.Z number
    - two versions with identical X.Y.Z. identifiers are compared by pre-release identifiers, left-to-right until difference found, numeric identifiers lower precedence than non-numeric, and non-numeric are compared lexically in ASCII sort order
  
  - Build Metadata:
    - denoted by "+" and series of dot separated identifiers (same as pre-release)
    - identifiers can't be empty
    - can follow patch or pre-release version
    - ignored in precedence
    
### Instructions for Running

1) Make sure you have a version of Python downloaded (Anaconda, for example)
2) Run test.py from your IDE or command line
3) Enter in sample test input after unit tests complete
4) According to the format guidelines specified above and on [this](https://semver.org/) web page, your input should either return 'before', 'after', 'invalid', or 'equal.

*For example: '4.4.5 4.4.6' -> 'after', '1.9.6 1.0.9' -> 'before', '1.4.5-alpha 1.4.5-beta' -> 'after', '0.3.4 1.3.4' -> 'invalid',
'1.3..4 1.3.4' -> 'invalid', '1.3.4-alpha+carrots.44 1.3.4-alpha' -> 'equal'*
