import sys

def hexdump(buffer:bytes, size:int):
    for i in range(0, size, 16):
        print(f'{i:08X} |', end='')
        for j in range(0, 16):
            if i + j < size:
                print(f' {buffer[i + j]:02X}', end='')
            else:
                print(' 00', end='')
        
        print(' | ', end='') # splitter

        for j in range(0, 16):
            if i + j < size:
                k = buffer[i + j]
                c = '.' if k < 32 or k > 127 else chr(k)

                print(c, end='')
            else:
                print(' ', end='')
        
        print('')

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} [FileName]')
        return
    
    with open(sys.argv[1], 'rb') as f:
        buffer = f.read()
        hexdump(buffer, len(buffer))

if __name__ == '__main__':
    main()