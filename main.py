from lexical_analyzer import Tokenizer
import syntax_semantic_analyzer as compiler
import re

DATA_TYPE = ['int','float','double','char']
ERRORS = []

### make tokens from source code
#..............................#
t = Tokenizer('source.c')
tokens = t.getTokens()
lines = t.getLines()

allTokens = [token for item in tokens for token in item]
allLines = " ".join(lines)

# print(allTokens)
# print(allLines)


### debug: printing all tokens
# print('.........................')
# for lineTokens in tokens:
#     for token in lineTokens:
#         print(token)


### all line ending token numbers
lineEndTokneNo = []
a = -1
for lineToken in tokens:
    a = a + len(lineToken)
    lineEndTokneNo.append(a)
# print('\nall line ending token numbers:')
# print(lineEndTokneNo)
print('\n\nRunning Code: ')
print('...................')
compiler.run_code()