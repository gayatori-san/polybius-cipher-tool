"""Polybius Cipher Tool — simple terminal app."""

from polybius import show_square, show_mappings, encrypt, decrypt, encrypt_with_steps, example


def main() -> None:
    """Run the interactive terminal app."""
    print("=" * 40)
    print("       POLYBIUS CIPHER TOOL")
    print("=" * 40)
    print("Workshop 5x5 grid: A-Y")
    print("Z is not included in the grid.")
    print("Classical cipher - NOT secure for modern use.\n")

    while True:
        print("1. Show Polybius square")
        print("2. Show letter mappings")
        print("3. Encrypt text")
        print("4. Decrypt coordinates")
        print("5. Show encryption steps")
        print("6. Show example")
        print("7. Exit")

        choice = input("\nChoose (1-7): ").strip()

        if choice == "1":
            print("\n" + show_square() + "\n")
        elif choice == "2":
            print("\n" + show_mappings() + "\n")
        elif choice == "3":
            try:
                print("\nEncrypted:", encrypt(input("Enter text: ")), "\n")
            except ValueError as error:
                print("Error:", error, "\n")
        elif choice == "4":
            try:
                print("\nDecrypted:", decrypt(input("Enter coordinates: ")), "\n")
            except ValueError as error:
                print("Error:", error, "\n")
        elif choice == "5":
            try:
                print("\n" + encrypt_with_steps(input("Enter text: ")) + "\n")
            except ValueError as error:
                print("Error:", error, "\n")
        elif choice == "6":
            print("\n" + example() + "\n")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-7.\n")


if __name__ == "__main__":
    main()
