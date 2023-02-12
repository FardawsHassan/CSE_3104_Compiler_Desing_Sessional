import re

class Tokenizer:

    def __init__ (self,file_path):
        self._sourceCode = open(file_path,'r')
        self._lines = []
        self._tokens = []

        ### get line by line from source code
        for line in self._sourceCode:
            self._lines.append(line)

        # debugging: printing source code
        print("\nSource code:")
        print("................")
        print(self._lines)
        print("\n")

        ### remove comments
        self.__remove_comments()

        # debugging: printing source code after cleaning
        print("\nSource code after Cleaning and removing comments:")
        print("...................................................")
        for item in self._lines:
            print(item)
        print("\n")


        ### tokenization
        self.__tokenize()

        # debugging: printing tokens form source code
        print("\nTokens form source code:")
        print(".........................")
        for item in self._tokens:
            print(item)

    

    def __remove_comments(self):
        self.cleanedLines = []

        #removed single line comments
        for line in self._lines:
            result = re.search(r"^//",line.strip('\n\t').strip())
            if(result is None):
                line = line[:-1]
                line = line.strip()
                if(line != ''):
                    self.cleanedLines.append(line)

        #removed multiple line comments
        self._lines = self.cleanedLines[:]
        self.cleanedLines.clear()
        i = 0
        flag = 0
        while(i<len(self._lines)):
            if(flag==0):
                result = re.search(r"^/\*",self._lines[i])
                if(result is None):
                    self.cleanedLines.append(self._lines[i])
                else:
                    flag = 1
                    i = i+1
                    continue
            if(flag==1):
                result = re.search(r".*\*/",self._lines[i])
                if(result is not None):
                    flag = 0
            i = i+1

        self._lines.clear()
        self._lines = self.cleanedLines[:]


    
    def __tokenize(self):
        self.line_tokens = []

        ### tokenizing lines by seperator
        for line in self._lines:
            self.line_tokens.clear()
            self.token = ''
            i = 0
            while(i<len(line)):
                if(line[i].isalnum()):
                    self.token = self.token+line[i]
                else:
                    self.line_tokens.append(self.token)
                    self.token = ''

                    if(line[i] !=' '):
                        self.line_tokens.append(line[i])
                
                i = i+1 
            if(len(self.token)>0):
                self.line_tokens.append(self.token)
            self._tokens.append([ item for item in self.line_tokens if item!=''])
    

    def getTokens(self):
        return self._tokens


    def getLines(self):
        return self._lines