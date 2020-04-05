#Lumbha-ram
#Computerscience6thsem
#TASK_1
#(Write_a_program_which_will_find_all_such_numbers_which_are_divisible_by_7_but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line)

l=[ ]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print ','.join(l)
