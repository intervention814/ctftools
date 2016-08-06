import sys

'''
Can take something like:

"\x31\xc0" // xorl %eax,%eax
"\x99" // cdq
"\x52" // push edx
"\x68\x2f\x63\x61\x74" // push dword 0x7461632f
"\x68\x2f\x62\x69\x6e" // push dword 0x6e69622f
"\x89\xe3" // mov ebx,esp
"\x52" // push edx
"\x68\x73\x73\x77\x64" // pu sh dword 0x64777373
"\x68\x2f\x2f\x70\x61" // push dword 0x61702f2f
"\x68\x2f\x65\x74\x63" // push dword 0x6374652f
"\x89\xe1" // mov ecx,esp
"\xb0\x0b" // mov $0xb,%al
"\x52" // push edx
"\x51" // push ecx
"\x53" // push ebx
"\x89\xe1" // mov ecx,esp
"\xcd\x80"; // int 80h

and turn it into something like:
\x31\xc0\x99\x52\x68\x2f\x63\x61\x74\x68\x2f\x62\x69\x6e\x89\xe3\x52\x68\x73\x73\x77\x64\x68\x2f\x2f\x70\x61\x68\x2f\x65\x74\x63\x89\xe1\xb0\x0b\x52\x51\x53\x89\xe1\xcd\x80
'''


def convert_to_single_line(shellcode_file):
    """
    Takes a file path containing shellcode in C format (with quotes and newlines and spaces and colons)
    and return a stripped down, command line usable version of shellcode. Very fragile.

    :param shellcode_file: The file containing the shellcode to be stripped.
    :return A command line ready version of the shellcode contained in shellcode_file.
    """
    escaped_shellcode = ""
    with open(shellcode_file, "rb") as file:
        for line in file:
            stripped_line = line.strip()
            for byte in stripped_line:
                if byte == '/':
                    break
                if byte == '\"' or byte == ' ' or byte==';':
                    continue
                escaped_shellcode += byte

    print str(len(escaped_shellcode)/4) + " bytes."
    return escaped_shellcode

if __name__ == "__main__":
    # Supply a file...
    print convert_to_single_line(sys.argv[1])