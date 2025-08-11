#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    vector<vector<int>> diff(board.size() + 1, vector<int>(board[0].size() + 1, 0));
    
    for (auto s: skill) {
        int type = s[0];
        int r1 = s[1];
        int c1 = s[2];
        int r2 = s[3];
        int c2 = s[4];
        int power = s[5];
        
        if (type == 1) power = -power;
        
        diff[r1][c1] += power;
        diff[r2 + 1][c2 + 1] += power;
        diff[r1][c2 + 1] -= power;
        diff[r2 + 1][c1] -= power;
    }
    
    for (int r = 0;r < diff.size();r++) {
        for (int c = 1; c < diff[0].size();c++) {
            diff[r][c] += diff[r][c - 1];
        }
    }
    
    for (int c = 0; c < diff[0].size();c++) {
    	for (int r = 1;r < diff.size();r++) {
            diff[r][c] += diff[r - 1][c];
        }
    }
    
    int cnt = board.size() * board[0].size();
    
    for (int r = 0;r < diff.size() - 1;r++) {
        for (int c = 0; c < diff[0].size() - 1;c++) {
            if (diff[r][c] + board[r][c] <= 0) cnt--;
        }
    }
    
    return cnt;
}