#include <stdio.h>

void solve() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n, m, k;
        scanf("%d %d %d", &n, &m, &k);

        int permutation[n];

        // Fill the first part with numbers from n down to n - m + 1
        for (int i = 0; i < n - m; ++i) {
            permutation[i] = n - i;
        }

        for (int i = n - m; i < n; ++i) {
            permutation[i] = i - (n - m) + 1;
        }

        // Output the permutation
        for (int i = 0; i < n; ++i) {
            printf("%d ", permutation[i]);
        }
        printf("\n");
    }
}

int main() {
    solve();
    return 0;
}
