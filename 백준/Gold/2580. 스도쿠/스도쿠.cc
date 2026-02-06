#include <iostream>
#include <vector>
using namespace std;
#define N 9

bool solve_sudoku(int sudoku[N][N], vector<pair<int, int> > &blanks, int blank_idx) {
    if (blank_idx == blanks.size()) return true;
    for (int i = 1; i <= 9; ++i) {
        auto blank = blanks[blank_idx];
        bool flag = true;
        for (int j = 0; j < N; ++j) {
            int x = ((int) (blank.first / 3)) * 3 + j / 3;
            int y = ((int) (blank.second / 3)) * 3 + j % 3;
            if (sudoku[blank.first][j] == i || sudoku[j][blank.second] == i ||
                sudoku[x][y] == i) {
                flag = false;
                break;
            }
        }
        if (!flag) continue;

        sudoku[blank.first][blank.second] = i;
        if (solve_sudoku(sudoku, blanks, blank_idx + 1)) return true;
        sudoku[blank.first][blank.second] = 0;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int sudoku[N][N] = {0,};
    vector<pair<int, int> > blanks;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> sudoku[i][j];
            if (sudoku[i][j] == 0) blanks.emplace_back(i, j);
        }
    }

    solve_sudoku(sudoku, blanks, 0);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << sudoku[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}
