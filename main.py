from brute_force import count_occurrences
from compare_dc import common_words_dc
from lcs_dp import lcs_from_texts
import pyfiglet

def main():
    # ASCII art banner using pyfiglet
    banner = pyfiglet.figlet_format("Text Analyzer", font="slant")
    print(banner)
    while True:
        print("Select operation:")
        print("1) Count word occurrences (Brute Force)")
        print("2) Common words (Divide and Conquer)")
        print("3) Longest common subsequence (Dynamic Programming)")
        print("4) Exit")
        choice = input("Choice: ").strip()
        if choice == '1':
            text = input("Paste your text:\n")
            pattern = input("Enter word/pattern to search:\n")
            count = count_occurrences(text, pattern)
            print(f"Occurrences of '{pattern}': {count}")
        elif choice == '2':
            text1 = input("Paste first text:\n")
            text2 = input("Paste second text:\n")
            common = common_words_dc(text1, text2)
            print("Common words:", ", ".join(common))
        elif choice == '3':
            text1 = input("Paste first text:\n")
            text2 = input("Paste second text:\n")
            lcs = lcs_from_texts(text1, text2)
            print("Longest Common Subsequence of words:", " ".join(lcs))
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()