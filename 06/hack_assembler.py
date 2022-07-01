import sys
from parser import Parser
from codex  import Codex
filename = 'Pong.asm'

hack_file = filename.partition('.')[0]+'.hack'


############Symbol Table#####################
predef_symTable1 = {'SCREEN':16384, 'KBD':24576, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4}
for i in range(16):
    key = 'R'+ str(i)
    predef_symTable1[key] = i
predef_symTable= predef_symTable1

labels = {}
variables = {}

symTable ={}

###########################################################

with open(filename) as f_in:
    f_filter= filter(None , (line.strip() for line in f_in))
    num = 0
    for i in (x for x in f_filter if not x.startswith('/')):
        i = i.partition('//')[0].strip()
        instruc = Parser.instructionType(i)
        if instruc=='L_INSTRUCTION':
            lab = Parser.symbol(i, instruc)
            labels[lab] = num
        else:
            num=num+1
    print(labels)
    symTable = {**predef_symTable, **labels }

with open(hack_file,'w',encoding = 'utf-8') as f_write:
    with open(filename) as f_in:
        f_filter= filter(None , (line.strip() for line in f_in))

        for i in (x for x in f_filter if not x.startswith('/')):
            i = i.partition('//')[0].strip()
            instruc = Parser.instructionType(i)
            if instruc =='C_INSTRUCTION':
                dest_sym = Parser.dest(i, instruc)
                dest_bin = Codex.dest(dest_sym)
                comp_sym = Parser.comp(i, instruc)
                print(comp_sym)
                comp_bin = Codex.comp(comp_sym)
                print(comp_bin)
                jump_sym = Parser.jump(i, instruc)
                jump_bin = Codex.jump(jump_sym)
                C_instr_bin = ('111'+ comp_bin+dest_bin+ jump_bin)
                print(C_instr_bin)
                f_write.write(C_instr_bin)
                f_write.write('\n')
            
            if instruc =='A_INSTRUCTION':
                a_symb = Parser.symbol(i, instruc)
                if a_symb.isnumeric():
                    a_bin = '{0:015b}'.format(int(a_symb))
                    a_bin = '0'+a_bin
                    print(a_bin)
                    f_write.write(a_bin)
                    f_write.write('\n')
                elif a_symb.isnumeric()==False:
                    if a_symb in symTable:
                        a_bin = '{0:015b}'.format(int(symTable[a_symb]))
                        a_bin = '0'+a_bin
                        print(a_bin)
                        f_write.write(a_bin)
                        f_write.write('\n')
                    else:
                        if len(variables)==0:
                            variables[a_symb] = 16
                            symTable[a_symb] = 16
                            a_bin = '{0:015b}'.format(int(symTable[a_symb]))
                            a_bin = '0'+a_bin
                            print(a_bin)
                            f_write.write(a_bin)
                            f_write.write('\n')
                        else:
                            last_value_in_var = list(variables.values())[-1]
                            variables[a_symb] = last_value_in_var +1
                            symTable[a_symb] = last_value_in_var +1
                            a_bin = '{0:015b}'.format(int(symTable[a_symb]))
                            a_bin = '0'+a_bin
                            print(a_bin)
                            f_write.write(a_bin)
                            f_write.write('\n')
                

        





            


