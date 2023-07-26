"""Tests for TDD Cata"""
import pytest
from src.greeting_master import greet

# Requirement 1
# Write a method greet(name) that interpolates name in a simple greeting.
# For example, when name is "Bob", the method should return a string "Hello, Bob.".


def test_basic_name_to_single_lower_greeting():
    """Test return of basic single names."""
    assert greet("Bob") == "Hello, Bob."
    assert greet("Alice") == "Hello, Alice."


def test_short_name_to_single_lower_greeting():
    """Test return of very short single names."""
    assert greet("A") == "Hello, A."
    assert greet("Q") == "Hello, Q."


def test_long_name_to_single_lower_greeting():
    """Test return of very long single names."""
    assert greet("Zeratustraeqandobralia") == "Hello, Zeratustraeqandobralia."
    assert greet("Eyafjajacalaultul") == "Hello, Eyafjajacalaultul."


def test_person_with_much_names_to_single_lower_greeting():
    """Test return of person with multiple names."""
    assert greet("Melica Amorella Quenn De Casto La Antonia Fon De Debua") == \
           "Hello, Melica Amorella Quenn De Casto La Antonia Fon De Debua."


# Requirement 2
# Handle empty or missing input by introducing a stand-in.
# For example, when name is null, then the method should return the string "Hello, my friend.".


def test_empty_string_to_single_anonymous_lower_greeting():
    """Test return of default greeting if given empty string."""
    assert greet("") == "Hello, my friend."


def test_space_string_to_single_anonymous_lower_greeting():
    """Test return of default greeting if given string with spaces."""
    assert greet(" ") == "Hello, my friend."
    assert greet("           ") == "Hello, my friend."


def test_request_without_params_to_single_anonymous_lower_greeting():
    """Test return of default greeting if no value is given."""
    assert greet() == "Hello, my friend."


# Requirement 3
# Handle shouting. When name is all uppercase, then the method should shout back to the user.
# For example, when name is "JERRY" then the method should return the string "HELLO, JERRY!".


def test_shout_basic_name_to_single_upper_greeting():
    """Test shouting return of basic single names."""
    assert greet("BOB") == "HELLO, BOB!"
    assert greet("ALICE") == "HELLO, ALICE!"


def test_shout_long_name_single_to_upper_greeting():
    """Test shouting return of very long single names."""
    assert greet("ZERATUSTRALOLROFLAN") == "HELLO, ZERATUSTRALOLROFLAN!"
    assert greet("EYAJAFJAJAJACUDL") == "HELLO, EYAJAFJAJAJACUDL!"


def test_person_with_much_shout_names_to_single_upper_greeting():
    """Test shouting return person with multiple names.."""
    assert greet("ELIORA TEN DENIS LA CICTORELLA DE CASPORRO SINTO CIRICLLA FON AR BRUE") == \
           "HELLO, ELIORA TEN DENIS LA CICTORELLA DE CASPORRO SINTO CIRICLLA FON AR BRUE!"


# Requirement 4
# Handle two names of input. When name is an array of two names (or, in languages that support, varargs or a splat),
# then both names should be printed.
# For example, when name is ["Jill", "Jane"], then the method should return the string "Hello, Jill and Jane.".


def test_list_of_two_basic_names_to_double_name_lower_greeting():
    """Test return of basic single names."""
    assert greet(["Bob", "Alice"]) == "Hello, Bob and Alice."


def test_list_of_two_short_names_to_double_name_lower_greeting():
    """Test return of two very short single names."""
    assert greet(["A", "D"]) == "Hello, A and D."


def test_list_of_two_long_names_to_double_name_lower_greeting():
    """Test return of two very long single names."""
    assert greet(["Zeratustraeqandobralia", "Eyafjajacalaultul"]) == \
           "Hello, Zeratustraeqandobralia and Eyafjajacalaultul."


def test_list_of_two_persons_with_much_names_to_double_name_lower_greeting():
    """Test return of person with multiple names."""
    assert greet(["Melica Amorella Quenn De Casto La Antonia Fon De Debua",
                  "Eliza Fiona Atneto Ja La Fall Cailtyroa In Despasito"]) == \
           "Hello, Melica Amorella Quenn De Casto La Antonia Fon De Debua and " \
           "Eliza Fiona Atneto Ja La Fall Cailtyroa In Despasito."


def test_list_of_two_with_empty_name_to_single_lower_and_anonymous_greeting():
    """Test return of name and empty string."""
    assert greet(["Alice", ""]) == "Hello, Alice and my other friend."
    assert greet(["", "Bob"]) == "Hello, Bob and my other friend."


