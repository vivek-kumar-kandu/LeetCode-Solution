int  isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return  0 ;
    }
    int original = x;
    long long reverse = 0;
    while (x > 0) {
        int digit = x % 10;
        reverse = reverse * 10 + digit;
        x = x / 10;
    }
    if (original == reverse) {
          return 1;
    } else {
          return 0;
    }
  
}
  
 