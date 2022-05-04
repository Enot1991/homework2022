def load_input():
    result = dict()
    for line in open("input.txt"):
        in_out = line.strip().split(" -> ")
        instr = in_out[0]
        if " " not in instr:
            if instr.isdigit():
                result[in_out[1]] = int(instr)
            else:
                result[in_out[1]] = instr
            continue
        in_wires = instr.split(" ")
        for i, element in enumerate(in_wires):
            if element.isdigit():
                in_wires[i] = int(element)
        result[in_out[1]] = in_wires
    return result



def compute_wire(wire, wires):
    if isinstance(wire, int):
        return wire
    value = wires[wire]
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return compute_wire(value, wires)
    if value[1] == "AND":
        result = compute_wire(value[0], wires) & compute_wire(value[2], wires)
    elif value[1] == "OR":
        result = compute_wire(value[0], wires) | compute_wire(value[2], wires)
    elif value[1] == "LSHIFT":
        result = compute_wire(value[0], wires) << compute_wire(value[2], wires)
    elif value[1] == "RSHIFT":
        result = compute_wire(value[0], wires) >> compute_wire(value[2], wires)
    elif value[0] == "NOT":
        result = ~ compute_wire(value[1], wires)
    else:
        assert False
    wires[wire] = result
    return result



wires = load_input()
result_signal = compute_wire("a", wires)




wires = load_input()
wires["b"] = result_signal
result_signal = compute_wire("a", wires)



f2 = open("output2.txt", "w")
f2.write(str(result_signal))
f2.close
