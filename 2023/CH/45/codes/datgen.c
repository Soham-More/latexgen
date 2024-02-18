#include <stdio.h>
#include <math.h>

#define NUM_POINTS 100
#define FILENAME "yt_data.txt"

int main() {
    FILE *fp;
    fp = fopen(FILENAME, "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    double t_values[NUM_POINTS];
    double y_values[NUM_POINTS];
    for (int i = 0; i < NUM_POINTS; i++) {
        t_values[i] = i * 50.0 / (NUM_POINTS - 1);
        y_values[i] = (exp(-t_values[i]/8) / (4 * sqrt(15))) * (9 * sin(sqrt(15) * t_values[i] / 8) - sqrt(15) * cos(sqrt(15) * t_values[i] / 8));
        fprintf(fp, "%.6f %.6f\n", t_values[i], y_values[i]);
    }

    fclose(fp);
    return 0;
}

