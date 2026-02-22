import random



random.seed() 

def gen_aritmetika():
    a = random.randint(2, 20)
    b = random.randint(2, 20)
    c = random.randint(2, 10)
    ops = random.choice([('+', '-'), ('+', '*'), ('-', '*')])
    expr = f"{a} {ops[0]} {b} {ops[1]} {c}"
    return f"1) Vypočítej: {expr}"

def gen_linearni_rovnice():
    
    x = random.randint(-10, 10)
    a = random.randint(1, 10)
    b = random.randint(-20, 20)
    c = a * x + b
    return f"2) Najdi x: {a}x + ({b}) = {c}"

def gen_textovy_priklad():
    osoba1 = random.choice(["Petr", "Anna", "Karel", "Eva"])
    osoba2 = random.choice(["tomu", "jí", "mu"])  
    pocet = random.randint(5, 25)
    rozdelit = random.randint(2, 6)
    return (f"3) {osoba1} má {pocet} jablek. Rozdělí je rovnoměrně mezi {rozdelit} přátel. "
            "Kolik jablek dostane každý a kolik zůstane?")

if __name__ == "__main__":
    examples = [
        gen_aritmetika(),
        gen_linearni_rovnice(),
        gen_textovy_priklad()
    ]
    for ex in examples:
        print(ex)