# Defined with the keyword 'lambda'
# syntax:   lambda (parameters) : (expression)

# Use lambda as in-place functions

def celsiusToFahrenheit(temp):
    return (temp * 9 / 5) + 32


def fahrenheitToCelsius(temp):
    return (temp - 32) * 5 / 9


def main():
    ctemp = [0, 12, 34, 100]
    ftemp = [32, 65, 100, 212]

    # Use regular functions to convert the temperature
    print("With regular functions")
    print("F to C", list(map(fahrenheitToCelsius, ftemp)))
    print("C to F", list(map(celsiusToFahrenheit, ctemp)))
    # Use lambda to do the same job
    print("Now using lambda functions")
    print("F to C (lambda)", list(map(lambda t: (t - 32) * 5 / 9, ftemp)))
    print("C to F (lambda)", list(map(lambda t:  (t * 9 / 5) + 32, ctemp)))


if __name__ == '__main__':
    main()
