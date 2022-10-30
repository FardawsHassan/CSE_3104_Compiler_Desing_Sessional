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


tokens = []
tk_string = ''
for token in lines:
    for j in range(len(token)):
        if(token[j].isalnum()):
            tk_string = tk_string+token[j]
        else:
            if(tk_string!=''):
                tokens.append(tk_string)
            tk_string = ''
            if(len(tokens)!=0 and tokens[-1]==' '):
                continue
            tokens.append(token[j])
    if(tk_string!=''):
        tokens.append(tk_string)
        tk_string = ''


# print('\n\nLines list: '+str(lines)+'\n')

print("\n\nLines are:")
for line in lines:
    print('\t'+line)


print('\n\nTokens are: ')
for item in tokens:
    print("\t"+str(item))




for i in range(len(tokens)):
    if(tokens[i]=='#'):
        i = i+1
        if(tokens[i]==' '):
            i = i+1
        if(tokens[i]=='include'):
            i = i+1
        if(tokens[i]==' '):
            i = i+1
        if(tokens[i]=='<'):
            i = i+1
        else:
            print("header file error, '<' missing.")
            i = i+1
        if(tokens[i] in PREPROCESSORS):
            i = i+1
        else:
            print("Invalid header file")



















source_file.close()