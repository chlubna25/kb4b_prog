def frakbob(a, b):
    return st.frakce.soucet(a, b)
def frakbob_odecteni(a, b):
    return st.frakce.rozdil(a, b)
def frakbob_nasobeni(a, b):
    return st.frakce.soucin(a, b)
def frakbob_deleni(a, b):
    return st.frakce.podil(a, b)
def frakbob_zkraceni(a):
    return st.frakce.zkraceni(a)
def frakbob_rozsireni(a, b):
    return st.frakce.rozsireni(a, b)
def frakbob_na_cislo(a, b):
    return st.frakce.nasobeni_cislem(a, b)
def frakbob_delit_cislem(a, b):
    return st.frakce.deleni_cislem(a, b)
def frakbob_to_float(a):
    return st.frakce.to_float(a)
def frakbob_from_float(a):
    return st.frakce.from_float(a)
def frakbob_to_string(a):
    return st.frakce.to_string(a)
def frakbob_from_string(a):
    return st.frakce.from_string(a)
def frakbob_compare(a, b):
    return st.frakce.porovnani(a, b)
def frakbob_simplify(a):
    return st.frakce.zjednoduseni(a)
def frakbob_get_numerator(a):
    return st.frakce.get_citatel(a)
def frakbob_get_denominator(a):
    return st.frakce.get_jmenovatel(a)

def frakbob_create(numerator, denominator):
    return st.frakce.vytvor(numerator, denominator)
def frakbob_to_mixed_number(a):
    return st.frakce.to_mixed_number(a)
def frakbob_from_mixed_number(whole, numerator, denominator):
    return st.frakce.from_mixed_number(whole, numerator, denominator)
def frakbob_decimal_to_fraction(decimal_str):