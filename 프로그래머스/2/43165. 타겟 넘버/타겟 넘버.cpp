#include <string>
#include <vector>

using namespace std;

int answer = 0;

void sum_up(int acc, const vector<int>& numbers, int idx, int target) {
    if (idx >= numbers.size()) {
        if (acc == target) answer++;
        return;
    }
    
    sum_up(acc + numbers[idx], numbers, idx + 1, target);
    sum_up(acc - numbers[idx], numbers, idx + 1, target);
}

int solution(vector<int> numbers, int target) {
    sum_up(0, numbers, 0, target);
    
    return answer;
}