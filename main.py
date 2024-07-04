import os

amount_disks: int = int(input("Quantos discos você quer? "))


def color_text(text: str, number: int) -> tuple[str, int]:
    escape_sequence = f"\033[38;5;{number%99 + 1}m"

    colored_text = f"{escape_sequence}{text}\033[0m"
    return (colored_text, len(escape_sequence) + 4)

def show_stacks(stacks: list[list, list, list]) -> None:
    os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal
    
    space_to_center = amount_disks * 2 + 1
    
    print(("1".center(space_to_center) + " ") + ("2".center(space_to_center) + " ") + ("3".center(space_to_center) + " "))
    
    for height in range(amount_disks - 1, -1, -1):
        for stack in stacks:
            if len(stack) - 1 < height:
                print("|".center(space_to_center), end="")
            else:
                disk: str = "█"*stack[height]*2 + "█"
                disk, added_char = color_text(disk, stack[height])
                print(disk.center(space_to_center + added_char), end="")
            print(" ", end="")
        print()

def handle_input(stacks: list[list, list, list]) -> None:
    while True:
        try:
            source, destination = [int(stack) - 1 for stack in input().split()]
            break
        except ValueError:
            pass
    if len(stacks[destination]) == 0:
        stacks[destination].append(stacks[source].pop())
    elif stacks[source][len(stacks[source]) - 1] > stacks[destination][len(stacks[destination]) - 1]:
        pass
    else:
        stacks[destination].append(stacks[source].pop())

if __name__ == "__main__":
    winning_example: list = [disk for disk in range(amount_disks)]
    stacks: list[list, list, list] = [[disk for disk in range(amount_disks)], [], []] # make the stack, no mess
    stacks[0].reverse()
    winning_example.reverse()
    
    # + 6 -> spaces
    # + 3 -> numbers on top, input, victory
    os.system(f"mode con: cols={amount_disks * 6 + 6} lines={amount_disks + 3}")
    
    show_stacks(stacks)
    while True:
        handle_input(stacks)
        show_stacks(stacks)
        if stacks[1] == winning_example or stacks[2] == winning_example:
            print("Vitória :D")
            break
    input()
    exit()