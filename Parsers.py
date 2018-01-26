from math import pi, ceil
def Parse_Data_edit(line, conf, is_mas):
    line = line.replace(" ", '')
    line = line.split(";")
    if not is_mas:
        return [eval_(line[0])]
    count_tick = [0]*len(line)
    t = conf.t_mas[len(conf.t_mas)-1]
    all_tick = t * conf.Accuracy[0]
    count = 0
    for i in range(len(line)):
        if line[i].find("[") != -1:
            count_tick[i] = int(eval_(line[i][line[i].find("[")+1:line[i].find("]")]) * conf.Accuracy[0])
            line[i] = line[i][:line[i].find("[")]
            all_tick -= count_tick[i]
            count += 1
    if len(line) != count:
        mid_count = ceil(all_tick/(len(line) - count))
    else:
        mid_count = 1;
    ret = []
    for i in range(len(line)):
        if count_tick[i] == 0:
            count_tick[i] = mid_count
        x = line[i]
        x = x.split("...")
        if len(x) == 2:
            a = eval_(x[0])
            b = eval_(x[1])
            step = (b-a)/count_tick[i]
        else:
            a = b = eval_(x[0])
            step = 0
        for i in range(count_tick[i]):
            ret.append(a)
            a += step
            if a > b:
                a = b
    return ret[:int(t * conf.Accuracy[0])]
#-----------------------------------------------------------------------------------------

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
             '^': (3, lambda x, y: x**y)}

def eval_(formula):
    def parse(formula_string):
        formula_string = formula_string.replace('pi', '3.14159')
        formula_string = formula_string.replace(',', '.')
        last_number = False
        neg = False
        number = ''
        for s in formula_string:
            if s in '1234567890.':
                number += s
            elif number:
                yield (float(number), -float(number))[neg]
                number = ''
                neg = False
                last_number = True
            if s in OPERATORS or s in "()":
                if s == '-' and not last_number:
                    neg = not neg
                else:
                    yield s
                    last_number = False
        if number:
            yield (float(number), -float(number))[neg]

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                try:
                    stack.append(OPERATORS[token][1](x, y))
                except ArithmeticError:
                    return None
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parse(formula)))



def Parse_Graph_edit(line, conf):
    Var_mas = [('t', conf.t_mas), ('m_r', conf.m_rocket), ('h', conf.distance), ('a_r', conf.a_rocket),
               ('u_r', conf.u_rocket), ("m_f", conf.m_fuel), ('u_f', conf.u_fuel), ('c_f', conf.c_fuel),
               ('p_a', conf.Atmospher_density), ('s_r', conf.S_rocket), ('C_r', conf.Coefficient_resistance),
               ('Mol_A', conf.Mol_gas), ('T_A', conf.Temperature)]
    Var = [("G", conf.G[0]), ("M_P", conf.M_planet[0]),
           ('R_P', conf.R_planet[0]),("pi", pi)]
    line = line.replace(' ', '')
    line = line.split(";")
    if len(line) > 2:
        raise LookupError
    x = []
    y = []

    for a, b in Var:
        line[0] = line[0].replace(a, '{:.100f}'.format(b))
        line[1] = line[1].replace(a, '{:.100f}'.format(b))

    t = conf.t_mas[len(conf.t_mas)-1]
    for i in range(int(t * conf.Accuracy[0])):
        temp_line = line[0][:]
        for a, b in Var_mas:
            temp_line = temp_line.replace(a, str(b[i]))
        for c in temp_line:
            if c.isalpha():
                raise SyntaxError
        ret_value = eval_(temp_line)
        if ret_value == None:
            x.append(None)
            y.append(None)
            continue
        x.append(ret_value)

        temp_line = line[1][:]
        for a, b in Var_mas:
            temp_line = temp_line.replace(a, str(b[i]))
        for c in temp_line:
            if c.isalpha():
                raise SyntaxError
        ret_value = eval_(temp_line)
        if ret_value == None:
            x[len(x) - 1] = None
        y.append(ret_value)

    return x, y
