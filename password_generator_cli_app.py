import string
import random

class PasswordGenerator:
    def __init__(self, length=8, use_digits=True, use_symbols=True, use_uppercase=True, use_lowercase=True):
        self.length = length
        self.use_digits = use_digits
        self.use_symbols = use_symbols
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase

    def get_charset(self):
        charset = ""
        if self.use_digits:
            charset += string.digits
        if self.use_symbols:
            charset += string.punctuation
        if self.use_uppercase:
            charset += string.ascii_uppercase
        if self.use_lowercase:
            charset += string.ascii_lowercase
        return charset

    def generate(self):
        charset = self.get_charset()
        if not charset:
            raise ValueError("❌ No characters selected to generate password!")
        return "".join(random.choice(charset) for _ in range(self.length))


class FileHandler:
    @staticmethod
    def save(password, filename="passwords.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(password + "\n")
        print(f"💾 Password saved to {filename}.")

    @staticmethod
    def load(filename="passwords.txt"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print("⚠️ No file found.")
            return []


class PasswordCLI:
    def __init__(self):
        self.generator = None

    def show_menu(self):
        print("\n🔐 Password Generator CLI")
        print("1️⃣ Generate a new password")
        print("2️⃣ View saved passwords")
        print("3️⃣ Exit")

    def get_user_input(self):
        length = int(input("📏 Password length: "))
        use_digits = input("Use digits? (y/n): ").lower() == "y"
        use_symbols = input("Use symbols? (y/n): ").lower() == "y"
        use_uppercase = input("Use uppercase letters? (y/n): ").lower() == "y"
        use_lowercase = input("Use lowercase letters? (y/n): ").lower() == "y"

        self.generator = PasswordGenerator(
            length, use_digits, use_symbols, use_uppercase, use_lowercase
        )

    def run(self):
        while True:
            self.show_menu()
            choice = input("👉 Choose an option: ")

            if choice == "1":
                self.get_user_input()
                try:
                    password = self.generator.generate()
                    print(f"✅ Password generated: {password}")
                    if input("Do you want to save it? (y/n): ").lower() == "y":
                        FileHandler.save(password)
                except ValueError as e:
                    print(e)

            elif choice == "2":
                passwords = FileHandler.load()
                if passwords:
                    print("📂 Saved passwords:")
                    for idx, p in enumerate(passwords, 1):
                        print(f"{idx}. {p}")

            elif choice == "3":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice")


if __name__ == "__main__":
    PasswordCLI().run()
