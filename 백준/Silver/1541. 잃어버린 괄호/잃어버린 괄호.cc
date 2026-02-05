#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string input;
    cin >> input;

    int result = 0;
    int mult = input[0] == '-' ? -1 : 1;

    for (int i = 0; i < input.length(); ++i) {
        int parse_int = 0, parse_len = 0;

        while (i + parse_len < input.length() && (
                   input[i + parse_len] != '+' &&
                   input[i + parse_len] != '-')
        )
            parse_len++;

        for (int j = i; j < i + parse_len; j++) {
            parse_int += ((input[j] - '0') * static_cast<int>(pow(
                              10, i + parse_len - j - 1)));
        }

        result += mult * parse_int;

        if (mult > 0 && i + parse_len < input.length()) {
            mult = input[i + parse_len] == '-' ? -1 : 1;
        }

        i += parse_len;
    }

    cout << result << endl;

    return 0;
}
