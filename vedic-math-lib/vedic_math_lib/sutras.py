def ekadhikena_purvena(n: int) -> int:
    """
    Ekadhikena Purvena: By one more than the previous one.
    Used in the context of squaring numbers ending in 5.
    """
    last_digit = n % 10
    if last_digit != 5:
        raise ValueError("This method only works for numbers ending in 5")
    
    previous_part = n // 10
    return previous_part * (previous_part + 1) * 100 + 25


def nikhilam_navatascaramam_dasatah(n: int) -> int:
    """
    Nikhilam Navatashcaramam Dashatah: All from 9 and the last from 10.
    Used to simplify multiplication by subtracting the number from a base (e.g. 10, 100).
    """
    base = 10 ** len(str(n))
    return base - n


def urdhva_tiryagbhyam(a: int, b: int) -> int:
    """
    Urdhva-Tiryagbhyam: Vertically and crosswise multiplication.
    General multiplication rule for two numbers using the cross-multiplication method.
    """
    return a * b


def paravartya_yojayet(a: int, b: int) -> float:
    """
    Paravartya Yojayet: Transpose and adjust.
    Used for solving simple equations by transposing terms.
    """
    return a / b


def sunyam_samyasamuccaye(a: int, b: int) -> bool:
    """
    Śūnyaṃ Sāmyasamuccayam: If the sum is the same, that sum is zero.
    If the factors on both sides of an equation are equal, then the equation equals zero.
    """
    return a == b


def anurupyena(a: int, b: int, base: int = 10) -> float:
    """
    Anurupyena: Proportionately.
    A general rule for working with proportionality in multiplication and division.
    """
    return (a * b) / base


def sankalana_vyavakalanabhyam(a: int, b: int) -> tuple:
    """
    Sankalana-Vyavakalanābhyām: By addition and subtraction.
    Used for solving simultaneous equations by adding and subtracting.
    """
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result


def purnapurnabhyam(a: int, b: int) -> int:
    """
    Pūrṇāpūrṇābhyām: By the completion or non-completion.
    A method for multiplication when numbers are near powers of 10.
    """
    base = 10 ** max(len(str(a)), len(str(b)))
    return (base - a) * (base - b)


def chalana_kalanabhyam(a: int, b: int) -> int:
    """
    Chālanā-Kālanābhyām: Differences and similarities.
    Used for division when numbers are close to the base.
    """
    return a // b


def yavadunam(n: int, base: int) -> int:
    """
    Yāvadūnam: Whatever the extent of deficiency.
    Used to square numbers that are close to a power of 10.
    """
    difference = base - n
    return (difference ** 2) + (n * (2 * base - n))


def visti_sesa_sankalana(n: int, base: int) -> int:
    """
    Viṣṭiseseṣāṇe Sankalana: Using the last digit or remainder to simplify calculations.
    This formula is used to simplify operations by focusing on remainders.
    """
    return n % base


def ksepanam(n: int, adjustment: int) -> int:
    """
    Kṣepaṇam: Using excess or deficiency to simplify calculations.
    Add or subtract an adjustment to make calculations easier.
    """
    return n + adjustment


def pratyayoyadah(a: int, b: int) -> int:
    """
    Pratyayoyādah: A method for finalizing calculations, often by applying a final step like adding or multiplying.
    """
    return a * b + (a + b)


def gunakasamuccaya(a: int, b: int) -> int:
    """
    Guṇakasamuccaya: The product of the sums equals the sum of the products.
    This method is used for simplifying polynomial products.
    """
    return (a + b) * (a + b)


def muladhara(n: int, base: int = 10) -> int:
    """
    Mūladhāra: The base principle.
    A general method for squaring numbers close to the base.
    """
    return (n ** 2) - (2 * base * n) + base ** 2


def samuccayavarga_sanjna(a: int, b: int) -> bool:
    """
    Samuccayavarga Sañjñā: If the factors are the same on both sides, they can be canceled.
    Used to simplify equations by canceling out equal terms on both sides.
    """
    return a == b
