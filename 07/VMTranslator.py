#filename : VMTranslator.py
#author : Meylis MALIKOV
#date : 24.05.22
import sys
from fileinput import filename


class Parser:
    def __init__(self, input_file):
        self.file_in = open(input_file)
    
        self.file_in_list = [] 
        for line in self.file_in:
            line = line.strip()
            if line and line[0]!='/':
                line = line.partition('//')[0].rstrip()    #remove the comments coming after command
                self.file_in_list.append(line)

        self.last_line_idx = len(self.file_in_list)-1
        self.current_line_idx = -1
        self.current_command = ' '
        self.arithmetic_cmmd = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']

    def hasMoreCommands(self)-> bool:
        if (self.current_line_idx ) < self.last_line_idx:
            return True  
        else:
            return False

    def advance(self):
        self.current_line_idx+=1
        current_command = self.file_in_list[self.current_line_idx]
        self.current_command = current_command
    
    def commandType(self):
        if self.current_command in self.arithmetic_cmmd:
            return 'C_ARITHMETIC'
        elif self.current_command == 'return':
            return 'C_RETURN'
        elif self.current_command.partition(' ')[0] == 'push':
            return 'C_PUSH'
        elif self.current_command.partition(' ')[0] == 'pop':
            return 'C_POP'
        elif self.current_command.partition(' ')[0] == 'label':
            return 'C_LABEL'
        elif self.current_command.partition(' ')[0] == 'goto':
            return 'C_GOTO'
        elif self.current_command.partition(' ')[0] == 'if-goto':
            return 'C_IF'
        elif self.current_command.partition(' ')[0] == 'function':
            return 'C_FUNCTION'
        elif self.current_command.partition(' ')[0] == 'call':
            return 'C_CALL'
        else:
            raise Exception('Wrong command type!')
        
    def arg1(self):
        arg1 = self.current_command.split(' ')[1]
        return arg1

    def arg2(self):
        arg2 = self.current_command.split(' ')[2]
        return int(arg2)



class CodeWriter:
    def __init__(self, output_file):
        self.file_out = open(output_file, 'w')
        self.base_addr_dict = {'SP': 0, 'local': 'LCL', 'argument': 'ARG', 'this':'THIS', 'that':'THAT'}


    def writeArithmetic(self, command):
        self.file_out.write('//'+command)
    
    def writePushPop(self, command, segment, index):  #index should be integer
        segment = self.base_addr_dict[segment]
        self.file_out.write('//'+command + segment + str(index))
        
        if command == 'C_PUSH':         
            self.file_out.write(f'@{index}')        # @index
            self.file_out.write('D=A')              # D = A
            self.file_out.write(f'@{segment}')      # @segment
            self.file_out.write('A=D+A')            # A = D + M
            self.file_out.write('D=M')              # D = M
            self.file_out.write(f'@SP')             # @SP
            self.file_out.write('A=M')              # A = M
            self.file_out.write('M = D')            # M = D
            self.file_out.write('@SP')              # @SP
            self.file_out.write('M = M+1')          # M = M+1

        if command =='C_POP':
            self.file_out.write(f'@{index}')        # @index
            self.file_out.write('D = A')

        pass

class Main:
    pass

file_test = Parser('BasicTest.vm')
while file_test.hasMoreCommands():
    file_test.advance()
    print(file_test.current_command)
    print(file_test.commandType())
file_test.file_in.close()
