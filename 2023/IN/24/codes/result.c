#include <stdio.h>
#include <math.h>

// Function to calculate Routh array for an nth order polynomial
void calculateRouthArray(double coefficients[], int order, double routh[][order / 2 + order % 2 + 1]) {
    int i, j, k = 0;

    // Initialize the first two rows of the Routh array
    for (i = 0; i < order && k < order + 1; i++) {
        routh[0][i] = coefficients[k];
        k += 2;
    }
     routh[0][order / 2 + order % 2] = 0.0; 

    k = 1; // Reset k for the second row
    for (i = 0; i < order && k < order + 1; i++) {
        routh[1][i] = coefficients[k];
        k += 2;
    }
     routh[1][order / 2 + order % 2] = 0.0; 

    // Calculate the rest of the Routh array
    for (i = 2; i < order; i++) {
        for (j = 0; j < order / 2 + order % 2; j++) {
            routh[i][j] = ((routh[i - 1][0] * routh[i - 2][j + 1]) - (routh[i - 2][0] * routh[i - 1][j + 1])) / routh[i - 1][0];
        }
        routh[i][order / 2 + order % 2] = 0.0; 
    }
}

int main() {
    double coefficients[4] = {1, 2, 5, 80}; // coefficients of the polynomial
    int order = 4;
    double routh[4][order / 2 + order % 2 + 1];

    // Call the function to calculate the Routh array
    calculateRouthArray(coefficients, order, routh);

    // Open a file for writing
    FILE *file = fopen("routh_output.txt", "w");

    if (file == NULL) {
        fprintf(stderr, "Error opening file for writing.\n");
        return 1; // Exit with an error code
    }

    // Print the Routh array to the file
    fprintf(file, "Routh array:\n");
    for (int i = 0; i < order; i++) {
        for (int j = 0; j < order / 2 + order % 2 + 1; j++) {
            fprintf(file, "%10.4lf  ", routh[i][j]);
        }
        fprintf(file, "\n");
    }

    // Count the number of sign changes in the first column
    int sign_changes = 0;
    double prev_sign = routh[0][0] >= 0 ? 1 : -1;
    for (int i = 1; i < order; i++) {
        double curr_sign = routh[i][0] >= 0 ? 1 : -1;
        if (curr_sign != prev_sign) {
            sign_changes++;
        }
        prev_sign = curr_sign;
    }

    // Print the number of sign changes to the file
    fprintf(file, "Number of zeros in the right half of the s-plane: %d\n", sign_changes);

    // Close the file
    fclose(file);

    return 0;
}
