"""Polybius Cipher Tool — a simple terminal app for classical encryption."""

from polybius import show_square, show_mappings, encrypt, decrypt, encrypt_with_steps, example


def print_banner() -> None:
    """Print the app banner."""
    print("=" * 40)
    print("       POLYBIUS CIPHER TOOL")
    print("=" * 40)
    print("NOTE: This is a classical cipher and")
    print("is NOT secure for modern use.\n")


def print_menu() -> None:
    """Print the menu options."""
    print("Options:")
    print("  1. Show the Polybius square")
    print("  2. Show letter mappings")
    print("  3. Encrypt text")
    print("  4. Decrypt coordinates")
    print("  5. Show encryption steps")
    print("  6. Show a simple example")
    print("  7. Quit")


def handle_square() -> None:
    print("\n--- Polybius Square ---")
    print(show_square())
    print()


def handle_mappings() -> None:
    print("\n--- Letter Mappings ---")
    print(show_mappings())
    print()


def handle_encrypt() -> None:
    text = input("Enter text to encrypt: ")
    print(f"\n  Encrypted: {encrypt(text)}\n")


def handle_decrypt() -> None:
    text = input("Enter coordinates to decrypt: ")
    print(f"\n  Decrypted: {decrypt(text)}\n")


def handle_steps() -> None:
    text = input("Enter text to see encryption steps: ")
    print("\n--- Encryption Steps ---")
    print(encrypt_with_steps(text))
    print()


def handle_example() -> None:
    print("\n--- Example ---")
    print(example())
    print()


def main() -> None:
    """Run the interactive terminal app."""
    print_banner()
    handlers = {
        "1": handle_square,
        "2": handle_mappings,
        "3": handle_encrypt,
        "4": handle_decrypt,
        "5": handle_steps,
        "6": handle_example,
    }

    while True:
        print_menu()
        choice = input("Choose (1-7): ").strip()
        if choice == "7":
            print("Goodbye!")
            break
        handler = handlers.get(choice)
        if handler:
            handler()
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
