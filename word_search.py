# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Ralph Maamari
# MarkUs Login: maamarir
#

PUZZLE1 = '''
glkutqyu
onnkjoaq
uaacdcne
gidiaayu
urznnpaf
ebnnairb
xkybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyotiutuvpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.
    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    >>> lr_occurrences(PUZZLE1, 'brian')
    0
    >>> lr_occurrences(PUZZLE1, 'nick')
    0
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.
    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    >>> total_occurrences('cow\ncow', 'cow')
    2
    >>> total_occurrences('ow\nwo', 'ow')
    4
    >>> total_occurrences(PUZZLE1, 'brian')
    2
    >>> total_occurrences(PUZZLE2, 'brian')
    3
    '''
    # Count the amount of left to right occurances
    total_left_to_right = lr_occurrences(puzzle, word)
    # Rotate the puzzle and save its new rotation state
    puzzle = rotate_puzzle(puzzle)  # 90 degrees left
    # count the amount of top to bottom occurances
    total_top_to_bottom = lr_occurrences(puzzle, word)
    # Rotate the puzzle and save its new rotation state
    puzzle = rotate_puzzle(puzzle)  # 180 Degrees left
    # Count the amount of right to left occurances
    total_right_to_left = lr_occurrences(puzzle, word)
    # Rotate the puzzle and save its new rotation state
    puzzle = rotate_puzzle(puzzle)  # 270 Degrees left
    # Count the amount of bottom to top occurances
    total_bottom_to_top = lr_occurrences(puzzle, word)
    # Rotate the puzzle and save its new rotation state
    puzzle = rotate_puzzle(puzzle)  # Original State
    return(total_left_to_right + total_top_to_bottom +
           total_right_to_left + total_bottom_to_top)


# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    ''' (str, str) -> bool
    Return a true boolean result based on the fact the word
    can be found in the puzzle from left to right or right to left.
    >>> in_puzzle_horizontal('hcat\nataa', 'ha')
    False
    >>> in_puzzle_horizontal('xcat\ncataa', 'take')
    False
    >>> in_puzzle_horizontal('xcat\ncataa', 'cat')
    True
    >>> in_puzzle_horizontal('xaxy\nyaaa', 'xy')
    True
    >>> in_puzzle_horizontal(PUZZLE1, 'brian')
    True
    >>> in_puzzle_horizontal(PUZZLE2, 'brian')
    False
    '''
    # Count the amount of left to right occurances
    total_left_to_right = lr_occurrences(puzzle, word)
    # Rotate the puzzle twice
    puzzle = rotate_puzzle(puzzle)  # 90 Degrees left
    puzzle = rotate_puzzle(puzzle)  # 180 Degrees left
    # Count the amount of right to left occurances
    total_right_to_left = lr_occurrences(puzzle, word)
    return(total_left_to_right >= 1 or total_right_to_left >= 1)


# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> bool
    Return a true boolean result based on the fact the word
    can be found in the puzzle from top to bottom or bottom to top.
    >>> in_puzzle_vertical('hcat\nataa', 'ha')
    True
    >>> in_puzzle_vertical('xcat\ncataa', 'take')
    False
    >>> in_puzzle_vertical('xcat\ncataa', 'cat')
    False
    >>> in_puzzle_vertical('xaxy\nyaaa', 'xy')
    True
    >>> in_puzzle_vertical(PUZZLE1, 'brian')
    True
    >>> in_puzzle_vertical(PUZZLE2, 'brian')
    True
    '''
    # Count the amount of top to bottom occurances
    puzzle = rotate_puzzle(puzzle)  # 90 Degrees left
    total_top_to_bottom = lr_occurrences(puzzle, word)
    # Rotate the puzzle twice
    puzzle = rotate_puzzle(puzzle)  # 180 Degrees left
    puzzle = rotate_puzzle(puzzle)  # 270 Degrees left
    # Count the amount of bottom to top occurances
    total_bottom_to_top = lr_occurrences(puzzle, word)
    return(total_bottom_to_top >= 1 or total_top_to_bottom >= 1)

# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    '''(str, str) -> bool
    Return a true boolean result based on the fact the word
    can be found anywhere inside the given puzzle.
    >>> in_puzzle('xcat\ncataa', 'take')
    False
    >>> in_puzzle('hcat\nataa', 'ha')
    True
    >>> in_puzzle('xcat\ncataa', 'cat')
    True
    >>> in_puzzle('xaxy\nyaaa', 'xy')
    True
    >>> in_puzzle(PUZZLE1, 'brian')
    True
    >>> in_puzzle(PUZZLE2, 'brian')
    True
    '''
    return((in_puzzle_vertical(puzzle, word)) or
           (in_puzzle_horizontal(puzzle, word)))

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    '''(str, str) -> bool
    Return a true boolean result based on the fact the word
    can be found in the puzzle from only one dimension (Either only the
    vertical dimensions or only the horizontal dimension) or if
    the word is not in the puzzle.
    >>> in_exactly_one_dimension('xcat\ncataa', 'take')
    True
    >>> in_exactly_one_dimension('hcat\nataa', 'ha')
    True
    >>> in_exactly_one_dimension('xcat\ncataa', 'cat')
    True
    >>> in_exactly_one_dimension('xaxy\nyaaa', 'xy')
    False
    >>> in_exactly_one_dimension(PUZZLE1, 'brian')
    False
    >>> in_exactly_one_dimension(PUZZLE2, 'brian')
    True
    '''
    return (not(in_puzzle(puzzle, word)) or
            not((in_puzzle_horizontal(puzzle, word)) and
                (in_puzzle_vertical(puzzle, word))))


# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    '''(str, str) -> bool
    Return a true boolean result based on the fact the word
    can be found only in the horizontal dimension (Left to Right or
    Right to Left) or if the word is not in the puzzle.
    >>> all_horizontal('xcat\ncataa', 'take')
    True
    >>> all_horizontal('hcat\nataa', 'ha')
    False
    >>> all_horizontal('xcat\ncataa', 'cat')
    True
    >>> all_horizontal('xaxy\nyaaa', 'xy')
    False
    >>> all_horizontal(PUZZLE1, 'brian')
    False
    >>> all_horizontal(PUZZLE2, 'brian')
    False
    '''
    return(not(in_puzzle(puzzle, word)) or
           ((in_puzzle_horizontal(puzzle, word)) and
           not(in_puzzle_vertical(puzzle, word))))

# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    '''(str, str) -> bool
    Return a true boolean result based on the fact the word
    has only one vertical occurance and no other occurances in the puzzle or
    if it is not in the puzzle.
    >>> at_most_one_vertical('xcat\ncataa', 'take')
    True
    >>> at_most_one_vertical('hcat\nataa', 'ha')
    True
    >>> at_most_one_vertical('xcat\ncataa', 'cat')
    False
    >>> at_most_one_vertical('xaxy\nyaaa', 'xy')
    False
    >>> at_most_one_vertical('at\nta', 'at')
    False
    >>> at_most_one_vertical(PUZZLE1, 'brian')
    False
    >>> at_most_one_vertical(PUZZLE2, 'brian')
    False
    '''
    return((in_puzzle_vertical(puzzle, word) == 1) and
           (total_occurrences(puzzle, word) == 1) or
           (total_occurrences(puzzle, word) == 0))


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''
    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.
    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    print(lr_occurrences(puzzle, name))
    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    # Rotates the puzzle 90 degress left and save the rotation state
    puzzle = rotate_puzzle(puzzle)  # 90 degrees left
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print(lr_occurrences(puzzle, name))
    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    # Rotates the puzzle 90 degress left and save the rotation state
    puzzle = rotate_puzzle(puzzle)  # 180 Degrees left
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print(lr_occurrences(puzzle, name))
    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    puzzle = rotate_puzzle(puzzle)  # 270 Degrees left
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(puzzle, name))
    # Return puzzle back to original rotation state
    puzzle = rotate_puzzle(puzzle)  # Original State
    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    print (total_occurrences(puzzle, name))
    # Add only one line below.
    # Your code should print a single number, nothing else.
    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print(in_puzzle_horizontal(puzzle, name))

do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')
# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'nick')
# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, 'nick'))
# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'anya'.
# Add only one line below. Your code should print only True or False.
# print(in_exactly_one_dimension(PUZZLE1, 'nick'))
print(in_puzzle(PUZZLE2, 'anya'))
