"""This module converts RuneScape prices to regular floats.

For some reason, Jagex represents prices in a way that is
human-readable, but not very machine readable. RuneScape prices come
in four varieties:

* Normal real number.

        123.456

* Thousands.

        123.456k

* Millions.

        123.456m

* Billions.

        123.456b

"""

SUFFIXES = {
    'k': 1e3,
    'm': 1e6,
    'b': 1e9,
}
"""Suffixes present on RuneScape numbers with their associated multipliers."""


def to_float(rs_price):
    """Convert a RuneScape price string to a normal Python float."""
    try:
        # Attempt to obtain the multiplier for the suffix (the last character).
        multiplier = SUFFIXES[rs_price[-1]]
        # Truncate the price.
        rs_price = rs_price[:-1]
    except KeyError:
        multiplier = 1
    return float(rs_price) * multiplier
