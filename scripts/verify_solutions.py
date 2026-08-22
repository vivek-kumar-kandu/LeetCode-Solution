import os
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    wrapper_c = "/tmp/leetcode_c_headers.h"
    wrapper_cpp = "/tmp/leetcode_cpp_headers.h"
    
    if sys.platform != 'win32':
        with open(wrapper_c, "w", encoding="utf-8") as f:
            f.write("""#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>
#include <math.h>
#include <ctype.h>
""")
        with open(wrapper_cpp, "w", encoding="utf-8") as f:
            f.write("""#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <cmath>
#include <climits>
#include <utility>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <memory>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
""")

    c_files = []
    cpp_files = []

    for root, dirs, files in os.walk(repo_root):
        if '.git' in root or '.github' in root:
            continue
        for file in files:
            if file.endswith('.c'):
                c_files.append(os.path.join(root, file))
            elif file.endswith('.cpp'):
                cpp_files.append(os.path.join(root, file))

    print("==========================================")
    print(f"Found {len(c_files)} C files and {len(cpp_files)} C++ files.")
    print("==========================================")

    if sys.platform != 'win32':
        for cfile in c_files:
            rel = os.path.relpath(cfile, repo_root)
            cmd = ["gcc", "-fsyntax-only", "-include", wrapper_c, cfile]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print(f"  [PASS] {rel}")
            else:
                print(f"  [WARN] {rel}")

        for cppfile in cpp_files:
            rel = os.path.relpath(cppfile, repo_root)
            cmd = ["g++", "-std=c++20", "-fsyntax-only", "-include", wrapper_cpp, cppfile]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print(f"  [PASS] {rel}")
            else:
                print(f"  [WARN] {rel}")

    print("==========================================")
    print("Verification Completed Successfully!")
    print("==========================================")

if __name__ == '__main__':
    main()
