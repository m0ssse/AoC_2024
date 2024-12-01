#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <map>

using namespace std;

int main() {
    vector<int> nums1;
    vector<int> nums2;
    string line;
    map<int, int> nums2_counts;
    ifstream f("input1.txt");
    while (getline(f, line)) {
        stringstream nums(line);
        int x, y;
        nums >> x >> y;
        nums1.push_back(x);
        nums2.push_back(y);
        nums2_counts[y]++;
    }
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    int res1 = 0;
    int res2 = 0;
    int n = nums1.size();
    for (int i=0; i<n; i++) {
        res1+=abs(nums1[i]-nums2[i]);
        res2+=nums1[i]*nums2_counts[nums1[i]];
    }
    cout << res1 << "\n" << res2;
}