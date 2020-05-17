num_bits = 15
tap_bits = [14, 15]
log2_integer = 7
bools = ['false', 'true ']

script = []


for b_num,b in enumerate(bools):
    t = 'alias decision_tree_bit_1_{} decision_{}{}'.format(b, b_num, 'X' * (log2_integer - 1))
    script.append(t)

script.append('')

for n in range(1, log2_integer, 1):
    for i in range(1 << n):
        s = "{:0{}b}".format(i, n)
        
        s1 = s
        s1 = s1 + "X" * (log2_integer - len(s1))
        t = 'alias decision_{} "'.format(s1)
        
        for b_num,b in enumerate(bools):
            s2 = s + str(b_num)
            s2 = s2 + "X" * (log2_integer - len(s2))
        
            t += 'alias decision_tree_bit_{}_{} decision_{} ; '.format(
               n+1, b, s2)
        
        t += '"'
        script.append(t)
     
script.append('')


for i in range(2**log2_integer):
    t = 'alias "trashcan{}" "echo (rerolling) saying banter #{} = {:0{}b} ; rotate_bits ; decision"'.format(i, i, i, log2_integer)
    script.append(t)

script.append('')


for i in range(2**log2_integer):
    s = "{:0{}b}".format(i, log2_integer)
    t = 'alias decision_{} "alias decision trashcan{}"'.format(s, i)
    script.append(t)



# command to set a bit to a specific value
for b in bools:
    script.append('')
    for i in range(1, num_bits + 1, 1):
        t = 'alias set_bit{}_{} "alias bit{} bit{}_{}"'.format(i, b, i, i, b)
        script.append(t)

script.append('')

"""
controls what happens when you actually set a bit to a value

includes command to rotate the next bit cyclically
have to treat last/first bit differently
        
because this involves flipping the xor accumulator for the tap bits,
running this multiple times will cause a bug (side effects)
"""
for b_num,b in enumerate(bools):
    script.append('')
    for i in range(1, num_bits + 1, 1):
        t = 'alias bit{}_{} "' \
            'alias rotate_bit{} set_bit{}_{} ; ' \
            'alias print_bit{} echo bit{} = {}' \
            ''.format(i, b, 
                       i+1, i+1, b,
                       i, i, b_num)
            
        # same as above, but also toggle the xor accumulator
        if i in tap_bits and b.startswith('true'):
            t += ' ; toggle_xor_accumulator'     
            
        if i <= log2_integer:
            t += ' ; decision_tree_bit_{}_{}'.format(i, b)
            
        t = t + '"'
        script.append(t)


script.append('')

t = 'alias set_xor_accumulator_false "' \
    'alias toggle_xor_accumulator set_xor_accumulator_true ; ' \
    'alias rotate_bit1 set_bit1_false'
script.append(t)

t = 'alias set_xor_accumulator_true "' \
    'alias toggle_xor_accumulator set_xor_accumulator_false ; ' \
    'alias rotate_bit1 set_bit1_true'
script.append(t)


script.append('')

# command to cyclically rotate all the bits
t = 'alias rotate_bits "'
for i in range(1, num_bits + 1, 1)[::-1]:
    t += 'rotate_bit{} ; '.format(i, i)
t += 'set_xor_accumulator_false ; '
for i in range(1, num_bits + 1, 1):
    t += 'bit{} ; '.format(i, i)
script.append(t)


script.append('')
t = 'alias print_bits "'
for i in range(1, num_bits + 1, 1):
    t += 'print_bit{} ; '.format(i)
t += '"'
script.append(t)


script.append('')

t = 'alias rng "' + "rotate_bits ; " * (log2_integer) + 'decision"'
script.append(t)

script.append('')


# initialize registers
t = 'set_xor_accumulator_false'
script.append(t)

# a random 128-bit prime number
seed = 339582161354900657370473467565847151939
for i in range(1, num_bits + 1, 1):
    t = 'set_bit{}_{} ; bit{}'.format(i, bools[(seed >> i) & 1], i)
    script.append(t)

script.append('')


script_txt = '\n'.join(script)


print(script_txt)

script_txt += """
bind mouse1 "+attack; rng"

// Adds randomness to the shuffling
bind w "+mfwd; rotate_bits"
bind s "+mback; rotate_bits"
bind a "+mleft; rotate_bits"
bind d "+mright; rotate_bits"
"""

