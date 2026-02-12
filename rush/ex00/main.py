from checkmate import checkmate

def main():
    print("--- Example 1 (Original) ---")
    board1 = """\
R...
.K..
..P.
....\
"""
    print(checkmate(board1))

    print("\n--- Example 2 (Original) ---")
    board2 = """\
..
.K\
"""
    print(checkmate(board2))

if __name__ == "__main__":
    main()
