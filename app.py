def calculate(a, b, operation):
    if operation == "add": return a + b
    if operation == "subtract": return a - b
    if operation == "multiply": return a * b
    if operation == "divide": return a / b  # no zero check

def process_users(users):
    result = []
    for u in users:
        result.append(u["name"].upper())
    return result  # no key check

def save_data(data, filename):
    f = open(filename, "w")
    f.write(str(data))  # file never closed