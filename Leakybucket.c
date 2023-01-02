#include<stdio.h>

void main()
{
    int bucketSize = 60;
    int inputRate = 0;
    int outputRate = 0;
    int remainingSize = 0;
    int dataPresent = -1;

    printf("\n Enter the size of the bucket : ");
    scanf("%d",&bucketSize);

    printf("\n Enter the output flow rate : ");
    scanf("%d",&outputRate);

    while(1)
    {
        printf("\n Do you have any data packets? (1 or 0): ");
        scanf("%d",&dataPresent);

        if(dataPresent == 1)
        {
            printf("\n Enter the input data flow rate : ");
            scanf("%d",&inputRate);

            if((remainingSize + inputRate) <= bucketSize)
            {
                remainingSize += inputRate;

                printf("\n The present size of bucket (before output flow) : %d",remainingSize);
                remainingSize -= outputRate;
                printf("\n The present size of bucket now : %d\n",remainingSize);
            }
            else
            {
                printf("\n Bucket is Full!!!!!!! Cannot accept the input!!!");
                printf("\n The present size of bucket now : %d\n",remainingSize);

            }
        }

        else
        {
            printf("\n The present size of bucket (before output flow) : %d",remainingSize);
            remainingSize -= outputRate;
            printf("\n The present size of bucket now : %d\n",remainingSize);
        }
    }
}
