class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<int>> mp;
        for (int i = 0; i < strs.size(); i++) {
            string t = strs[i];
            sort(t.begin(), t.end());
            mp[t].push_back(i);
        }
        vector<vector<string>> res;
        for (auto it : mp) {
            vector<string> st;
            vector<int> idxs = it.second;
            for (auto idx : idxs) {
                st.push_back(strs[idx]);
            }
            res.push_back(st);
        }
        return res;
    }
 };
