#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer(enroll.size(), 0);
    vector<int> parents(referral.size(), 0);
    
    unordered_map<string, int> idmap;
    idmap["-"] = -1;
    
    for (int i = 0;i < enroll.size();i++) {
        idmap[enroll[i]] = i;
    }
    
    for (int i = 0;i < referral.size();i++) {
        parents[i] = idmap[referral[i]];
    }
    
    for (int i = 0;i < seller.size();i++) {
        int a = amount[i] * 100;
        int s = idmap[seller[i]];
        
        while (s >= 0) {
        	int parent_amount = a / 10;
            
            answer[s] += (a - parent_amount);
            
            a = parent_amount;
            s = parents[s];
        }
    }
    
    return answer;
}