# Requirement 5
# Handle an arbitrary number of names as input. When name represents more than two names,
# separate them with commas and close with an Oxford comma and "and".
# For example, when name is ["Amy", "Brian", "Charlotte"], then the method should
# return the string "Hello, Amy, Brian, and Charlotte."


def test_greeting_when_empty_list_to_anonymous_group_greeting():
    """Test return of basic single names."""
    assert greet([]) == "Hello, my friends."


def test_list_of_three_to_three_lower_names_lower_greeting():
    """Test return of three basic single names."""
    assert greet(["Jackier", "Geralt", "Yennifer"]) == "Hello, Jackier, Geralt, and Yennifer."


def test_list_of_ten_to_ten_lower_names_greeting():
    """Test return of ten basic single names."""
    assert greet(["Jackier", "Geralt", "Yennifer", "Golum", "Bilbo",
                  "Twoflower", "Rinswind", "Borh", "Gendalf", "Sauron"]) \
           == "Hello, Jackier, Geralt, Yennifer, Golum, Bilbo, " \
              "Twoflower, Rinswind, Borh, Gendalf, and Sauron."


def test_list_of_five_with_empty_to_four_lower_names_with_anonymous_group_greeting():
    """Test return of four basic single names and empty string."""
    assert greet(["Jackier", "Geralt", "", "Yennifer", "Nenneke"]) == \
           "Hello, Jackier, Geralt, Yennifer, Nenneke, and my other friends."


def test_list_of_five_with_spaces_to_four_lower_names_with_anonymous_group_greeting():
    """Test return of four basic single names and space string."""
    assert greet(["Jackier", "Geralt", "   ", "Yennifer", "Nenneke"]) == \
           "Hello, Jackier, Geralt, Yennifer, Nenneke, and my other friends."


def test_list_of_seven_with_multiple_spaces_to_lower_names_with_anonymous_group_greeting():
    """Test return of four basic single names and space string."""
    assert greet(["Jackier", "  ", "   ", "Yennifer", "", "Qugogoda", "Asgradet"]) == \
           "Hello, Jackier, Yennifer, Qugogoda, Asgradet, and my other friends."


def test_list_of_two_and_person_with_much_names_to_lower_names_greeting():
    """Test return of three basic single and multi names."""
    assert greet(["Jackier", "Geralt", "Cahir Mawr Dyffryn aep Ceallach"]) == \
           "Hello, Jackier, Geralt, and Cahir Mawr Dyffryn aep Ceallach."


def test_list_of_three_with_short_name_to_lower_names_greeting():
    """Test return of three basic and short single names."""
    assert greet(["B", "A", "Heroky"]) == \
           "Hello, B, A, and Heroky."


# Requirement 6
# Allow mixing of normal and shouted names by separating the response into two greetings.
# For example, when name is ["Amy", "BRIAN", "Charlotte"], then the method should return
# the string "Hello, Amy and Charlotte. AND HELLO, BRIAN!".

def test_list_of_two_shouting_and_basic_names_to_greeting_with_lower_names_and_greeting_with_upper_names():
    """Test return of one basic and one shout names."""
    assert greet(["Elisa", "MAXIM"]) == "Hello, Elisa. AND HELLO, MAXIM!"


def test_list_of_three_shouting_and_basic_names_to_greeting_with_lower_names_and_greeting_with_upper_names():
    """Test return pf two basic and one shout names."""
    assert greet(["Mark", "MARIA", "Milena"]) ==\
           "Hello, Mark and Milena. AND HELLO, MARIA!"


def test_list_of_five_shouting_and_basic_names_to_greeting_with_lower_names_and_greeting_with_upper_names():
    """Test return of few basic and few shout names."""
    assert greet(["SASHA", "Luisa", "Mihhail", "MAREK", "Andrea"]) ==\
           "Hello, Luisa, Mihhail, and Andrea. AND HELLO, SASHA AND MAREK!"
    assert greet(["SASHA", "Luisa", "Mihhail", "MAREK", "ANDREA"]) ==\
           "Hello, Luisa and Mihhail. AND HELLO, SASHA, MAREK, AND ANDREA!"


def test_list_of_five_shouting_and_short_and_basic_names_to_greeting_with_lower_names_and_greeting_with_upper_names():
    """Test return of basic and short and shout names."""
    assert greet(["K", "ILONA", "Denis", "Egor", "CARNELLA"]) ==\
           "Hello, K, Denis, and Egor. AND HELLO, ILONA AND CARNELLA!"


