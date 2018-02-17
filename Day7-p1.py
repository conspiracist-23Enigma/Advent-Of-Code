programs = []

while True:
    input_prog = (input().replace(',','')).split()
    if input_prog == []:
        break
    elif len(input_prog) > 3:
        programs += [input_prog]

sub_programs = set()
for prog in programs:
    for sub_prog in prog[3:]:
        sub_programs.add(sub_prog)

for prog in programs:
    if not (prog[0] in sub_programs):
        print (prog[0])
        break;

