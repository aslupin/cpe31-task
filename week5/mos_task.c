#include <stdio.h>
main()
{
    char p[10];
    int g,h,j;
    printf("(O)range juice(20 bath)\n");
    printf("(G)rape juice (21 bath)\n");
    printf("(C)occonut juice (22 bath\n)");
    printf("(I)ced juice(18 bath\n)");
    printf("Input your letter do you want to drink: ");
    scanf("%c",p);
    if(p == 'O')
    {
        printf("Input your money: ");
        scanf("%d",&g);
    if(g >=20)
        {
            j=g-20
            printf("Your money enough for drink");
            if(g > 0)
            {
                printf("your change : %d",&j);

            }      
        }
    else 
    { 
        printf("not enough");

    }
    }
    
}