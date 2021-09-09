
#  using a var assigning fstring args
formatter = "{} {} {} {}"
#  printing ints using fstring
print(formatter.format(1, 2, 3, 4))
#  printing strings using fstring
print(formatter.format("one", "two", "three", "four"))
# printing boolean by fstring
print(formatter.format(True, False, False, True))
# as we assign 4 fstrings {} we're printing them as string
print(formatter.format(formatter, formatter, formatter, formatter))
# using fstring {} var we can type our string in new line followed by ,
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
