import sys

class Codex():
    @staticmethod 
    def dest(instr=' '):
            temp = [0, 0, 0]
            check = False
            #check if the input is correct
            for i in list(instr):
                if i  in ['D', 'M', 'A', ' ']:
                    check = True
                else:
                    sys.exit('wrong memory destination!')
            if check:
                if "A" in instr:
                    temp[0] = 1
                if "D" in instr:
                    temp[1] = 1
                if "M" in instr:
                    temp[2] = 1
                return ''.join(str(i) for i in temp) 

    @staticmethod
    def jump(instr):
        table_j = {None: '000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 
        'JLT': '100', 'JNE':'101', 'JLE': '110', 'JMP': '111' }
        if instr in table_j:
            return table_j[instr] 
        else:
            sys.exit('Wrong jump input!')
    
    @staticmethod
    def comp(instr):

        table_c = {'0': '0101010', '1':'0111111', '-1': '0111010', 'D': '0001100',
        'A': '0110000', 'M':'1110000', '!D': '0001101', '!A':'0110001', '!M': '1110001',
        '-D': '0001111', '-A': '0110011', '-M': '1110011', 'D+1': '0011111', 'A+1': '0110111',
        'M+1': '1110111', 'D-1':'0001110', 'A-1': '0110010', 'M-1': '1110010', 'D+A': '0000010',
        'D+M': '1000010', 'D-A': '0010011', 'D-M': '1010011', 'A-D': '0000111', 'M-D':'1000111',
        'D&A': '0000000', 'D&M': '1000000', 'D|A': '0010101', 'D|M':'1010101'
        }
        if instr in table_c:
            #print(table_c[instr])
            return table_c[instr]
        else:
            sys.exit('Wrong c command!')