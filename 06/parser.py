import sys
filename='Max.asm'

class Parser():

    clean_length= 13
    @staticmethod
    def comment_white(x):
        if x!=None:
            if x.startswith('/'):
                return False
            else:
                return True

    @classmethod
    def hasMoreLines(cls, previous_line):
        if previous_line < Parser.clean_length:
            return True
        else:
            return False
    @classmethod
    def advance(cls, morelines, previous_line, f_in):
        if morelines:
            next_line = previous_line + 1
            return f_in.readline(next_line)



    @staticmethod
    def instructionType(line):
        if line.strip().startswith('@'):
            #print('A_INSTRUCTION')
            return 'A_INSTRUCTION'
        elif line.strip().startswith('('):
            #print('L_INSTRUCTION')
            return 'L_INSTRUCTION'
        else:
            #print('C_INSTRUCTION')
            return 'C_INSTRUCTION'

    @staticmethod
    def symbol(line, instruction):
        if instruction=='L_INSTRUCTION':
            #print(line.replace('(', '').replace(')', ''))
            return line.replace('(', '').replace(')', '')
        elif instruction=='A_INSTRUCTION':
            #print(line.replace('@', ''))
            return line.replace('@', '')

    @staticmethod
    def dest(line, instruction):
        if instruction=='C_INSTRUCTION':
            #print(line.partition('=')[0])
            if '=' in line:
                return line.partition('=')[0]
            else:
                return ' '

    @staticmethod
    def comp(line, instruction):
        if instruction=='C_INSTRUCTION':
            if '=' in line:
                line = line.partition('=')[2]
            line =line.partition(';')[0]
            #print(line)
            return line
    @staticmethod
    def jump(line, instruction):
        if instruction=='C_INSTRUCTION':
            if ';' in line:
                line = line.partition(';')[-1]
                #print(line)
                return line