def test_list_of_five_shouting_and_long_and_basic_names_to_greeting_with_lower_names_and_greeting_with_upper_names():
    """Test return of basic and long and shout names."""
    assert greet(["Eyfjajalaculd", "ELISANDRELLA", "Archel", "RACHEL", "DEAGENDRAFAJARAN"]) == \
           "Hello, Eyfjajalaculd and Archel. AND HELLO, ELISANDRELLA, RACHEL, AND DEAGENDRAFAJARAN!"


def test_list_of_five_shouting_and_empty_basic_names_to_greeting_with_lower_names_and_greeting_with_upper_names_and_anonymous_greeting():
    """Test return of basic and shout names with empty name"""
    assert greet(["Germiona", "Harry", "RON", "ALBUS", ""]) == \
           "Hello, Germiona, Harry, and my other friends. AND HELLO, RON AND ALBUS!"


def test_list_of_five_shouting_and_space_basic_names_to_greeting_with_lower_names_and_greeting_with_upper_names_and_anonymous_greeting():
    """Test return of basic and shout names with space name"""
    assert greet(["Germiona", "Harry", "RON", "ALBUS", "      "]) == \
           "Hello, Germiona, Harry, and my other friends. AND HELLO, RON AND ALBUS!"


def test_list_of_five_only_shouting_names_to_greeting_with_upper_names():
    """Test return of only shout names."""
    assert greet(["FARAMIR", "BOROMIR", "SAURON", "GENDALF", "RADAGAST"]) == \
           "HELLO, FARAMIR, BOROMIR, SAURON, GENDALF, AND RADAGAST!"


def test_list_of_three_shout_and_basic_and_empty_names_to_greeting_with_lower_names_and_greeting_with_upper_names_and_anonymous_greeting():
    """Test return of one shout, one basic and one empty names."""
    assert greet(["FARAMIR", "Boromir", ""]) == \
           "Hello, Boromir, and my other friends. AND HELLO, FARAMIR!"


# Requirement 7
# If any entries in name are a string containing a comma, split it as its own input.
# For example, when name is ["Bob", "Charlie, Dianne"], then the method should return the
# string "Hello, Bob, Charlie, and Dianne.".


def test_list_of_two_with_comma_string_to_greeting_with_three_lower_names():
    """Test return of basic name and string with two names."""
    assert greet(["Bob", "Charlie, Dianne"]) == \
           "Hello, Bob, Charlie, and Dianne."


def test_list_of_three_with_comma_string_to_greeting_with_four_lower_names():
    """Test return of two basic names and string with two names."""
    assert greet(["Bob", "Charlie, Dianne", "Elisa"]) == \
           "Hello, Bob, Charlie, Dianne, and Elisa."


def test_list_of_three_with_two_comma_string_to_greeting_with_five_lower_names():
    """Test return of basic name and two string with two names."""
    assert greet(["Bob", "Charlie, Dianne", "Elisa, Eleonora"]) == \
           "Hello, Bob, Charlie, Dianne, Elisa, and Eleonora."


def test_list_of_three_with_comma_string_and_shout_to_greeting_with_lower_names_and_shout_name():
    """Test return of basic name, shout name and string with two names."""
    assert greet(["Bob", "Charlie, Dianne", "ELISA"]) == \
           "Hello, Bob, Charlie, and Dianne. AND HELLO, ELISA!"


def test_list_of_three_with_comma_string_and_empty_to_greeting_with_lower_names_and_anonymous():
    """Test return of basic name, empty name and string with two names."""
    assert greet(["Bob", "Charlie, Dianne", ""]) == \
           "Hello, Bob, Charlie, Dianne, and my other friends."


def test_list_of_three_with_shout_comma_string_to_greeting_with_lower_names_and_upper_names_and_anonymous():
    """Test return of two basic names and string with two shout names."""
    assert greet(["Bob", "CHARLIE, DIANNE", "Elina"]) == \
           "Hello, Bob and Elina. AND HELLO, CHARLIE AND DIANNE!"


def test_list_of_five_with_shout_comma_string_and_basic_comma_string_to_greeting_with_lower_names_and_upper_names():
    """Test return of basic and shout names with strings of two basic and two shout names."""
    assert greet(["Bob", "CHARLIE, DIANNE", "Perikl, Diamed", "MARGO", "Elina"]) == \
           "Hello, Bob, Perikl, Diamed, and Elina. AND HELLO, CHARLIE, DIANNE, AND MARGO!"


def test_list_of_only_one_comma_string_to_greeting_with_two_lower_names():
    """Test return of string with two basic names."""
    assert greet(["Charlie, Dianne"]) == \
           "Hello, Charlie and Dianne."


