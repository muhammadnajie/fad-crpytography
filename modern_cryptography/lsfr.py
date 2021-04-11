def main():
    iv = list("1111")[::-1]
    output = []
    dummy_pt = "10101010101111"
    for c in range(len(dummy_pt)):
        xor = int(iv[0]) ^ int(iv[3])
        iv.insert(0, str(xor))
        temp = iv.pop()
        output.append(temp)
    output = "".join(output)
    print(output)

main()