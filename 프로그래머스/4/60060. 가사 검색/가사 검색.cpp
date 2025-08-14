#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <memory>

using namespace std;

struct Trie {
    int cnt;
    struct Trie* next[26];

    Trie() {
        cnt = 0;
        fill_n(next, 26, nullptr);
    }

    ~Trie() {
        for (int i = 0;i < 26;i++) {
            delete next[i];
        }
    }
    
    void insert(const string& c) {
        struct Trie* iter = this;
        iter->cnt++;

        for (int i = 0;i < c.size();i++) {
            if (!iter->next[c[i] - 'a']) {
                iter->next[c[i] - 'a'] = new Trie();
            }

            iter = iter->next[c[i] - 'a'];
            iter->cnt++;
        }
    }

    int count(const string& s) {
        struct Trie* iter = this;
        int idx = 0;
        
        while (s[idx] != '?') {
            iter = iter->next[s[idx] - 'a'];
            if (iter == nullptr) return 0;
            idx++;
        }
        
        return iter->cnt;
    }
};

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    unordered_map<string, int> result_cache;
    unordered_map<int, unique_ptr<struct Trie>> fwd, bwd;

    for (auto word: words) {
        string rev = word;
        reverse(rev.begin(), rev.end());
        
        if (!fwd[word.size()]) fwd[word.size()] = make_unique<Trie>();
        if (!bwd[word.size()]) bwd[word.size()] = make_unique<Trie>();

        fwd[word.size()]->insert(word);
        bwd[word.size()]->insert(rev);
    }

    for (auto query: queries) {
        int cnt = 0;
        
        auto find = result_cache.find(query);
        
        if (find != result_cache.end()) {
            answer.push_back(find->second);
            continue;
        }
        
        if (query[0] == '?') {
            string rev = query;
            reverse(rev.begin(), rev.end());
            
        	if (bwd.find(query.size()) != bwd.end())
            	cnt = bwd[query.size()]->count(rev);
        } else {
        	if (fwd.find(query.size()) != fwd.end())
            	cnt = fwd[query.size()]->count(query);
        }
        
        result_cache[query] = cnt;
        answer.push_back(cnt);
    }

    return answer;
}