def test_list_of_three_comma_string_to_greeting_with_lower_names_and_upper_names():
    """Test return of strings with two shout names and two basic names."""
    assert greet(["Charlie, Dianne", "ELIANDR, FELICITA", "Debita, Lund"]) == \
           "Hello, Charlie, Dianne, Debita, and Lund. AND HELLO, ELIANDR AND FELICITA!"


def test_list_of_only_one_comma_string_with_many_basic_names_to_greeting_with_five_lower_names():
    """Test return of string with multiple basic names."""
    assert greet(["Charlie, Dianne, Rosalin, Fionna, Eles"]) == \
           "Hello, Charlie, Dianne, Rosalin, Fionna, and Eles."


def test_list_of_only_one_comma_string_with_many_basic_and_shout_names_to_greeting_with_lower_names_and_upper_names():
    """Test return of string with multiple basic and shout names."""
    assert greet(["NANSY, Charlie, Dianne, ALISA, Rosalin, Fionna, NASTYA, GERRA, Eles"]) == \
           "Hello, Charlie, Dianne, Rosalin, Fionna, and Eles. AND HELLO, NANSY, ALISA, NASTYA, AND GERRA!"


# Requirement 8
# Allow the input to escape intentional commas introduced by Requirement 7. These can
# be escaped in the same manner that CSV is, with double quotes surrounding the entry.
# For example, when name is ["Bob", "\"Charlie, Dianne\""], then the method should return
# the string "Hello, Bob and Charlie, Dianne.".


def test_list_of_basic_names_with_escaped_comma_string_to_greeting_with_lower_name_and_escaped_lower_string():
    """Test return of basic name and escaped comma string with multiple names."""
    assert greet(["Bob", "\"Charlie, Dianne\""]) == \
           "Hello, Bob and Charlie, Dianne."


def test_list_of_few_basic_names_with_escaped_comma_string_to_greeting_with_lower_names_and_escaped_lower_string():
    """Test return of few basic name and escaped comma string with multiple names."""
    assert greet(["Bob", "\"Charlie, Dianne\"", "Rosalin"]) == \
           "Hello, Bob, Charlie, Dianne, and Rosalin."


def test_only_escaped_comma_string_to_greeting_with_escaped_lower_string():
    """Test return of escaped comma string with multiple names."""
    assert greet(["\"Charlie, Dianne\""]) == \
           "Hello, Charlie, Dianne."


def test_only_shout_escaped_comma_string_to_greeting_with_escaped_shout_string():
    """Test return of shout escaped comma string with multiple names."""
    assert greet(["\"CHARLIE, DIANNE\""]) == \
           "HELLO, CHARLIE, DIANNE!"


def test_list_of_basic_and_shout_names_with_escaped_comma_string_to_greeting_with_escaped_lower_string_and_lower_name_and_greeting_with_shout_name():
    """Test return of shout name and escaped comma string with multiple names."""
    assert greet(["Bob", "\"Charlie, Dianne\"", "ROSALIN"]) == \
           "Hello, Bob and Charlie, Dianne. AND HELLO, ROSALIN!"


def test_list_of_basic_name_with_escaped_comma_string_and_empty_string_to_greeting_with_escaped_lower_string_and_lower_name_and_anonymous():
    """Test return of basic name, empty string and escaped comma string with multiple names."""
    assert greet(["Bob", "\"Charlie, Dianne\"", ""]) == \
           "Hello, Bob, Charlie, Dianne, and my other friends."


def test_list_of_basic_name_with_escaped_comma_string_and_space_string_to_greeting_with_escaped_lower_string_and_lower_name_and_anonymous():
    """Test return of basic name, space string and escaped comma string with multiple names."""
    assert greet(["Bob", "\"Charlie, Dianne\"", "    "]) == \
           "Hello, Bob, Charlie, Dianne, and my other friends."


def test_list_of_few_basic_and_shout_names_with_escaped_comma_string_and_empty_string_and_comma_string_to_greeting_with_lower_names_and_shout_names_and_anonymous():
    """
    Test return of basic names, shout names, empty string, comma string, shout comma string,
    escaped comma string and shout escaped comma string.
    """
    assert greet(["Bob", "\"Charlie, Dianne\"", "", "ELEONORA", "David", "Jester",
                  "DORTAMOL", "DIEGO, VENTURA", "Fridrich, Yosep", "\"YOHANN, DOL\""]) == \
           "Hello, Bob, Charlie, Dianne, David, Jester, Fridrich, Yosep, and my other friends. " \
           "AND HELLO, ELEONORA, DORTAMOL, DIEGO, VENTURA, AND YOHANN, DOL!"


if __name__ == '__main__':
    pytest.main()
