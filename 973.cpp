#include <vector>
#include <cmath>
#include <algorithm>

class Solution {
public:
    int distance(std::vector<int>& point) {
        return point[0] * point[0] + point[1] * point[1];
    }

    std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int k) {
        for (int i = 0; i < points.size(); ++i) {
            points[i].push_back(distance(points[i]));
        }

        for (int i = 0; i < points.size() - 1; ++i) {
            int j = i + 1;
            while (j > 0) {
                if (points[j - 1][2] > points[j][2]) {
                    std::swap(points[j - 1], points[j]);
                } else {
                    break;
                }
                j--;
            }
        }

        std::vector<std::vector<int>> res;
        for (int i = 0; i < k; ++i) {
            res.push_back({points[i][0], points[i][1]});
        }
        return res;
    }
};