script_txt += """
alias "trashcan0" "say how are you typing so fast"
alias "trashcan1" "say how do i fly as demonstration man"
alias "trashcan2" "say what button make assassin go transparent"
alias "trashcan3" "say how make tuxedo terrorist do lobster dance?"
alias "trashcan4" "say how to eat hoagie as big machinegun man"
alias "trashcan5" "say how outback man get lemonade"
alias "trashcan6" "say how to glow as healing scientist"
alias "trashcan7" "say where jogger get soda"
alias "trashcan8" "say how to institute automatic cannon as constructor"
alias "trashcan9" "say how shot lazer as hillbilly"
alias "trashcan10" "say how to launch ball as call center guy"
alias "trashcan11" "say can large ammunition bloke get fish and chips"
alias "trashcan12" "say how to signal friends with rubber suit guy"
alias "trashcan13" "say how speed man become super blur?"
alias "trashcan14" "say How inventor produce vending machine?"
alias "trashcan15" "say how engine man use calculator?"
alias "trashcan16" "say how to fly as captain america"
alias "trashcan17" "say where robot gun get bullet shoots"
alias "trashcan18" "say how do i shoot air as masked ignition man?!"
alias "trashcan19" "say how do make gun robots bigger as suspender dude"
alias "trashcan20" "say How can push explody train down choo choo tracks"
alias "trashcan21" "say How do make patriot fly"
alias "trashcan22" "say how does triathlon winner get home run"
alias "trashcan23" "say How do flame-man use signal"
alias "trashcan24" "say As the australian longshoot man how do I throw apple juice"
alias "trashcan25" "say How to reprogram cannons with french businessman!"
alias "trashcan26" "say how eyeball shoot eyeballs!!!"
alias "trashcan27" "say how make u.s. marine go air force?"
alias "trashcan28" "say How to make construction worker build gas pump?"
alias "trashcan29" "say when can carpenter put soda machine"
alias "trashcan30" "say How make Gun as Bob the Builder"
alias "trashcan31" "say go play with your building blocks"
alias "trashcan32" "say How do you push as the firebat"
alias "trashcan33" "say how warrior dig with shovel"
alias "trashcan34" "say what button to glow ghost buster?"
alias "trashcan35" "say how I go shiny as the dentist"
alias "trashcan36" "say how does fast boy throw ball"
alias "trashcan37" "say how fireman hammertime"
alias "trashcan38" "say how architect get more minerals"
alias "trashcan39" "say How do I make healing box?"
alias "trashcan40" "say how machine man get vespene gas"
alias "trashcan41" "say who can then the secret agent become the other team"
alias "trashcan42" "say why masked tuxedo man change color???"
alias "trashcan43" "say how do outback steakhouse guy do the telescope"
alias "trashcan44" "say how does french toast go seethrough"
alias "trashcan45" "say how masked artist make ice sculptures"
alias "trashcan46" "say How do I street fighter move as the fireman???????????"
alias "trashcan47" "say as the American guy, how do I use my jetpack"
alias "trashcan48" "say how to raise flag as patriot?!"
alias "trashcan49" "say How building healing bot as technician?"
alias "trashcan50" "say how fighter guy play trumpet"
alias "trashcan51" "say As science hillbilly, how do I deploy a tiny robo-cop?"
alias "trashcan52" "say why to build turret as construction worker!"
alias "trashcan53" "say How to shoot annoying baseball player?"
alias "trashcan54" "say How to pretend to die as french businessman"
alias "trashcan55" "say how ski mask guy listen to radio"
alias "trashcan56" "say how do boston scoundrel run fast?"
alias "trashcan57" "say how use chef knife as helmet child?"
alias "trashcan58" "say how do drinks machine as erection man?"
alias "trashcan59" "say how do i build disco platform as hank of the hill"
alias "trashcan60" "say how moorish legend do fast run"
alias "trashcan61" "say How u jump high as sports player"
alias "trashcan62" "say how to fly as sold man?"
alias "trashcan63" "say how speedy hooligan throw christmas ball?"
alias "trashcan64" "say how country singer play guitar"
alias "trashcan65" "say how white usain bolt sponsor pepsi"
alias "trashcan66" "say how coal miner play missile command with wrungler"
alias "trashcan67" "say where infantry fellow get gunboots?"
alias "trashcan68" "say how medicine man find supersaw?"
alias "trashcan69" "say how professorman inside eggshell?"
alias "trashcan70" "say how somali pirate get pegleg"
alias "trashcan71" "say how archer wanker shoot fire"
alias "trashcan72" "say how texas man get can opener hand"
alias "trashcan73" "say how astronaut suit eat candy"
alias "trashcan74" "say how albert einstein get lightning bolt hand"
alias "trashcan75" "say where vladimir putin find boxing glove"
alias "trashcan76" "say how russian president consume breadwich"
alias "trashcan77" "say how nasa spaceman do the fire jump?"
alias "trashcan78" "say how suit waiter download mixtape"
alias "trashcan79" "say explain how fighterman get a-bomb launcher?"
alias "trashcan80" "say pls say how does outback shooterman piss on wankers"
"""

with open(r"C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\cfg\user\test.cfg", "w") as f:
    f.write(script_txt)

