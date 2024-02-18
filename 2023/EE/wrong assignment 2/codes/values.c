#include<stdio.h>
#include<stdlib.h> 

float* linspace(float start, float end, int stepNum);
float* f(float* input, int stepNum);

int main(){
    //opening the file
    FILE *fptr=fopen("values.dat", "w");
    //defining the array of x
    float *x=linspace(0.01, 5, 100);
    //defining the array of y : Both positive and negative are taken seperately to avoid div by 0
    float *y_p=f(x, 100);
    float *y_n=f(x, 100);

    //outputting to file
    for(int k=0; k<99; k++){
        y_n[k]=-y_n[k];
        fprintf(fptr, "%f ", y_p[k]);
    }
    y_n[99]=-y_n[99];
    fprintf(fptr, "%f\n", y_p[99]);
    for(int k=0; k<99; k++){
        fprintf(fptr, "%f ", y_n[99-k]);
    }
    fprintf(fptr, "%f", y_n[0]);
    return 0;
}
//creating a linspace function in C 
float* linspace(float start, float end, int stepNum){
    float* array=(float*)malloc(stepNum*sizeof(int));
    float dx= (end-start)/stepNum;
    //Filling the array with evenly-spaced values
    for (int i=0; i<stepNum; i++){
        array[i]=start+dx*i;
    }
    return array;
    free(array);
}
//creating the function 
float* f(float* input, int stepNum){
    float* output=(float*)malloc(stepNum*sizeof(int));
    for(int j=0; j<stepNum; j++){
        //f(x)
        output[j]=-4*input[j]-2/input[j];
    }
    return output;
    free(output);
}