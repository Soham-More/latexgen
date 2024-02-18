#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    double t, u, y, w;
    
    fp = fopen("data.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    
    fprintf(fp, "Time y1 y2\n");
    
    for (t = -10.0; t <= 10.0; t += 0.1) {
        u = (t >= 0.0) ? 1.0 : 0.0;
        y = u + 2.0 * t * exp(-t) * u - exp(-t) * u;
        w = -u - 4.0 * t * exp(-t) * u + 4* exp(-t) * u;
        fprintf(fp, "%.2f    %.4f    %.4f \n", t, y, w);
    }
    
    fclose(fp);
    
    return 0;
}
