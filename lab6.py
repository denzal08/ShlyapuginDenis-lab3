def is_numder(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
text = input()
print(is_numder(text))