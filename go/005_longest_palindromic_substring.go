package main

import (
    "fmt"
)

func longestPalindrome(s string) string {
    if len(s) == 1 {
        return s
    }

    start, end, maxLen := 0, 0, 0

    for i := 0; i < len(s); i++ {
        maxLen = max(
            expand(s, i, i),
            expand(s, i, i + 1),
            )
        if maxLen > end - start {
            start = i - (maxLen - 1) / 2
            end = i + maxLen / 2
        }
    }

    return s[start:end + 1]
}

func expand(s string, left int, right int) int {
    L, R := left, right
    for L >= 0 && R < len(s) && s[L] == s[R] {
        L -= 1
        R += 1
    }
    return R - L - 1
}

func main() {
    fmt.Println(longestPalindrome("babad"))
}
