#!/usr/bin/env python3
import checkmate

def main():
    board1 = [
        "R...",
        ".K..",
        "..P.",
        "....",
    ]
    # ตั้งให้เบี้ยอยู่ด้านล่าง
    checkmate.print_result(board1, pawn_moves_down=True)

    board2 = [
        "....",
        ".K..",
        "....",
        "..R.",
    ]
    checkmate.print_result(board2, pawn_moves_down=True)

    #ลองทำ string หลายบรรทัด
    s = """
    .....
    ..K..
    .....
    ..Q..
    .....
    """
    board3 = checkmate.parse_board_from_string(s)
    checkmate.print_result(board3, pawn_moves_down=True)
main()