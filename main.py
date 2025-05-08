from brute_force import count_occurrences
from compare_dc import common_words_dc
from lcs_dp import lcs_from_texts
from string_algo import kmp_search_positions, jump_search_in_text
from utils import tokenize
import pyfiglet

def main():
    # ASCII art banner using pyfiglet
    banner = pyfiglet.figlet_format("LexiCLI", font="slant")
    print(banner)
    while True:
        print("Select operation:")
        print("1) Count word occurrences (Brute Force)")
        print("2) Common words (Divide and Conquer)")
        print("3) Longest common subsequence (Dynamic Programming)")
        print("4) Locate pattern positions (String Algorithm - Knuth-Morris-Pratt)")
        print("5) Find token index (Jump Search)")
        print("6) Exit")
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
            text = input("Paste your text:\n")
            pattern = input("Enter pattern to locate (KMP):\n")
            positions = kmp_search_positions(text, pattern)
            if positions:
                print(f"Pattern '{pattern}' found at positions: {positions}")
            else:
                print(f"Pattern '{pattern}' not found.")
        elif choice == '5':
            text = input("Paste your text:\n")
            # Show sorted tokens for jump search
            tokens = sorted(tokenize(text))
            print("Sorted tokens:", tokens)
            key = input("Enter word to find index (Jump Search):\n")
            idx = jump_search_in_text(text, key)
            if idx != -1:
                print(f"Index of '{key}': {idx}")
            else:
                print(f"'{key}' not found.")
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()