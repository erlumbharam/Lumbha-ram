#Lumbha-ram
#Computerscience6thsem
#TASK_1
#(Write_a_program_which_will_find_all_such_numbers_which_are_divisible_by_7_but_are_not_a_multipleof_5,_between_2000_and_3200_(both included)._The_numbers_obtained_should_be_printed_in_a
comma_separated_sequence_on_a_single_line)

l=[ ]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print ','.join(l)
