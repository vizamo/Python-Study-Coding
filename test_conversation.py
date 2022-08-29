from conversation import Student, normalize_quadratic_equation


def test_sentence_composite():
    """"."""
    s = Student(30)
    sentence6 = "This number, that you need to guess is composite."
    sentence1 = "This number, that you need to guess is with no hesitation composite."
    sentence2 = "The given number occurs to be composite."
    sentence3 = "This number, that you need to guess is with no hesitation composite."
    sentence4 = "Number is composite."
    sentence5 = "The given number occurs to be composite."
    check = "Possible answers are [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]."
    assert s.decision_branch(sentence1) == check
    assert s.decision_branch(sentence2) == check
    assert s.decision_branch(sentence3) == check
    assert s.decision_branch(sentence4) == check
    assert s.decision_branch(sentence5) == check
    assert s.decision_branch(sentence6) == check


def test_sentence_composite_not():
    """"."""
    s = Student(30)
    sentence1 = "This number, that you need to guess is not a composite."
    sentence2 = "The aforementioned number does not occur to be composite."
    sentence3 = "The aforementioned number doesn't happen to be composite."
    sentence4 = "This number does not happen to be composite."
    check = "Possible answers are [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]."
    assert s.decision_branch(sentence1) == check
    assert s.decision_branch(sentence2) == check
    assert s.decision_branch(sentence3) == check
    assert s.decision_branch(sentence4) == check


def test_sentence_zero():
    """"."""
    s = Student(30)
    sentence1 = "Number has 1 zero in its binary form."
    sentence2 = "The aforementioned number is made up of 4 zeroes in its binary form."
    sentence3 = "Number has 4 zeroes in its binary form."
    sentence4 = "This number is made up of 1 zero in its binary form."
    sentence5 = "The given number has 3 zeroes in its binary form."
    check1 = "Possible answers are [0, 2, 5, 6, 11, 13, 14, 23, 27, 29, 30]."
    check3 = "Possible answers are [8, 17, 18, 20, 24]."
    check4 = "The number I needed to guess was 16."
    assert s.decision_branch(sentence1) == check1
    assert s.decision_branch(sentence2) == check4
    assert s.decision_branch(sentence3) == check4
    assert s.decision_branch(sentence4) == check1
    assert s.decision_branch(sentence5) == check3


def test_sentence_one():
    """"."""
    s = Student(30)
    sentence1 = "Number is made up of 4 ones in its binary form."
    sentence2 = "Number is made up of 3 ones in its binary form."
    sentence4 = "Number is made up of 2 ones in its binary form."
    sentence5 = "The aforementioned number is made up of 4 ones in its binary form."
    sentence6 = "This number has 3 ones in its binary form."
    sentence7 = "This number that we are speaking of right now is made up of 4 ones in its binary form."
    check2 = "Possible answers are [3, 5, 6, 9, 10, 12, 17, 18, 20, 24]."
    check3 = "Possible answers are [7, 11, 13, 14, 19, 21, 22, 25, 26, 28]."
    check4 = "Possible answers are [15, 23, 27, 29, 30]."
    assert s.decision_branch(sentence1) == check4
    assert s.decision_branch(sentence2) == check3
    assert s.decision_branch(sentence4) == check2
    assert s.decision_branch(sentence5) == check4
    assert s.decision_branch(sentence6) == check3
    assert s.decision_branch(sentence7) == check4


def test_sentence_dec():
    """"."""
    s = Student(30)
    sentence1 = 'Number includes decimal value: "4".'
    sentence2 = 'This number is comprised of decimal value: "0".'
    sentence3 = 'The given number contains decimal value: "5".'
    sentence4 = 'This number that we are speaking of right now contains decimal value: "5".'
    sentence5 = 'This number, that you need to guess is comprised of decimal value: "6".'
    sentence6 = 'Number is comprised of decimal value: "3".'
    check0 = "Possible answers are [0, 10, 20, 30]."
    check3 = "Possible answers are [3, 13, 23, 30]."
    check4 = "Possible answers are [4, 14, 24]."
    check5 = "Possible answers are [5, 15, 25]."
    check6 = "Possible answers are [6, 16, 26]."
    assert s.decision_branch(sentence1) == check4
    assert s.decision_branch(sentence2) == check0
    assert s.decision_branch(sentence3) == check5
    assert s.decision_branch(sentence4) == check5
    assert s.decision_branch(sentence5) == check6
    assert s.decision_branch(sentence6) == check3


