
#include <stdio.h>

int main()
{
    FILE *fp = fopen("data.dat", "w");
    int a = 0;
    for (int i= -8; i<10; i++){
        if(i!=9){
            fprintf(fp, "%d ",i);
            }
        else{
            fprintf(fp, "%d",i);
        }
    }
    fclose(fp);
    

}

