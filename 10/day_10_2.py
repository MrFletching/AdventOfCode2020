#!/usr/bin/env python3

def main():
    adapters = read_adapters('input.txt')
    adapters.sort()

    built_in_adapter = adapters[-1] + 3
    adapters.append(built_in_adapter)

    adapter_arrangements = {0: 1}

    for adapter in adapters:

        adapter_arrangements[adapter] = 0

        for i in range(3):
            prev_adapter = adapter - i - 1
            if prev_adapter in adapter_arrangements:
                adapter_arrangements[adapter] += adapter_arrangements[prev_adapter]

    arrangements = adapter_arrangements[built_in_adapter]

    print(f'Arrangements: {arrangements}')



def read_adapters(filename):
    with open(filename) as f:
        return [int(l) for l in f]


if __name__ == '__main__':
    main()