def test_sentence_hex():
    """"."""
    s = Student(100)
    sentence1 = 'This number is comprised of hex value: "2".'
    sentence2 = 'Number is comprised of hex value: "6".'
    sentence3 = 'This number that we are speaking of right now is comprised of hex value: "3".'
    sentence4 = 'Number involves hex value: "3".'
    sentence5 = 'This number, that you need to guess includes hex value: "3".'
    sentence6 = 'This number includes hex value: "1".'
    sentence7 = 'The given number is comprised of hex value: "1".'
    sentence8 = 'This number includes hex value: "1".'
    check1 = "Possible answers are [1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]."
    check2 = "Possible answers are [2, 18]."
    check3 = "Possible answers are [3, 19]."
    check6 = "Possible answers are [6, 22]."
    assert s.decision_branch(sentence1) == check2
    assert s.decision_branch(sentence2) == check6
    assert s.decision_branch(sentence3) == check3
    assert s.decision_branch(sentence4) == check3
    assert s.decision_branch(sentence5) == check3
    assert s.decision_branch(sentence6) == check1
    assert s.decision_branch(sentence7) == check1
    assert s.decision_branch(sentence8) == check1

def test_sentence_prime():
    """"."""
    s = Student(30)
    sentence = "This number that we are speaking of right now must occur to be prime."
    check = "Possible answers are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]."
    assert s.decision_branch(sentence) == check


def test_sentence_prime_not():
    """"."""
    s = Student(30)
    sentence1 = "Number doesn't occur to be prime."
    sentence2 = "This number that we are speaking of right now does not occur to be prime."
    sentence3 = "This number, that you need to guess doesn't occur to be prime."
    sentence4 = "The given number doesn't occur to be prime."
    sentence5 = "This number doesn't happen to be prime."
    check = "Possible answers are [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]."
    assert s.decision_branch(sentence1) == check
    assert s.decision_branch(sentence2) == check
    assert s.decision_branch(sentence3) == check
    assert s.decision_branch(sentence4) == check
    assert s.decision_branch(sentence5) == check


def test_sentence_order_inc():
    """"."""
    s = Student(100)
    sentence1 = "Number is without a doubt in increasing order."
    sentence2 = "This number, that you need to guess happens to be in increasing order."
    sentence3 = "This number, that you need to guess is in increasing order."
    sentence4 = "The aforementioned number is in increasing order."
    check = "Possible answers are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 38, 39, 44, 45, 46, 47, 48, 49, 55, 56, 57, 58, 59, 66, 67, 68, 69, 77, 78, 79, 88, 89, 99]."
    assert s.decision_branch(sentence1) == check
    assert s.decision_branch(sentence2) == check
    assert s.decision_branch(sentence3) == check
    assert s.decision_branch(sentence4) == check


def test_sentence_order_inc_not():
    """"."""
    s = Student(100)
    sentence1 = "Number is not in increasing order."
    sentence2 = "The aforementioned number does not occur to be in increasing order."
    sentence3 = "This number that we are speaking of right now does not occur to be in increasing order."
    sentence4 = "The aforementioned number doesn't occur to be in increasing order"
    sentence5 = "This number does not happen to be in increasing order."
    check = "Possible answers are [10, 20, 21, 30, 31, 32, 40, 41, 42, 43, 50, 51, 52, 53, 54, 60, 61, 62, 63, 64, 65, 70, 71, 72, 73, 74, 75, 76, 80, 81, 82, 83, 84, 85, 86, 87, 90, 91, 92, 93, 94, 95, 96, 97, 98, 100]."
    assert s.decision_branch(sentence1) == check
    assert s.decision_branch(sentence2) == check
    assert s.decision_branch(sentence3) == check
    assert s.decision_branch(sentence4) == check
    assert s.decision_branch(sentence5) == check


def test_sentence_order_dec():
    """"."""
    s = Student(100)
    sentence = "Number is in decreasing order."
    check = "Possible answers are {}."
    assert s.decision_branch(sentence) == check


def test_sentence_order_dec_not():
    """"."""
    s = Student(100)
    sentence = "The aforementioned number doesn't occur to be in decreasing order."
    check = "Possible answers are {}."
    assert s.decision_branch(sentence) == check


def test_sentence_fibo():
    """"."""
    s = Student(232)
    sentence = "This number that we are speaking of right now is without a doubt in fibonacci sequence."
    check = "Possible answers are [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]."
    assert s.decision_branch(sentence) == check


