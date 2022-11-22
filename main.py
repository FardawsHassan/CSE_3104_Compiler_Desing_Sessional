import re

source_file = open("source.txt","r")
lines = []
tokens = []

KEYWORDS = ['auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while']
LIBRARIES = ['stdio','math','conio']
PREPROCESSORS = ['include','define','undef','ifdef','ifndef','if','else','elif','endif','error','pragma']
VAR_TYPE = ['char','int','float','double','long','short']



#### keywords list builder
# key = ""
# s = ""
# for item in key.split():
#     s = s + "'" + item[1:] + "',"
# print(s)


for line in source_file:
    lines.append(line)
lines = [i.strip('\n\t').strip() for i in lines if i!='\n']


#### Line end token
lines_last_token = []

### Tokenization
####################
tk_string = ''
i = -1
for token in lines:
    if(token[0:2]=='//'):
        continue
    for j in range(len(token)):
        if(token[j].isalnum() or token[j]=='.'):
            tk_string = tk_string+token[j]
        else:
            if(tk_string!=''):
                tokens.append(tk_string)
                i = i+1
            tk_string = ''
            if(len(tokens)!=0 and tokens[-1]==' '):
                if(token[j]!=' '):
                    tokens.append(token[j])
                    i = i+1
                continue
            tokens.append(token[j])
            i = i+1
    if(tk_string!=''):
        tokens.append(tk_string)
        i = i+1
        tk_string = ''
    lines_last_token.append(i)


### Printing for debugging    
# print(lines_last_token)
print("\n\nLines are:")
for line in lines:
    print('\t'+line)

print('\n\nTokens are: ')
for item in tokens:
    print("\t"+str(item))



def header_validation(s):
    #patter generator for header 
    tmp_s = ''
    for item in LIBRARIES:
        tmp_s = tmp_s + str(item)+'|'
    pattern = '# *include *<('+ tmp_s[:-1]+').h *>'
    # print(s)
    # print(pattern)

    if(re.match(pattern,s)):
        return True


def body_validation(s):
    #patter generator for header 
    tmp_s = ''

    pattern = 'int *main *\( *\) *{ *return *0 *; *}'
    # print(s)
    # print(pattern)

    if(re.match(pattern,s)):
        return True




print('\n\n\nCompiling:')
s = ''
at_token = 0
i = 0
while(True):
    if(tokens[i]=='#'):
        s = ''.join(tokens[i:lines_last_token[at_token]+1])
        # next line
        at_token = at_token + 1
        i = lines_last_token[at_token-1]+1
        if(not header_validation(s)):
            print('\tError: invalid header file.')
            s *= 0
            continue
        else:
            print('\t...valid header.')
            continue
    if(tokens[i] in VAR_TYPE or tokens[i]=='void'):
        # if(lines_last_token[at_token]!=';'):
        s = ''.join(tokens[i:])
        if(not body_validation(s)):
            print('\tError: Invalid body.')
            s *= 0
        else:
            print('\t...valid body.')

            
    break

print('\n')




















source_file.close()