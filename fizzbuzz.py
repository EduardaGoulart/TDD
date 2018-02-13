"""
Regras do FizzBuzz

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para as demais posições: o próprio número
"""

#Calcula os múltiplos de 3
def multiple_of_3(num):
    return num % 3 == 0


#Calcula os múltiplos de 5
def multiple_of_5(num):
    return num % 5 == 0


def robot(poss):

    say = str(poss)

    if poss % 5 == 0 and poss % 3 == 0:
        say = 'fizzbuzz'

    elif multiple_of_5(poss):
        say = 'buzz'

    elif multiple_of_3(poss):
        say = 'fizz'

    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'

