class Solution {
public:
    bool isPalindrome(string s) {
        string str;
        for (size_t i = 0; i < s.length(); i++)
        {
            if (isalnum(s[i]))
            {
                str.push_back(tolower(s[i]));
            }
        }
        if (str.empty())
        {
            return true;
        }
        for (size_t i = 0, j = str.length() - 1; i < j; i++, j--)
        {
            if (str[i] != str[j])
            {
                return false;
            }   
        }
        return true;
    }
};