def test_sentence_fibo_not():
    """"."""
    s = Student(30)
    sentence1 = "Number does not happen to be in fibonacci sequence."
    sentence2 = "This number, that you need to guess does not happen to be in fibonacci sequence."
    sentence3 = "This number that we are speaking of right now is not in fibonacci sequence."
    sentence4 = "The given number isn't in fibonacci sequence."
    sentence5 = "This number does not happen to be in fibonacci sequence."
    sentence6 = "This number, that you need to guess does not occur to be in fibonacci sequence."
    sentence7 = "The given number doesn't happen to be in fibonacci sequence."
    check = "Possible answers are [4, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30]."
    assert s.decision_branch(sentence1) == check
    assert s.decision_branch(sentence2) == check
    assert s.decision_branch(sentence3) == check
    assert s.decision_branch(sentence4) == check
    assert s.decision_branch(sentence5) == check
    assert s.decision_branch(sentence6) == check
    assert s.decision_branch(sentence7) == check


def test_sentence_catalan():
    """"."""
    s = Student(30)
    sentence = "This number that we are speaking of right now does happen to be in catalan sequence."
    check = "Possible answers are [1, 2, 5, 14]."
    assert s.decision_branch(sentence) == check


def test_sentence_catalan_not():
    """"."""
    s = Student(30)
    sentence1 = "This number that we are speaking of right now doesn't happen to be in catalan sequence."
    sentence2 = "The given number isn't in catalan sequence."
    sentence3 = "The aforementioned number isn't in catalan sequence."
    sentence4 = "The given number is not in catalan sequence."
    sentence5 = "This number that we are speaking of right now does not happen to be in catalan sequence."
    sentence6 = "This number that we are speaking of right now isn't in catalan sequence."
    check = "Possible answers are [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]."
    assert s.decision_branch(sentence1) == check
    assert s.decision_branch(sentence2) == check
    assert s.decision_branch(sentence3) == check
    assert s.decision_branch(sentence4) == check
    assert s.decision_branch(sentence5) == check
    assert s.decision_branch(sentence6) == check


def test_sentence_normalize_quadratic_equation():
    """"."""
    assert normalize_quadratic_equation("x2 + 2x = 3") == "x2 + 2x - 3 = 0"
    assert normalize_quadratic_equation("0 = 3 + 1x2") == "x2 + 3 = 0"
    assert normalize_quadratic_equation("2x + 2 = 2x2") == "2x2 - 2x - 2 = 0"
    assert normalize_quadratic_equation("0x2 - 2x = 1") == "2x + 1 = 0"
    assert normalize_quadratic_equation("0x2 - 2x = 1") == "2x + 1 = 0"
    assert normalize_quadratic_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2") == "14x2 - x - 10 = 0"
    assert normalize_quadratic_equation("0 = 1") == "1 = 0"
    assert normalize_quadratic_equation("0x2 - 0x + 1 = 0") == "1 = 0"
    assert normalize_quadratic_equation("3 + 6 - 2 + x2 = 0") == "x2 + 7 = 0"


