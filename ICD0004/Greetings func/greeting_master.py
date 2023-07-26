"""Implementation of Greeting"""
import re


def greet(name='my friend') -> str:
    """
    Create a greeting to named person.

    :param name: name of person to greet
    :return: greeting, that looks like "Hello, Name."
    """
    type_of_name = type(name)
    len_of_name = len(name)

    if type_of_name == str:
        return sub_greet_str(name, len_of_name)
    elif type_of_name == list:
        return sub_greet_list(name, len_of_name)
    else:
        return "Hello, unknown"


def sub_greet_str(name: str, len_of_name: int) -> str:
    """
    Sub function to simplify greet func
    Create a greeting to named person, if given a single name in string.

    :param name: name of person to greet
    :param len_of_name: length of name string, for handling names in 1 letter long
    :return: greeting, that looks like "Hello, Name." or "HELLO, NAME!"
    """
    if len(name) > 3 and name[0] == '"' and name[-1] == '"':
        return f"HELLO, {name[1:-1]}!" if name.isupper() else f"Hello, {name[1:-1]}."
    elif ", " in name:
        splited_names = name.split(", ")
        return sub_greet_list(splited_names, len(splited_names))
    elif re.match(r'\W+|^$', name):
        return "Hello, my friend."
    elif name.isupper() and len_of_name > 1:
        return f"HELLO, {name}!"
    else:
        return f"Hello, {name}."


def sub_greet_list(names: list, len_of_name: int) -> str:
    """
    Sub function to simplify greet func
    Create a greeting to named persons, if given a list of names.

    :param names: list of persons names to greet
    :param len_of_name: length of list
    :return: greeting, that looks like
    "Hello, Name1, Name2, and Name3." or "HELLO, NAME1, NAME2, AND NAME3!"
    """
    if len_of_name == 0:
        return "Hello, my friends."
    if len_of_name == 1:
        return sub_greet_str("".join(names), len_of_name)

    is_empty = 0
    lower_names = []
    upper_names = []

    for n in range(len_of_name):
        checking_name = names[n]
        if len(checking_name) > 3 and checking_name[0] == '"' and checking_name[-1] == '"':
            upper_names.append(checking_name[1:-1]) if checking_name.isupper() else lower_names.append(checking_name[1:-1])

        elif ", " in checking_name:
            splited_names = checking_name.split(", ")
            names = names[0:n] + splited_names + names[n + 1:]
            return greet(names)
        elif re.match(r'^\W+$|^$', checking_name):
            is_empty = 1
        elif checking_name.isupper() and len(checking_name) > 1:
            upper_names.append(checking_name)
        else:
            lower_names.append(checking_name)

    if len(names) == 2:
        return sub_greet_list_of_two(lower_names, upper_names, is_empty)

    lower_output, is_empty = sub_greet_list_of_lower_input(lower_names, is_empty)

    upper_output, is_empty = sub_greet_list_of_upper_input(upper_names, is_empty)

    if len(lower_output) == 0:
        return upper_output
    elif len(upper_output) == 0:
        return lower_output
    else:
        return lower_output + " AND " + upper_output


def sub_greet_list_of_lower_input(lower_names: list, is_empty: int) -> str:
    """
    Sub function to simplify greet func
    Create output for lower case names, if for greeting was given the list

    :param lower_names: list of persons names to greet
    :param is_empty: information, does list contains a empty strings for anonymous greeting
    :return: greeting, that looks like "HELLO, NAME1, NAME2, AND NAME3!"
    """
    lower_output = ""
    if len(lower_names) > 0:
        if len(lower_names) == 2 and is_empty != 1:
            lower_output = sub_greet_list_of_two(lower_names, [], is_empty)
        elif is_empty == 1:
            lower_output = "Hello, " + ", ".join(lower_names) + ", and my other friends."
            is_empty = 0
        elif len(lower_names) == 1 and is_empty != 1:
            lower_output = sub_greet_str("".join(lower_names), 10)
        else:
            lower_output = "Hello, " + ", ".join(lower_names[0:-1]) + f", and {lower_names[-1]}."
    return lower_output, is_empty


def sub_greet_list_of_upper_input(upper_names: list, is_empty: int) -> str:
    """
    Sub function to simplify greet func
    Create output for lower case names, if for greeting was given the list

    :param upper_names: list of persons names to greet
    :param is_empty: information, does list contains a empty strings for anonymous greeting
    :return: greeting, that looks like "HELLO, Name1, Name2, and Name3."
    """
    upper_output = ""
    if len(upper_names) > 0:
        if len(upper_names) == 2 and is_empty != 1:
            upper_output = sub_greet_list_of_two([], upper_names, is_empty)
        elif is_empty == 1 and len(lower_names) == 0:
            upper_output = "HELLO, " + ", ".join(upper_names) + ", AND MY OTHER FRIENDS!"
        elif len(upper_names) == 1 and is_empty != 1:
            upper_output = sub_greet_str("".join(upper_names), 10)
        else:
            upper_output = "HELLO, " + ", ".join(upper_names[0:-1]) + f", AND {upper_names[-1]}!"
    return upper_output, is_empty


def sub_greet_list_of_two(lower_names: list, upper_names: list, is_empty : int) -> str:
    """
    Sub function to simplify greet func when list have two names
    Create a greeting to two named persons.

    :param lower_names: list of two persons names to greet if they lower
    :param upper_names: list of two persons names to greet if they upper (shouted)
    :param is_empty: does in the list was empty or space string
    :return: greeting, that looks like
    "Hello, Name1 and Name2." or "HELLO, NAME1 AND NAME2!"
    """
    if is_empty == 1:
        return f"Hello, {lower_names[0]} and my other friend." if len(lower_names) > 0 \
            else f"Hello, my other friend. AND HELLO {upper_names[0]}"
    lower_output = "Hello, " + " and ".join(lower_names) + "."
    upper_output = "HELLO, " + " AND ".join(upper_names) + "!"
    if len(lower_output) < 9:
        return upper_output
    elif len(upper_output) < 9:
        return lower_output
    else:
        return lower_output + " AND " + upper_output
