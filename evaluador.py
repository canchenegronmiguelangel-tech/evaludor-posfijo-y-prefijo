class Pila:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.esta_vacia():
            raise ValueError("Expresión inválida: faltan operandos")
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)


OPERADORES = ("+", "-", "*", "/", "^")


def aplicar(op, a, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("División entre cero")
        return a / b
    if op == "^":
        return a ** b


def evaluar_posfija(expr, mostrar_pasos=True):
    p = Pila()
    for t in expr.split():
        if t in OPERADORES:
            b = p.pop()
            a = p.pop()
            r = aplicar(t, a, b)
            if mostrar_pasos:
                print(f"   {a} {t} {b} = {r}")
            p.push(r)
        else:
            p.push(float(t))
    resultado = p.pop()
    if not p.esta_vacia():
        raise ValueError("Expresión inválida: sobran operandos")
    return resultado


def evaluar_prefija(expr, mostrar_pasos=True):
    p = Pila()
    for t in reversed(expr.split()):
        if t in OPERADORES:
            a = p.pop()  # operando izquierdo
            b = p.pop()  # operando derecho
            r = aplicar(t, a, b)
            if mostrar_pasos:
                print(f"   {a} {t} {b} = {r}")
            p.push(r)
        else:
            p.push(float(t))
    resultado = p.pop()
    if not p.esta_vacia():
        raise ValueError("Expresión inválida: sobran operandos")
    return resultado


def menu():
    print("\n==============================")
    print("  EVALUADOR DE EXPRESIONES")
    print("==============================")
    print("1. Evaluar expresión POSFIJA")
    print("2. Evaluar expresión PREFIJA")
    print("3. Ver ejemplos")
    print("4. Salir")
    return input("Elige una opción: ").strip()


def main():
    while True:
        opcion = menu()

        if opcion == "1":
            print("Ejemplo: 3 4 + 2 *   (separa con espacios)")
            expr = input("Expresión posfija: ")
            try:
                print("Pasos:")
                print("Resultado:", evaluar_posfija(expr))
            except (ValueError, ZeroDivisionError) as e:
                print("Error:", e)

        elif opcion == "2":
            print("Ejemplo: * + 3 4 2   (separa con espacios)")
            expr = input("Expresión prefija: ")
            try:
                print("Pasos:")
                print("Resultado:", evaluar_prefija(expr))
            except (ValueError, ZeroDivisionError) as e:
                print("Error:", e)

        elif opcion == "3":
            print("\nPosfija: 3 4 + 2 *")
            print("Resultado:", evaluar_posfija("3 4 + 2 *"))
            print("\nPrefija: * + 3 4 2")
            print("Resultado:", evaluar_prefija("* + 3 4 2"))

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()