#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> maps)
{
    const int dx[4] = {-1, 0, 1, 0};
    const int dy[4] = {0, -1, 0, 1};
    
    const int m = maps.size();
    const int n = maps[0].size();
    
    vector<vector<bool>> visit(m, vector<bool>(n, false));
    queue<pair<int, int>> q;
    q.emplace(0, 0);
    
    queue<int> lvl;
    lvl.emplace(1);
    
    while (!q.empty()) {
        auto curr = q.front();
        auto clevel = lvl.front();
        
        q.pop();
        lvl.pop();
        
        for (int i = 0;i < 4;i++) {
            int nx = curr.first + dx[i];
            int ny = curr.second + dy[i];
            
            if (nx == m - 1 && ny == n - 1) return clevel + 1;
            
            if (0 <= nx && nx < m && 0 <= ny && ny < n)
            if (!visit[nx][ny] && maps[nx][ny]) {
            	visit[nx][ny] = true;
            	q.emplace(nx, ny);
                lvl.emplace(clevel + 1);
            }
        }
    }
    
    return -1;
}