#include<stdio.h>
#include<stdlib.h>
#define MAX 10

struct  employee
{
    int empid;
    char name[20];
    int age;
};

struct record
{
    struct employee info;
    struct record *link;
};
void insert(struct employee emprec, struct record *table[]);
int search(int key, struct  record *table[]);
void del(int key,struct record *table[]);
void display(struct record *table[]);
int hash(int key);

main()
{
    struct record *table[MAX];
    struct employee emprec;
    int i,key,choice;
    for (i=0;i <=MAX-1;i++){
        table[i] = NULL;
    }
    while (1)
    {
        printf("1.insert \n");
        printf("2.search \n");
        printf("3.delete \n");
        printf("4.display \n");
        printf("5.exit \n");
        printf("enter your choice \n");
        scanf("%d",&choice);

        switch (choice)
        {
        case 1:
            printf("enter the record\n");
            printf("enter empid,name,age\n");
            scanf("%d%s%d",&emprec.empid,&emprec.name,&emprec.age);
            insert(emprec,table);
            break;
        case 2:
            printf("enter key to be searched\n");
            scanf("%d",&key);
            i = search(key,table);
            if(i==-1)
                printf("key not found\n");
            else
                printf("key found in chain %d\n",i);
            break;
        case 3:
            printf("enter key to be deleted\n");
            scanf("%d",&key);
            del(key,table);
            break;
        case 4:
            display(table);
            break;
        case 5:
            exit(1);
 
        }
    }
}
void insert(struct employee emprec, struct record *table[])
{
    int h ,key;
    struct record *tmp;
    key = emprec.empid;
    if(search(key,table) != -1)
    {
        printf("dublicate key\n");
        return;
    }
    h=hash(key);
    tmp = malloc(sizeof(struct record));
    tmp->info = emprec;
    tmp->link = table[h];
    table[h] = tmp;
}

void display(struct record *table[])
{
    int i ;
    struct record *ptr;
    for(i=0;i<MAX;i++)
    {
        printf("\n[%d] ",i);
        if (table[i]!=NULL)
        {
            ptr = table[i];
            while (ptr!=NULL)
            {
                printf("%d %s %d \t",ptr->info.empid,ptr->info.name,ptr->info.age);
                ptr = ptr->link;
            }
            
        }
    }
}
int search(int key, struct  record *table[])
{
    int h ;
    struct record *ptr;
    h = hash(key);
    ptr = table[h];
    while (ptr!=NULL)
    {
        if (ptr->info.empid == key)
            return h;
        ptr = ptr->link;

    }
    return -1;
}
void del(int key,struct record *table[])
{
    int h; 
    struct record *tmp,*ptr;
    h = hash(key);
    if (table[h] == NULL)
    {
        printf("key %d not found\n",key);
        return;
    }
    if (table[h]->info.empid == key)
    {
        tmp = table[h];
        table[h] = table[h]->link;
        free(tmp);
        return;
    }
    ptr = table[h];

    while (ptr->link != NULL)
    {
        if(ptr->link->info.empid == key)
        {
            tmp = ptr->link;
            ptr->link = tmp->link;
            free(tmp);
            return;
        }
        ptr = ptr->link;
    }
    printf("key %d do not found\n",key);
}

int hash(int key)
{
    return(key%MAX);
}