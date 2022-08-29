""""."""
import re
import math

regex_a = r'((- )?(\d+)?)x2(\D|$)'
regex_b = r'((- )?(\d+)?)x1?(\D|$)'
regex_c = r'((- )?((?:^)|(?<= ))\d+)( |$)'


class Student:
    """"."""

    def __init__(self, biggest_number: int):
        """
        Constructor.

        save biggest number into a variable that is attainable later on.
        Create a collection of all possible results [possible_answers] <- dont rename that (can be a list or a set)
        :param biggest_number: biggest possible number(inclusive) to guess
        NB: calculating using sets is much faster compared to lists
        """
        self.biggest_number = biggest_number
        self.possible_answers = set([all_possible_answers for all_possible_answers in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        """
        Regex can and should be used here.

        :param sentence: sentence to solve
        call one of the functions bellow (within this class) and return either one of the following strings:
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}." if there are multiple possibilities
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        a = self.regex_possible_actions(sentence)
        not_reverse = self.regex_find_reverse(sentence)
        if a[0] == "quadratic":
            result = self.deal_with_quadratic_equation(a[1], a[2], a[3], a[4])
        elif a[0] == "catalan":
            result = self.deal_with_catalan_sequence(not_reverse)
        elif a[0] == "fibonacci":
            result = self.deal_with_fibonacci_sequence(not_reverse)
        else:
            return self.no_complex(a, not_reverse)
        if len(result) > 1:
            return f"Possible answers are {sorted(result)}."
        return f"The number I needed to guess was {result[0]}."

    def no_complex(self, a, not_reverse):
        """"."""
        if a[0] == "prime":
            result = self.deal_with_primes(not_reverse)
        elif a[0] == "composite":
            result = self.deal_with_composites(not_reverse)
        elif a[0] == "zero":
            result = self.deal_with_number_of_zeroes(int(a[1]))
        elif a[0] == " one":
            result = self.deal_with_number_of_ones(int(a[1]))
        elif a[0] == "decimal":
            result = self.deal_with_dec_value(str(a[1]))
        elif a[0] == "hex":
            result = self.deal_with_hex_value(str(a[1]))
        elif a[0] == "order":
            result = self.deal_with_number_order(a[1], not_reverse)
        if len(result) > 1:
            return f"Possible answers are {sorted(result)}."
        return f"The number I needed to guess was {result[0]}."

    def regex_possible_actions(self, sentence: str):
        """"."""
        actions = ["catalan", "fibonacci", "prime", "composite", "zero", r" one", "decimal", "hex", "order", "quadratic"]
        additional_information_is_needed = ["zero", r" one", "decimal", "hex", "order"]
        for action in actions:
            act = self.regex_find_action(sentence, action)
            if act is True:
                if action in additional_information_is_needed:
                    return self.regex_find_addition_to_action(sentence, action)
                if action == "quadratic":
                    return self.quadratic_helper(sentence)
                return action, 0

    def regex_find_action(self, sentence: str, pattern: str):
        """"."""
        match = re.search(pattern, sentence)
        if match:
            return True
        else:
            return False

    def regex_find_reverse(self, sentence: str):
        """"."""
        anti = ["not", "doesn't", "don't", "isn't", "aren't"]
        for a in anti:
            match = re.search(a, sentence)
            if match:
                return False
        return True

    def regex_find_addition_to_action(self, sentence: str, action: str):
        """"."""
        pattern = ""
        if action in ["zero", r" one"]:
            pattern = r"\d+"
        elif action == "order":
            pattern = r"\w\wcreasing"
            match = re.search(pattern, sentence)
            if match.group() == "increasing":
                return action, True
            else:
                return action, False
        elif action == "hex" or action == "decimal":
            pattern = r'value: "([\d\w]+)"'
            match = re.search(pattern, sentence)
            return action, match.group(1)
        match = re.search(pattern, sentence)
        if match:
            return action, match.group(0)
        else:
            return False

    def quadratic_helper(self, sentence: str):
        """"."""
        eq = re.findall('"(.+)"', sentence)[0]
        bigger = True if re.findall("bigger|smaller", sentence)[0] == "bigger" else False
        action_value = re.findall(r"-?\d+\.\d+", sentence)[0] if len(re.findall(r"-?\d+\.\d+", sentence)) > 0 else 0
        action_m_d = None if action_value == 0 else True if len(re.findall("divide", sentence)) == 0 else False
        return "quadratic", eq, action_m_d, float(action_value), bigger

    def intersect_possible_answers(self, update: list):
        """
        Logical AND between two sets.

        :param update: new list to be put into conjunction with self.possible_answers
        conjunction between self.possible_answers and update
        https://en.wikipedia.org/wiki/Logical_conjunction
        """
        self.possible_answers &= set(update)
        return list(self.possible_answers)

    def exclude_possible_answers(self, update: list):
        """
        Logical SUBTRACTION between two sets.

        :param update: new list to be excluded from self.possible_answers
        update excluded from self.possible_answers
        """
        self.possible_answers -= set(update)
        return list(self.possible_answers)

    def deal_with_number_of_zeroes(self, amount_of_zeroes: int):
        """
        Filter possible_answers to match the amount of zeroes in its binary form.

        :param amount_of_zeroes: number of zeroes in the correct number's binary form
        """
        self.possible_answers = set(filter(lambda x: str(bin(x))[2:].count("0") == amount_of_zeroes, self.possible_answers))
        return list(self.possible_answers)

    def deal_with_number_of_ones(self, amount_of_ones: int):
        """
        Filter possible answers to match the amount of ones in its binary form.

        :param amount_of_ones: number of zeroes in the correct number's binary form
        """
        self.possible_answers = set(filter(lambda x: str(bin(x))[2:].count("1") == amount_of_ones, self.possible_answers))
        return list(self.possible_answers)

    def deal_with_primes(self, is_prime: bool):
        """
        Filter possible answers to either keep or remove all primes.

        Call find_primes_in_range to get all composite numbers in range.
        :param is_prime: boolean whether the number is prime or not
        """
        a = find_primes_in_range(self.biggest_number)
        if is_prime is True:
            return self.intersect_possible_answers(a)
        if is_prime is False:
            return self.exclude_possible_answers(a)
        return None

    def deal_with_composites(self, is_composite: bool):
        """
        Filter possible answers to either keep or remove all composites.

        Call find_composites_in_range to get all composite numbers in range.
        :param is_composite: boolean whether the number is composite or not
        """
        a = find_composites_in_range(self.biggest_number)
        if is_composite is True:
            return self.intersect_possible_answers(a)
        if is_composite is False:
            return self.exclude_possible_answers(a)
        return None

    def deal_with_dec_value(self, decimal_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: decimal value within the number like 9 in 192
        """
        self.possible_answers = set(filter(lambda x: decimal_value in str(x), self.possible_answers))
        return list(self.possible_answers)

    def deal_with_hex_value(self, hex_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: hex value within the number like e in fe2
        """
        self.possible_answers = set(filter(lambda x: hex_value in str(hex(x))[2:], self.possible_answers))
        return list(self.possible_answers)

    def deal_with_quadratic_equation(self, equation: str, to_multiply: bool, multiplicative: float, is_bigger: bool):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        Regex can be used here.
        Call quadratic_equation_solver with variables a, b, c.
        deal_with_dec_value should be called.
        :param equation: the quadratic equation
        :param to_multiply: whether it is necessary to multiply or divide with a given multiplicative
        :param multiplicative: the multiplicative to multiply or divide with
        :param is_bigger: to use the bigger or smaller result of the quadratic equation(min or max from [x1, x2])
        """
        normalized = normalize_quadratic_equation(equation)
        solved = quadratic_equation_solver(normalized)
        print(normalized, solved)
        if solved is None:
            return self.possible_answers
        value = float(solved) if len(solved) == 1 else float(solved[1]) if is_bigger is True else float(solved[0])
        if to_multiply is True:
            value *= float(multiplicative)
        elif to_multiply is False:
            value /= float(multiplicative)
        return self.deal_with_dec_value(str(round(value)))

    def deal_with_fibonacci_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all fibonacci numbers.

        Call find_fibonacci_numbers to get all fibonacci numbers in range.
        :param is_in: boolean whether the number is in fibonacci sequence or not
        """
        a = find_fibonacci_numbers(self.biggest_number)
        if is_in is True:
            return self.intersect_possible_answers(a)
        if is_in is False:
            return self.exclude_possible_answers(a)
        return None

    def deal_with_catalan_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all catalan numbers.

        Call find_catalan_numbers to get all catalan numbers in range.
        :param is_in: boolean whether the number is in catalan sequence or not
        """
        a = find_catalan_numbers(self.biggest_number)
        if is_in is True:
            return self.intersect_possible_answers(a)
        if is_in is False:
            return self.exclude_possible_answers(a)
        return None

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        """
        Filter possible answers to either keep or remove all numbers with wrong order.

        :param increasing: boolean whether to check is in increasing or decreasing order
        :param to_be: boolean whether the number is indeed in that order
        """
        if increasing is True:
            a = list(sorted(filter(lambda x: False not in [int(str(x)[a]) <= int(str(x)[a + 1]) for a in range(len(str(x)) - 1)], self.possible_answers)))
        elif increasing is False:
            a = list(sorted(filter(lambda x: False not in [int(str(x)[a]) >= int(str(x)[a + 1]) for a in range(len(str(x)) - 1)], self.possible_answers)))
        if to_be is True:
            return self.intersect_possible_answers(a)
        if to_be is False:
            return self.exclude_possible_answers(a)
        return None


def normalize_quadratic_equation(equation: str):
    """
    Normalize the quadratic equation.

    normalize_quadratic_equation("x2 + 2x = 3") => "x2 + 2x - 3 = 0"
    normalize_quadratic_equation("0 = 3 + 1x2") => "x2 + 3 = 0"
    normalize_quadratic_equation("2x + 2 = 2x2") => "2x2 - 2x - 2 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2") => "14x2 - x - 10 = 0"

    :param equation: quadratic equation to be normalized
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return: normalized equation
    """
    left, right = equation.split("=")
    quadro_l = sum(list(map(lambda x: 0 if len(x) == 0 else 1 if x[0] == " " or x[0] == "" else -1 if x[0] == "- " else eval(x[0]), re.findall(regex_a, left))))
    solo_l = sum(list(map(lambda x: 0 if len(x) == 0 else 1 if x[0] == " " or x[0] == "" else -1 if x[0] == "- " else eval(x[0]), re.findall(regex_b, left))))
    uno_l = sum(list(map(lambda x: 0 if len(x) == 0 else eval(x[0]), re.findall(regex_c, left))))
    quadro_r = sum(list(map(lambda x: 0 if len(x) == 0 else 1 if x[0] == " " or x[0] == "" else -1 if x[0] == "- " else eval(x[0]), re.findall(regex_a, right))))
    solo_r = sum(list(map(lambda x: 0 if len(x) == 0 else 1 if x[0] == " " or x[0] == "" else -1 if x[0] == "- " else eval(x[0]), re.findall(regex_b, right))))
    uno_r = sum(list(map(lambda x: 0 if len(x) == 0 else eval(x[0]), re.findall(regex_c, right))))
    quadro = quadro_l - quadro_r
    solo = solo_l - solo_r
    uno = uno_l - uno_r
    step1 = f"{quadro}x2 + {solo}x + {uno}"
    step2 = help_to_normalize(step1)
    return step2


def help_to_normalize(equation: str):
    """"."""
    a, b, c = equation.split("+")
    a = a.strip()
    b = b.strip()
    c = int(c.strip())
    alpha, beta = a.split("x")
    gamma, delta = b.split("x")
    alpha = int(alpha)
    gamma = int(gamma)
    if alpha == 0:
        if gamma < 0:
            gamma *= -1
            c *= -1
        elif gamma == 0:
            c = int(math.fabs(c))
    if a != "" and alpha < 0:
        alpha *= -1
        gamma *= -1
        c *= -1
    a = "x2" if alpha == 1 else f"{alpha}x2" if alpha != 0 else ""
    b = "" if gamma == 0 else f"{gamma}x" if math.fabs(gamma) != 1.0 and a == "" \
        else "x" if math.fabs(gamma) == 1.0 and a == "" else " + x" if gamma == 1 else " - x" if gamma == -1 else \
        f" + {gamma}x" if str(gamma).count("-") == 0 else f" - {gamma * -1}x"
    c = "" if c == 0 else f"{c}" if alpha == 0 and gamma == 0 else f" + {c}" if str(c).count("-") == 0 else f" - {c * -1}"
    return f"{a}{b}{c} = 0"


def quadratic_equation_solver(equation: str):
    """
    Solve the normalized quadratic equation.

    :param str: quadratic equation
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return:
    if there are no solutions, return None.
    if there is exactly 1 solution, return it.
    if there are 2 solutions, return them in a tuple, where smaller is first
    all numbers are returned as floats.
    """
    eq, zero = equation.split("=")
    print(equation, re.findall(regex_a, eq), re.findall(regex_b, eq), re.findall(regex_c, eq))
    if len(re.findall(regex_a, eq)) != 0:
        r_a = re.findall(regex_a, eq)[0][0]
        a = 1 if r_a == "" else -1 if r_a == "- " \
            else int(r_a)
    else:
        a = 0
    if len(re.findall(regex_b, eq)) != 0:
        r_b = re.findall(regex_b, eq)[0][0]
        b = 1 if r_b == " " or r_b == "" else -1 if r_b == "- " \
            else int(eval(r_b))
    else:
        b = 0
    if len(re.findall(regex_c, eq)) != 0:
        r_c = re.findall(regex_c, eq)[0][0]
        c = int(eval(r_c))
    else:
        c = 0
    if a == 0:
        if b == 0:
            return None
        return (-c) / b
    d = (b ** 2) - 4 * a * c
    if d < 0:
        return None
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 == x2:
        return x1
    return tuple(sorted([x1, x2]))


def find_primes_in_range(biggest_number: int):
    """
    Find all primes in range(end inclusive).

    :param biggest_number: all primes in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :return: list of primes
    """
    list = []
    if biggest_number >= 2:
        list.append(2)
    for i in range(biggest_number + 1):
        for a in range(2, math.ceil(math.sqrt(i) + 1)):
            if i % a == 0:
                break
            if a == math.ceil(math.sqrt(i)):
                list.append(i)
    return list


def find_composites_in_range(biggest_number: int):
    """
    Find all composites in range(end inclusive).

    Call find_primes_in_range from this method to get all composites
    :return: list of composites
    :param biggest_number: all composites in range of biggest_number(included)
    """
    list = []
    for i in range(3, biggest_number + 1):
        for a in range(2, math.ceil(math.sqrt(i) + 1)):
            if i % a == 0:
                list.append(i)
                break
    return list


def find_fibonacci_numbers(biggest_number: int):
    """
    Find all Fibonacci numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all fibonacci numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :return: list of fibonacci numbers
    """
    a = [0, 1, 1]
    if biggest_number == 0:
        return [0]
    if biggest_number == 1:
        return a
    if biggest_number == 2:
        return a + [2]
    n = 3
    fibo = 1
    while fibo <= biggest_number:
        fibo = help_find_fibonacci(n)
        n += 1
        a.append(fibo)
    return a[:-1]


def help_find_fibonacci(now: int):
    """"A."""
    if now <= 0:
        return 0
    if now == 1:
        return 1
    else:
        fibo = help_find_fibonacci(now - 1) + help_find_fibonacci(now - 2)
        return fibo


def find_catalan_numbers(biggest_number: int):
    """
    Find all Catalan numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all catalan numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Catalan_number
    :return: list of catalan numbers
    """
    a = []
    catalan = 0
    n = 0
    while catalan <= biggest_number:
        catalan = help_find_catalan(n)
        a.append(catalan)
        n += 1
    return a[:-1]


def help_find_catalan(n: int):
    """"."""
    if n <= 1:
        return 1
    catalan = 0
    for i in range(n):
        catalan += help_find_catalan(i) * help_find_catalan(n - 1 - i)
    return catalan


if __name__ == '__main__':
    s = Student(30)
    a = s.possible_answers
    last = list(s.possible_answers)[-1]
    print(a, last)
    print()
    print(s.deal_with_composites(True))
    print(s.deal_with_composites(False))
    print()
    print(s.deal_with_number_of_zeroes(1))
    print(s.deal_with_number_of_zeroes(3))
    print(s.deal_with_number_of_zeroes(4))
    print()
    print(s.deal_with_number_of_ones(2))
    print(s.deal_with_number_of_ones(3))
    print(s.deal_with_number_of_ones(4))
    print(s.deal_with_number_of_ones(5))
    print()
    print(s.deal_with_dec_value("0"))
    print(s.deal_with_dec_value("3"))
    print(s.deal_with_dec_value("4"))
    print(s.deal_with_dec_value("5"))
    print(s.deal_with_dec_value("6"))
    print()
    print(s.deal_with_hex_value("1"))
    print(s.deal_with_hex_value("2"))
    print(s.deal_with_hex_value("3"))
    print(s.deal_with_hex_value("6"))
    print()
    print(s.deal_with_primes(True))
    print(s.deal_with_primes(False))
    print("Order")
    print(s.deal_with_number_order(True, True))
    # print(s.deal_with_number_order(True, False))
    # print(s.deal_with_number_order(False, True))
    # print(s.deal_with_number_order(False, False))
    print()
    print(s.deal_with_fibonacci_sequence(True))
    print(s.deal_with_fibonacci_sequence(False))
    print()
    print(s.deal_with_catalan_sequence(True))
    print(s.deal_with_catalan_sequence(False))

    print(s.regex_find_addition_to_action('This number that we are speaking of right now contains decimal value: "5".', "decimal"))
    print(s.regex_find_addition_to_action('Number is not in increasing order.', "order"))
    print(s.regex_find_addition_to_action('The aforementioned number is made up of 4 zeroes in its binary form.', "zero"))
    a = [2, 3, 6, 7, 22, 23]
    print(s.exclude_possible_answers(a))
    # def print_regex_results(regex, f):
    #     for match in re.finditer(regex, f):
    #         print(match.group(1))
    #
    #
    # f = "3x2 - 4x + 1"
    #
    # print_regex_results(regex_a, f)  # 3
    # print_regex_results(regex_b, f)  # - 4
    # print_regex_results(regex_c, f)  # 1
    #
    # f2 = "3x2 + 4x + 5 - 2x2 - 7x + 4"
    #
    # print("x2")
    # print_regex_results(regex_a, f2)  # 3, - 2
    # print("x")
    # print_regex_results(regex_b, f2)  # 4, - 7
    # print("c")
    # print_regex_results(regex_c, f2)  # 5, 4
