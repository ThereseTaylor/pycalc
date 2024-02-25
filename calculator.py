def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def main():
    while True:
        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        print(x, y)


if __name__ == "__main__":
    main()
