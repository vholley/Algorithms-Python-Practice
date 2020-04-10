'''
propositional_logic.py

This program has functions for evaluating logical propositions and producing a
truth table with given propositions.

'''

import itertools
from copy import copy

'''
format_prop(prop)

Returns the proposition, formatted in string form.

Parameters:
prop (list): proposition in nested list form

Returns:
string: 'formatted_prop' in string form
'''


def format_prop(prop):
    # BASE CASE: #####################################
    # If prop only contains one atomic proposition, return the proposition
    if len(prop) == 1:
        formatted_prop = '(' + prop[0][0] + ')'
        return formatted_prop

    # If prop contains nested elements, resolve the nested elements starting
    # with the innermost compound proposition

    # In Python, nested functions can mutate global variables
    # Create a copy of prop which can be mutable, mut_prop
    mut_prop = copy(prop)

    # If the third element is a compound proposition, resolve that proposition
    if len(mut_prop) == 3:
        if len(mut_prop[2]) > 1:
            mut_prop[2] = [format_prop(mut_prop[2])]

    # If the second element is a compound proposition, resolve that proposition
    if len(mut_prop) <= 3:
        if len(mut_prop[1]) > 1:
            mut_prop[1] = [format_prop(mut_prop[1])]
    ##################################################

    # UNARY OPERATOR (not): ##########################
    if len(mut_prop) == 2:
        # The first element is a logical connective, connect
        connect = mut_prop[0]

        # The second element is an atomic proposition, atomic
        atomic = mut_prop[1][0]

        # The only valid unary connective is 'not'
        if connect == 'not':
            formatted_prop = '(' + connect + ' ' + atomic + ')'
            return formatted_prop

        # If the unary operation is not 'not,' raise an error
        else:
            raise ValueError('Unary proposition is not "not."')

    ##################################################

    # BINARY OPERATOR (and, or, if, iff, xor): #######
    elif len(mut_prop) == 3:
        # The first element is a logical connective, connect
        connect = mut_prop[0]

        # The remaining elements are atomic propositions, atomic1 atomic2
        atomic1 = mut_prop[1][0]
        atomic2 = mut_prop[2][0]

        if connect not in ('if', 'iff', 'or', 'and', 'xor'):
            raise ValueError('Binary proposition does not have valid connectives.')

        # Change 'if' and 'iff' representation
        if connect == 'if':
            connect = '->'
        elif connect == 'iff':
            connect = '<->'

        # Format left and right sides of a binary operation
        left_prop = '(' + atomic1 + ' '
        right_prop = ' ' + atomic2 + ')'

        formatted_prop = left_prop + connect + right_prop
        return formatted_prop
    ####################################################

    # INVALID LENGTH ####################################
    # If the length of prop is not 2 or 3, raise an error
    else:
        raise ValueError('Proposition incorrect length.')
    #####################################################


'''
eval_prop(prop, values)

Returns the evaluation (True or False) as an int (1 or 0) of the proposition,
given a proposition in list form and a list of values for each atomic variable.

Parameters:
prop (list): proposition in nested list form.
values (list): list of integers, either 0 or 1 indicating False or True for
each atomic variable in the proposition.

Returns:
int: 0 for False, 1 for True
'''


def eval_prop(prop, values):
    # BASE CASE: #####################################
    # If prop only contains one atomic proposition, return values[0]
    if len(prop) == 1:
        return int(values[0])

    # If prop contains nested elements, resolve the nested elements starting
    # with the innermost compound proposition

    # In Python, nested functions can mutate global variables
    # Create a copy of prop which can be mutable, mut_prop
    mut_prop = copy(prop)

    # If the third element is a compound proposition, resolve that proposition
    if len(mut_prop) == 3:
        if len(mut_prop[2]) > 1:
            mut_prop[2] = [eval_prop(mut_prop[2], values)]

    # If the second element is a compound proposition, resolve that proposition
    if len(mut_prop) <= 3:
        if len(mut_prop[1]) > 1:
            mut_prop[1] = [eval_prop(mut_prop[1], values)]
    ##################################################

    # UNARY OPERATOR (not): ##########################
    if len(mut_prop) == 2:
        # The first element is a logical connective, connect
        connect = mut_prop[0]

        # The second element is an atomic proposition, atomic
        # The value of atomic comes from str('p(index of values + 1)')
        # (i.e. 'p1' converts to values[0])
        atomic = values[int(mut_prop[1][0][1]) - 1]
        if connect == 'not':
            return int(not atomic)
        else:
            raise ValueError('Unary proposition is not "not."')
    ##################################################

    # BINARY OPERATOR (and, or, if, iff, xor): #######
    elif 3 == len(mut_prop):
        # The first element is a logical connective, connect
        connect = mut_prop[0]

        # The remaining elements are atomic propositions, atomic1 atomic2
        atomic1 = mut_prop[1][0]
        atomic2 = mut_prop[2][0]

        if connect not in ('if', 'iff', 'or', 'and', 'xor'):
            raise ValueError('Binary proposition does not have valid connectives.')

        # The values of left and right come from str('p(index of values + 1)')
        # (i.e. 'p1' converts to values[0])
        # If atomic is a string, change it to the corresponding value
        if isinstance(atomic1, str):
            left = values[int(atomic1[1]) - 1]
        else:
            left = atomic1

        if isinstance(atomic2, str):
            right = values[int(atomic2[1]) - 1]
        else:
            right = atomic2

        # the line here is an example. fill in the rest.
        if connect == 'and':
            return int(left and right)
        elif connect == 'or':
            return int(left or right)
        elif connect == 'xor':
            return int(left ^ right)
        elif connect == 'if':
            return int((not left) or right)
        else:
            return int((left and right) or ((not left) and (not right)))

    # INVALID LENGTH ####################################
    else:
        raise ValueError('Proposition incorrect length.')
    #####################################################


