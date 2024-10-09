unfold_vert = [2, 3, 0, 1]
unfold_hori = [1, 0, 3, 2]
unfold_diag = [3, 2, 1, 0]

def solve(k, tasks, hole):
    col_start, col_end = 1, 2 ** k
    row_start, row_end = 1, 2 ** k

    for task in tasks:
        half_width = int((col_end - col_start + 1)/2)
        half_height = int((row_end - row_start + 1)/2)

        if task == 'U': row_end -= half_height
        elif task == 'L': col_end -= half_width 
        elif task == 'D': row_start += half_height
        elif task == 'R': col_start += half_width 

    row, col = row_end, col_end
    vert, hori, diag = unfold_vert[hole], unfold_hori[hole], unfold_diag[hole]

    arr = [] 
    if row % 2 == 0 and col % 2 == 0: arr = [[diag, vert], [hori, hole]]
    elif row % 2 == 0 and col % 2 == 1: arr = [[vert, diag], [hole, hori]]
    elif row % 2 == 1 and col % 2 == 0: arr = [[hori, hole], [diag, vert]]
    elif row % 2 == 1 and col % 2 == 1: arr = [[hole, hori], [vert, diag]]


    for i in range(2**k):
        print(*(arr[i & 1] * (2**(k-1))))



if __name__ == "__main__":
    k = int(input())
    tasks = input().split()
    hole = int(input())

    solve(k, tasks, hole)
