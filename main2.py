def detect_and_convert(value):
    val = value.strip()
    if val.lower() in ["true", "false"]:
        return (val.lower() == "true"), "bool"
    try:
        int_val = int(val)
        return int_val, "int"
    except ValueError:
        pass
    try:
        float_val = float(val)
        return float_val, "float"
    except ValueError:
        pass
    return val, "str"

print("Enter values (press Enter on empty line to finish):")

values = []  

while True:
    inp = input("> ")
    if inp == "":
        break
    converted, inferred_type = detect_and_convert(inp)
    values.append((inp, inferred_type, converted))

print("summary table")
print(f"{'Original':<15} {'Inferred Type':<15} {'Converted Value':<15}")
print("-" * 45)
for original, inferred_type, converted in values:
    print(f"{original:<15} {inferred_type:<15} {str(converted):<15}")
