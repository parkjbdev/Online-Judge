#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int main(void)
{
    int N, M;
    cin >> N >> M;

    int x, y;
    char MAP[50][50] = {0};

    for (int i = 0; i < N; i++)
    {
        cin >> MAP[i];
        for (int j = 0; j < M; j++)
        {
            if (MAP[i][j] == '0')
            {
                x = i;
                y = j;
                MAP[i][j] = '.';
            }
        }
    }

    const int DXs[4] = {-1, 1, 0, 0};
    const int DYs[4] = {0, 0, -1, 1};

    bool visited[50][50][0b1000000] = {0};
    visited[x][y][0] = true;

    typedef tuple<int, int, int, int> qelem;
    queue<qelem> q;
    q.push(make_tuple(x, y, 0, 0));

    while (!q.empty())
    {
        qelem now = q.front();

        int x = get<0>(now);
        int y = get<1>(now);
        int keys = get<2>(now);
        int level = get<3>(now);

        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + DXs[i];
            int ny = y + DYs[i];

            if (!(0 <= nx && nx < N && 0 <= ny && ny < M))
                continue;

            if (visited[nx][ny][keys] or MAP[nx][ny] == '#')
                continue;

            else if (MAP[nx][ny] == '1')
            {
                x = nx;
                y = ny;
                cout << level + 1 << endl;
                return 0;
            }
            if (MAP[nx][ny] == '.' && !visited[nx][ny][keys])
            {
                visited[nx][ny][keys] = true;
                q.push(make_tuple(nx, ny, keys, level + 1));
            }
            else if ('A' <= MAP[nx][ny] && MAP[nx][ny] <= 'Z')
            {
                if ((keys & (1 << (MAP[nx][ny] - 'A'))) != 0 && !visited[nx][ny][keys])
                {
                    visited[nx][ny][keys] = true;
                    q.push(make_tuple(nx, ny, keys, level + 1));
                }
            }
            else if ('a' <= MAP[nx][ny] && MAP[nx][ny] <= 'z')
            {
                int tmp_keys = keys | (1 << (MAP[nx][ny] - 'a'));
                if (!visited[nx][ny][keys])
                {
                    visited[nx][ny][tmp_keys] = true;
                    q.push(make_tuple(nx, ny, tmp_keys, level + 1));
                }
            }
        }
    }

    cout << -1 << endl;

    return 0;
}
