def checkmate(board: str):
    try:
        lines = board.splitlines()

        if not lines:
            return None

        size = len(lines)

        for line in lines:
            if len(line) != size:
                return None

        king_count = 0
        king_pos = None

        for r in range(size):
            for c in range(size):
                if lines[r][c] == 'K':
                    king_count += 1
                    king_pos = (r, c)

        if king_count != 1:
            return None

        kr, kc = king_pos

        def check_direction(dr, dc, valid_pieces):
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                piece = lines[r][c]
                if piece != '.':
                    if piece in valid_pieces:
                        return True
                    return False
                r += dr
                c += dc
            return False

        # Pawn
        for dr, dc in [(1, -1), (1, 1)]:
            r, c = kr + dr, kc + dc
            if 0 <= r < size and 0 <= c < size:
                if lines[r][c] == 'P':
                    return "Success"

        # Rook / Queen
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if check_direction(dr, dc, {'R', 'Q'}):
                return "Success"

        # Bishop / Queen
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if check_direction(dr, dc, {'B', 'Q'}):
                return "Success"

        return "Fail"

    except Exception:
        return None
