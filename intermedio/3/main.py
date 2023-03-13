def tower_of_hanoi(disks=5, first_pole="A", second_pole="B", third_pole="C"):
    if disks == 1:
        print("Mueve el disco 1 de la varilla",
              first_pole, "hacia la varilla", second_pole)
        return
    tower_of_hanoi(disks-1, first_pole, third_pole, second_pole)
    print("Mueve el disco", disks, "de la varilla",
          first_pole, "hacia la varilla", second_pole)
    tower_of_hanoi(disks-1, third_pole, second_pole, first_pole)


if __name__ == "__main__":
    tower_of_hanoi()
