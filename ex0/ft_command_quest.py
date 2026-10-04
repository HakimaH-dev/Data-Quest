import sys


def ft_command_quest():
    print("=== Command Quest ===")
    print(f"Programe name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Argument received : {len(sys.argv) - 1}")
    i = 1
    while len(sys.argv) > i:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total argument: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
