class Solution {
public:
    bool isPalindrome(int x) {
        string str = to_string(x);
        string backwards = "";
        for (int i = str.length() - 1; i >= 0; --i)
        {
            backwards += str[i];
        }
        if (str.compare(backwards) == 0) 
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