def test_sentence_quadro_a():
    """"."""
    s = Student(30)
    sentence1 = 'This number, that you need to guess is comprised of a digit, where the bigger result ' \
                'for the following quadratic equation:' \
        '"- 1 - 39x2 - 19x = 64 - 52 + 23x2 - 61x + 41x - 27 + 81x2 - 53x2" ' \
                'is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_b():
    """"."""
    s = Student(30)
    sentence1 = 'This number is comprised of a digit where 3.0000 times the bigger result ' \
                'for the following quadratic equation:' \
        '"67x + 32x2 - 60x2 + 74x2 - 76 - 98 + 95 + 18x - 98x - 86x + 17 - 68x2 + 100x + 181 = 98" ' \
                'is divided by 0.1000 and is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_c():
    """"."""
    s = Student(30)
    sentence1 = 'The given number includes a digit where 0.5625 times the bigger result ' \
                'for the following quadratic equation:' \
        '"59x2 - 57x + 97x2 + 45x + 87 + 67 + 41x = - 58x + 87 - 61 + 82x + 4x + 48 + 159x2" ' \
                'is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_d():
    """"."""
    s = Student(30)
    sentence1 = 'Number includes a digit, where the bigger result ' \
                'for the following quadratic equation:' \
        '"- 39 + 41x + 75x + 54 - 67x + 171 - 70x2 - 27 - 90 - 48x = 0" ' \
                'is divided by 0.3333 and is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_e():
    """"."""
    s = Student(30)
    sentence1 = 'This number, that you need to guess includes a digit where -4.9020 times the smaller result ' \
                'for the following quadratic equation:' \
        '"47x2 + 1x - 33x2 - 29 + 93 + 69x2 - 115 = - 38x2 + 71x2" ' \
                'is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_f():
    """"."""
    s = Student(30)
    sentence1 = 'The aforementioned number involves a digit, where the smaller result ' \
                'for the following quadratic equation:' \
        '"- 17x2 + 79x2 = 97x + 2x2 + 117x2 - 46x - 61x + 27x - 18x - 42 - 46x2" ' \
                'is divided by -0.2121 and is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_g():
    """"."""
    s = Student(30)
    sentence1 = 'This number contains a digit, where the bigger result ' \
                'for the following quadratic equation:' \
        '"- 52x + 69x = - 67x2 - 49x2 + 145x - 41x2 + 3x2 - 58x - 71x + 10 - 86x2 + 175x2" ' \
                'is divided by 0.3846 and is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_h():
    """"."""
    s = Student(30)
    sentence1 = 'This number includes a digit, where the bigger result ' \
                'for the following quadratic equation:' \
        '"- 32 + 53x2 - 43x2 - 76x = 0" ' \
                'is divided by 1.6000 and is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_j():
    """"."""
    s = Student(30)
    sentence1 = 'This number, that you need to guess is comprised of a digit where -5.0000 times the smaller result ' \
                'for the following quadratic equation:' \
        '"48x2 + 5 - 83x - 6x - 9x2 + 158x - 83x + 46x - 47x2 + 82x2 = 31x + 3x2 + 105 - 52 + 22" ' \
                'is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_k():
    """"."""
    s = Student(30)
    sentence1 = 'The given number involves a digit where 7.0000 times the bigger result ' \
                'for the following quadratic equation:' \
        '"97 - 56 + 38x + 81x - 60x2 - 31 - 121x + 94x2 - 42x2 = 0" ' \
                'is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_l():
    """"."""
    s = Student(30)
    sentence1 = 'Number contains a digit, where the smaller result ' \
                'for the following quadratic equation:' \
        '"29 - 20x - 1 - 86x2 - 252x + 87x + 91x + 6x = - 30x" ' \
                'is divided by -0.1429 and is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


def test_sentence_quadro_m():
    """"."""
    s = Student(30)
    sentence1 = 'This number, that you need to guess involves a digit where 7.0000 times the bigger result ' \
                'for the following quadratic equation:' \
        '"- 29x2 + 32 - 81 - 2 + 99 - 12 = - 1x + 8" ' \
                'is rounded to closest integer.'
    check = "Possible answers are {}."
    assert s.decision_branch(sentence1) == check


import re
# regex_a = r'(-? ?(\d+)?)?x2'
# regex_b = r'(-? ?\d+|-? ?.)?x(1| |$)'
# regex_c = r'[^a-z][0-9]+[^a-z]|^(-? ?\d+)$'
#
# regex_c = r'(-?[^\w]\d+) |$'
# regex_c = r'(-?[^\w]\d+)[^\w]'
# regex_c = r'(-?[\s]\d+)[$\s]'
# regex_c = r'([^a-z][0-9]+[^a-z])'

# regex_a = r'(-? ?\d+)?x2'
# regex_b = r'(-? ?\d+|-? ?.)?x(1| )'
# regex_c = r'[^x+](-? ?\d+)( |$)'

regex_a = r'((- )?(\d+)?)x2(\D|$)'
regex_b = r'((- )?(\d+)?)x1?(\D|$)'
regex_c = r'(?: |^)((- )?\d+)( |$)'

# regex_c = r'[^x+](-? ?\d+)( |$)'
# regex_c = r'( |^)((- )?\d+)( |$)'


def test_regex_a():
    """"."""
    f = re.search(regex_a, "12x22 - 2x")
    assert f == None


def test_regex_b():
    """"."""
    text = "1 - x2"
    match = re.search(regex_a, text)
    print(match)
    assert match.group(1) == "- "


def test_regex_c():
    """"."""
    text = "3x"
    match = re.search(regex_b, text)
    match2 = re.findall(regex_b, text)
    print(match)
    print(match2)
    assert match.group(1) == "3"


def test_regex_d():
    """"."""
    text = "42x + 3x2 - 21"
    match = re.search(regex_c, text)
    match2 = re.findall(regex_c, text)
    print(match)
    print(match2)
    assert match.group(1) == "- 21"
