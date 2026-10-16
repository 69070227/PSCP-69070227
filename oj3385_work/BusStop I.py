"""bus stop I"""

def main():
    """dkdkdk"""
    p = int(input())
    stop = int(input())

    bus = []
    all_stop = []
    total = 0

    for _ in range(stop):
        passenger = list(map(int,input().split()))
        all_stop.append(passenger)

        all_stop.sort(key=lambda x: x[0])

    for passenger in all_stop:
        current = passenger[0]
        wait = passenger[1:]
        new = []
        for des in bus:
            if des == current:
                total += 1
            else:
                new.append(des)

            bus = new

        for des in wait:
            if des > current and len(bus) < p:
                bus.append(des)

    print(total)

main()
