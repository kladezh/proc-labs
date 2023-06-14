from operands import BinaryOperation, PrefixFunction, PostfixFunction


def parse(arr: list) -> str:
    return " ".join(str(x) for x in arr)


def isdigit(string: str) -> bool:
    if string.isdigit():
        return True
    try:
        float(string)
        return True
    except ValueError:
        return False


def convert_to_rpn(expr: list) -> list:
    result = []
    stack = []

    for symbol in expr:
        # число или постфиксная функция
        if isdigit(symbol) or PostfixFunction.isstr(symbol):
            result.append(symbol)

        # префиксная функция
        elif PrefixFunction.isstr(symbol):
            stack.append(symbol)

        # открывающая скобка
        elif symbol == "(":
            stack.append(symbol)

        # закрывающая скобка
        elif symbol == ")":
            while stack[-1] != "(":
                try:
                    result.append(stack.pop())
                except IndexError:
                    raise

            if stack[-1] == "(":
                stack.pop()

        # бинарная операция
        elif BinaryOperation.isstr(symbol):
            op = BinaryOperation.fromstr(symbol)
            # префиксная функция или бинарная операция и приоритет выше/равен
            while stack and (
                PrefixFunction.isstr(stack[-1])
                or (
                    (stack_op := BinaryOperation.fromstr(stack[-1]))
                    and (stack_op.priority >= op.priority)
                )
            ):
                result.append(stack.pop())
            stack.append(symbol)

    while stack:
        result.append(stack.pop())

    return result


def solve_expression(rpn_expr: list) -> float:
    stack = []

    for symbol in rpn_expr:
        try:
            # число
            if isdigit(symbol):
                stack.append(float(symbol))

            # бинарная операция
            elif BinaryOperation.isstr(symbol):
                right, left = stack.pop(), stack.pop()
                op = BinaryOperation.fromstr(symbol)

                stack.append(op.action(left, right))

            # префиксная или постфиксная функция
            elif (op := PrefixFunction.fromstr(symbol)) or (
                op := PostfixFunction.fromstr(symbol)
            ):
                last = stack.pop()
                stack.append(op.action(last))

        except IndexError:
            raise

    return stack.pop()


def main():
    expr = input("\nВведите выражение:\n")
    splited_expr = expr.split()

    rpn_expr = convert_to_rpn(splited_expr)
    print(f"\nПреобразованное выражение:\n{parse(rpn_expr)}\n")

    result = solve_expression(rpn_expr)
    print(f"\nРезультат: {result}")


if __name__ == "__main__":
    main()
