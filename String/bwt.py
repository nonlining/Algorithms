# python3
import sys

def BWT(text):
    n = len(text)
    m = []
    for i in range(n):
        m.append(text[-i:]+text[:-i])
    sorted_m = sorted(m)

    return "".join(s[-1] for s in sorted_m)


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    #text = "AGACATA$"
    # AAAC$CGAAAAAAAACCCCAAGA
    print(BWT(text))