#2025.9.10 L3
''' 
Data types
int, float, str, 
bool(True/False --必须大写), 
complex(虚数用j不用i, j前面必须有数字才能是虚数单位, 而不是字母) -- 1j而不是j,
None(必须大写N), 
list, tuple, dict, set, dict, set, frozenset

1️⃣
2.23e-3 == 2.23 * 10^(-3)
(Integer) object can't be modified

e.g.
x = 10
x = 20
是创造了一个新的object, 然后把x指向了新的object

2️⃣
string: 
one character: ''
more than one character: ""


'''

def main():
    x = 10
    print(type(x)) # int

    x = y = 20
    print(id(x), id(y)) # xy同时赋值，id()显示内存地址相同 -> 说明x和y指向同一个object

    x = 1 + 1j # imaginary part
    print(type(x))

    #define more than one variable
    a, b, c = 1, 2.2, "hello"

    name: str = "Desmond" # or name = str("Desmond")

if __name__ == "__main__":
    main()