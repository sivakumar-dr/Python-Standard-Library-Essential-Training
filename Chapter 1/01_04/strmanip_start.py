# Working with string manipulation functions

test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"

# TODO: upper and lower convert between cases
print(test_string1.capitalize())
print(test_string1.upper())
print(test_string1.lower())

# TODO: Use the split and join functions
print(" ".join(test_string1.split(" ")))

# TODO: use justification functions to align strings
# ljust, center, rjust
names = ["Amy", "John", "George", "Michael", "Penelope"]
biggest = max(len(name) for name in names)

# TODO: Use a translation table to replace characters
sample_str = "The quick brown fox jumped over the lazy dog"
