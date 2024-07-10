#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> elements;

public:
    void set(string key, string value, int timestamp) {
        elements[key].push_back({timestamp, value});
    }

    string get(string key, int timestamp) {
        if (elements.find(key) == elements.end()) {
            return "";
        }

        auto& pairs = elements[key];

        auto it = upper_bound(pairs.begin(), pairs.end(), timestamp,
                              [](int ts, const pair<int, string>& p) {
                                  return ts < p.first;
                              });

        if (it == pairs.begin()) {
            return "";
        }

        return prev(it)->second;
    }
};
