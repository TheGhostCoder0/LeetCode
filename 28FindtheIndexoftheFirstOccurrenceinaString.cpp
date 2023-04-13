class Solution {
public:
    int strStr(string haystack, string needle) {
        auto index = haystack.find(needle);
        if (index == string::npos)
            index = -1;
        return index;
    }
};
