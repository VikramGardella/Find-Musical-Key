full_octave = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
user_input = [1,1,1,1,1,1,0,1,0,0,1,1]

a_major = [1,0,1,0,1,1,0,1,0,1,0,1]
a_minor = [1,0,1,1,0,1,0,1,1,0,1,0]

def create_major(root):
    to_return = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(12):
        to_return[(i+root)%12] = a_major[i]

    return to_return

def create_minor(root):
    to_return = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(12):
        to_return[(i+root)%12] = a_minor[i]

    return to_return

def round_percent(dec):
    return ((int(dec*10000))/100)

def calc_sim(user, key):
    like = 0
    for i in range (12):
        #print('note: ' + full_octave[i] + ' inKey: ' + str(key[i]) + ' inUser: ' + str(user[i]))
        if(key[i] == user[i]):
            #print('match')
            like = like + 1

    return (round_percent(like/12.0))

def get_user_input():
    to_ret = []
    for i in range(len(full_octave)):
        user_string = input(full_octave[i] + '?\t').lower()
        while(user_string != 'yes' and user_string != 'no'):
            user_string = input(full_octave[i] + '?\t').lower()
        if(user_string == 'yes'):
            to_ret.append(1)
        else:
            to_ret.append(0)
    return to_ret
'''
Step 1

Manually make 12-element lists for all Major and Minor keys 
that contain boolean values (integers: 0 or 1) based on whether the 
note at the corresponding index of "full_octave" is, in fact, a note 
found in the key at-hand.
'''


#Major Keys:

a_major = create_major(0)
as_major = create_major(1)
b_major = create_major(2)
c_major = create_major(3)
cs_major = create_major(4)
d_major = create_major(5)
ds_major = create_major(6)
e_major = create_major(7)
f_major = create_major(8)
fs_major = create_major(9)
g_major = create_major(10)
gs_major = create_major(11)


#Minor Keys:

a_minor = create_minor(0)
as_minor = create_minor(1)
b_minor = create_minor(2)
c_minor = create_minor(3)
cs_minor = create_minor(4)
d_minor = create_minor(5)
ds_minor = create_minor(6)
e_minor = create_minor(7)
f_minor = create_minor(8)
fs_minor = create_minor(9)
g_minor = create_minor(10)
gs_minor = create_minor(11)

print('\nBelow, specify which notes are in your piece by typing \'yes\' or \'no\':\n\n')

user_input = get_user_input()

print('\n\nMatches by key:\n')
print('A Major: ' + str(calc_sim(user_input, a_major)) + "%")
print('A Minor: ' + str(calc_sim(user_input, a_minor)) + "%")
print('A# Major: ' + str(calc_sim(user_input, as_major)) + "%")
print('A# Minor: ' + str(calc_sim(user_input, as_minor)) + "%")
print('B Major: ' + str(calc_sim(user_input, b_major)) + "%")
print('B Minor: ' + str(calc_sim(user_input, b_minor)) + "%")
print('C Major: ' + str(calc_sim(user_input, c_major)) + "%")
print('C Minor: ' + str(calc_sim(user_input, c_minor)) + "%")
print('C# Major: ' + str(calc_sim(user_input, cs_major)) + "%")
print('C# Minor: ' + str(calc_sim(user_input, cs_minor)) + "%")
print('D Major: ' + str(calc_sim(user_input, d_major)) + "%")
print('D Minor: ' + str(calc_sim(user_input, d_minor)) + "%")
print('D# Major: ' + str(calc_sim(user_input, ds_major)) + "%")
print('D# Minor: ' + str(calc_sim(user_input, ds_minor)) + "%")
print('E Major: ' + str(calc_sim(user_input, e_major)) + "%")
print('E Minor: ' + str(calc_sim(user_input, e_minor)) + "%")
print('F Major: ' + str(calc_sim(user_input, f_major)) + "%")
print('F Minor: ' + str(calc_sim(user_input, f_minor)) + "%")
print('F# Major: ' + str(calc_sim(user_input, fs_major)) + "%")
print('F# Minor: ' + str(calc_sim(user_input, fs_minor)) + "%")
print('G Major: ' + str(calc_sim(user_input, g_major)) + "%")
print('G Minor: ' + str(calc_sim(user_input, g_minor)) + "%")
print('G# Major: ' + str(calc_sim(user_input, gs_major)) + "%")
print('G# Minor: ' + str(calc_sim(user_input, gs_minor)) + "%")


'''
Step 2

Make the User Interface and assign variable names/identifiers to be 
referenced later in the Back-End.
'''


'''
Step 3

Take user input via toggle buttons for virtual fretboard
'''


'''
Step 4

Determine notes of those frets.
'''


'''
Step 5

Limit it down to one 12 semitone octave, resulting in 12-element 
list of boolean values. It will be best to use 0's for false and 1's 
for true (ie. "note was in user's guitar composition AND also the key 
being cross-referenced to produce a percentage/decimal value 
representing match accuracy).
'''
