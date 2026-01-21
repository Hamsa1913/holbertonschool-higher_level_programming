try:
    if i > a:
        raise Exception("Too far")
    result += (a ** b) / i
except Exception:
    result = b + a
    break
