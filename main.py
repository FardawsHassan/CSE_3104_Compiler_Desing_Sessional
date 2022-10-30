import re

source_file = open("source.txt","r")
lines = []
tokens = []

KEYWORDS = ['auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while']
LIBRARIES = ['stdio','math','conio']
PREPROCESSORS = ['include','define','undef','ifdef','ifndef','if','else','elif','endif','error','pragma']

# key = ""
# s = ""
# for item in key.split():
#     s = s + "'" + item[1:] + "',"
# print(s)

for line in source_file:
    lines.append(line)

lines = [i.strip('\n\t') for i in lines if i!='\n']
lines_last_token = []


tokens = []
tk_string = ''

i = -1
for token in lines:
    for j in range(len(token)):
        if(token[j].isalnum()):
            tk_string = tk_string+token[j]
        else:
            if(tk_string!=''):
                tokens.append(tk_string)
                i = i+1
            tk_string = ''
            if(len(tokens)!=0 and tokens[-1]==' '):
                continue
            tokens.append(token[j])
            i=i+1
    if(tk_string!=''):
        tokens.append(tk_string)
        i=i+1
        tk_string = ''
    lines_last_token.append(i)
    
    


# print('\n\nLines list: '+str(lines)+'\n')

print("\n\nLines are:")
for line in lines:
    print('\t'+line)


print("\n\nlast tokens of line: "+str(lines_last_token))

print('\n\nTokens are: ')
for item in tokens:
    print("\t"+str(item))



s = ''
at_token = 0
for i in range(len(tokens)):
    if(tokens[i]=='#'):
        s = ''.join(tokens[i:lines_last_token[i]+1])
        at_token = at_token + 1
        pattern = '# *include *<stdio. *h *>'
        if(not re.match(pattern,s)):
            print('Invalid header file')
        s *= 0



















source_file.close()