#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def in_bounds(r, c, n):
    return 0 <= r < n and 0 <= c < n #เช็ค input

def find_king(board): #หา K จากใน input
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                return r, c
    return -1, -1

def check_pawn_attacks(board, kr, kc, pawn_moves_down=True):
    #ดูเบี้ย (P)
    n = len(board)
    if pawn_moves_down:
        target_rows = kr + 1
    else:
        target_rows = kr - 1

    for dc in (-1, 1):
        r = target_rows
        c = kc + dc
        if in_bounds(r, c, n) and board[r][c] == 'P':
            return True

    return False

def check_lines_straight(board, kr, kc):
    n = len(board)
    # ทิศ: ขึ้น, ลง, ซ้าย, ขวา
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        r = kr + dr
        c = kc + dc
        while in_bounds(r, c, n):
            cell = board[r][c]
            if cell != '.':
                # เจอชิ้นแรกในเส้นนี้
                if cell == 'R' or cell == 'Q':
                    return True
                else:
                    # เป็นชิ้นอื่น บังทาง หยุดทิศนี้
                    break
            r += dr
            c += dc

    return False

def check_lines_diagonal(board, kr, kc):
    n = len(board)

    # ทิศ: ซ้ายบน, ขวาบน, ซ้ายล่าง, ขวาล่าง
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        r = kr + dr
        c = kc + dc
        while in_bounds(r, c, n):
            cell = board[r][c]
            if cell != '.':
                if cell == 'B' or cell == 'Q':
                    return True
                else:
                    break
            r += dr
            c += dc

    return False

def is_in_check(board, pawn_moves_down=True):
    # ตรวจบอร์ดว่างหรือบอร์ดไม่ใช่รูปสี่เหลี่ยม
    if not board:
        return False

    n = len(board)
    for row in board:
        if len(row) != n:
            return False

    # หา K
    kr, kc = find_king(board)
    if kr == -1:
        # ไม่พบ K
        return False
    # ตรวจ Pawn
    if check_pawn_attacks(board, kr, kc, pawn_moves_down=pawn_moves_down):
        return True
    # ตรวจ Rook/Queen แนวตรง
    if check_lines_straight(board, kr, kc):
        return True
    # ตรวจ Bishop/Queen แนวทแยง
    if check_lines_diagonal(board, kr, kc):
        return True
    return False

def print_result(board, pawn_moves_down=True):
    if is_in_check(board, pawn_moves_down=pawn_moves_down):
        print("Success")
    else:
        print("Fail")

def parse_board_from_string(board_str):
    lines = []
    for raw in board_str.splitlines():
        line = raw.strip()
        if line != "":
            lines.append(line)
    return lines
