class Solution {
public:
    char findTheDifference(string s, string t) {
        for (size_t i = 0; i < s.length(); i++)
        {
            string str = string(1, s[i]);
            size_t index = t.find(str);
            t[index] = '0';
        }
        for (size_t i = 0; i < t.length(); i++)
        {
            if (isdigit(t[i]))
            {
                continue;
            }
            else
            {
                return t[i];
            }
        }
        return '0';
    }
};
