#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <deque>

using namespace std;
using Graph = unordered_map<string, deque<string>>;

vector<string> answer;

bool dfs(Graph& adj, string airport, int lvl, int ticket_max) {
    answer.push_back(airport);
    
    if (lvl >= ticket_max) return true;
    
    int max_tries = adj[airport].size();
    int tries = 0;
    
    while (!adj[airport].empty() && tries < max_tries) {
        tries++;
    	string next_airport = adj[airport].front();
    	adj[airport].pop_front();
    	bool res = dfs(adj, next_airport, lvl + 1, ticket_max);
        if (res) return true;
        adj[airport].push_back(next_airport);
    }
    
    answer.pop_back();
    
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    Graph adj;
    
    for (int i = 0;i < tickets.size();i++) {
        auto &ticket = tickets[i];
        adj[ticket[0]].push_back(ticket[1]);
    }
    
    for (auto &[key, val]: adj) {
        sort(adj[key].begin(), adj[key].end());
    }
    
    bool ret = dfs(adj, "ICN", 0, tickets.size());
    
    return answer;
}