'''
print_table(prop, n_var)

Prints a truth table given a proposition in nested list form and
an integer defining the number of atomic variables.

Parameters:
prop (list): proposition in nested list form.
n_var (int): the number of atomic variables in prop.

Returns:
None
'''


def print_table(prop, n_var):

    # Create a list containing each row of the table, table_list
    table_list = []

    # Create a list containing information for the rows, row_list
    row_list = []

    # Append elements for each atomic proposition
    for i in range(n_var + 1):
        row_list.append('| p' + str(i))

    # Append the last column
    row_list.append('| ' + format_prop(prop))

    # Combine the strings to create the row, row_str
    row_str = ' '.join(row_list)

    # Append the row_str to table_list
    table_list.append(row_str)

    # Create a list of every permutation of 2^n TRUE and FALSE values, p_values
    p_values = list(itertools.product([0, 1], repeat=n_var))

    # For each permutation of TRUE and FALSE values, create a new row
    for tup in p_values:
        row_list = []
        values = list(tup)

        # Append each value to row_list
        for element in values:
            row_list.append('| ' + str(element))

        # Calculate the proposition with values and append to row_list
        prop_result = str(eval_prop(prop, values))
        row_list.append('| ' + prop_result)

        # Combine the strings to create the rows, row_str
        row_str = ' '.join(row_list)

        # Append the row_str to table_list
        table_list.append(row_str)

    # Print the table from table list
    for row in table_list:
        print(row)


if __name__ == '__main__':

    values = [1]
    prop = ['not', ['p1']]
    ps_str = ' '.join('p{}={}'.format(i + 1, v) for i, v in enumerate(values))
    print('Evaluating proposition p =', format_prop(prop))
    prop_val = eval_prop(prop, values)
    print('over', ps_str, ':', prop_val)

    print()
    values = [1, 1]
    prop = ['and', ['p1'], ['p2']]
    ps_str = ' '.join('p{}={}'.format(i + 1, v) for i, v in enumerate(values))
    print('Evaluating proposition p =', format_prop(prop))
    prop_val = eval_prop(prop, values)
    print('over', ps_str, ':', prop_val)

    print()
    values = [1, 0]
    prop = ['iff', ['p1'], ['p2']]
    ps_str = ' '.join('p{}={}'.format(i + 1, v) for i, v in enumerate(values))
    print('Evaluating proposition p =', format_prop(prop))
    prop_val = eval_prop(prop, values)
    print('over', ps_str, ':', prop_val)

    print()
    values = [1, 1, 0]
    prop = ['if', ['and', ['p1'], ['not', ['p2']]], ['p3']]
    ps_str = ' '.join('p{}={}'.format(i + 1, v) for i, v in enumerate(values))
    prop_str = format_prop(prop)
    print('Evaluating proposition p =', prop_str)
    prop_val = eval_prop(prop, values)
    print('over', ps_str, ':', prop_val)

    print()
    values = [1, 0, 1]
    prop = ['iff', ['p1'], ['or', ['p2'], ['not', ['p3']]]]
    ps_str = ' '.join('p{}={}'.format(i + 1, v) for i, v in enumerate(values))
    print('Evaluating proposition p =', format_prop(prop))
    prop_val = eval_prop(prop, values)
    print('over', ps_str, ':', prop_val)

    print('---------------------------------------------------')
    print()
    print('Table:')
    print_table(['if', ['and', ['p1'], ['not', ['p2']]], ['p3']], 3)
