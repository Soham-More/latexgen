#include <stdio.h>
#include<math.h>
#include<time.h> 

float x(float t);

float k = 2000 ; // Equivalent spring constant 
float m = 20 ; // Mass of the block
float a = 1 ;// Plug amplitude as 1


int main() 
{
    FILE *file = fopen("values.dat", "w"); //open values.dat to print the data in it
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    float t = 0 ; //current time
    while(t < 7)
    {
        fprintf(file ,"%f \t %e\n", t , x((float)(t)));
        t+= 0.001 ; // find values after every 0.001 seconds
    }   
    return 0 ;
}
float x(float t)
{
    return cos(sqrt(k/m)*t);  // function of x(t)
}
