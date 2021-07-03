////c++ code to implement complex functions using class

// #include<iostream>
// using namespace std;
// class complex
// {
//     public:
//     int a , b;
//     void getdata()
//     {
//         cin>>a>>b;
//     }
//     void display()
//     {
//         cout<<a<<"+"<<b<<"i"<<endl;
//     }
//     void sum(complex c1,complex c2)
//     {
//         a = c1.a + c2.a;
//         b = c1.b + c2.b;
//     }
//     void mult(complex c1,complex c2)
//     {
//         a = c1.a*c2.a - c1.b*c2.b;
//         b = c1.a*c2.b + c1.b*c2.a;
//     }
// };

// int main()
// {
//     complex c1,c2,c3,c4;
//     cout<<"enter nos"<<endl;
//     c1.getdata();
//     cout<<"enter nos"<<endl;
//     c2.getdata();
//     cout<<"sum is"<<endl;
//     c3.sum(c1,c2);
//     c3.display();
//     cout<<"multiplication is"<<endl;
//     c4.mult(c1,c2);
//     c4.display();
//     return 0;
// }


////program to take students records
// #include<iostream>
// using namespace std;
// class person
// {
//     public:
//     string name;
//     int roll,dob;
//     void getdata()
//     {
//         cin>>name>>roll>>dob;
//     }
//     void display()
//     {
//         cout<<"name is"<<name<<endl;
//         cout<<"roll no is"<<roll<<endl;
//         cout<<"dob is"<<dob<<endl;
//     }
// };
// int main()
// {
    
//     int choice;
//     while (true)
//     {
//     person p1,p2;
//     cout<<"enter your choice"<<endl;
//     cout<<"1.insert data"<<endl;
//     cout<<"2.display data"<<endl;
//     cout<<"3.exit"<<endl;
//     cin>>choice;
//     switch(choice)
//     {
//         case 1:
//          cout<<"enter name , roll no ,dob"<<endl;
//          p1.getdata();
//          break;
//         case 2:
//             p1.display();
//             break;
//         case 3:
//             exit(0);
//         default:
//         cout<<"invalid value"<<endl;
//         break;
//     }
// }
//     return 0;
// }

#include<iostream>
#include<cstring>
#define max 10
using namespace std;
 class hashtable
 {
public :
char key[10],meaning[10],k[10];
string h[max][2];
int count,ch;
void input();
void display();
void hashf(char[]);
void linearp(string key,int);
 void search();
 void Delete();
hashtable()
{
 for(int i=0;i<max;i++)
 {
 for(int j=0;j<2;j++)
 {
 h[i][j] = "zzz";
 }
 }
 count=0;
}
 };
 void hashtable :: input()
 {
cout<<"Enter the key \n";
cin>>key;
cout<<"Enter the meaning \n";
cin>>meaning;
hashf(key);
 }
 void hashtable :: hashf(char key[])
 {
 int sum=0;
 for(int i=0 ;i<strlen(key) ;i++)
 {
sum = sum + int(key[i]);
}
ch = sum % max;
linearp(key,ch);

 }
 void hashtable :: linearp(string key,int ch)
 {
if(count==max)
{
cout<<"Table is Full";
}
else
{
while(h[ch][0]!="zzz" && count != max)
{
ch++;
ch = ch % max;
}
h[ch][0] = key;
h[ch][1] = meaning;
count++;
}
 }
 void hashtable :: display()
 {
 for(int i=0;i<max;i++)
 {
 for(int j=0;j<2;j++)
 {
 cout<<"\t"<<h[i][j];
}
cout<<"\n";
 }
 }
 void hashtable :: search()
 {
 cout<<"Enter the string to be search \n";
 cin>>k;
 int sum=0;
 for(int i=0 ;i<strlen(k) ;i++)
 {
 sum = sum + int(k[i]);
}
ch= sum % max;
 if(count==max)
{
cout<<"search is not found \n";
}
else
{
while(h[ch][0]!=k && count != max)
{
ch++;
ch = ch % max;
}
count++;
if(h[ch][0]==k)//strcmp(h[ch][0],k)==1)
 {
 cout<<"string is found at index"<<ch<<"\n";
 }
}
 }
 void hashtable :: Delete()
 {
 cout<<"Enter the string to be delete \n";
 cin>>k;
 int sum=0;
 for(int i=0 ;i<strlen(k) ;i++)
 {
 sum = sum + int(k[i]);
}
ch= sum % max;
if(count==max)
{
cout<<"search is not found \n";
}
else
{
while(h[ch][0]!=k && count != max)
{
ch++;
ch = ch % max;
}
 }

 h[ch][0]="zzz";
 h[ch][1]="zzz";
 cout<<"string is delete from index"<<ch<<"\n";

 }

 int main()
 {
 int ch;
 char c;
 hashtable h1;
do
{
cout<<"\nEnter choice\n1.input\n2.display\n3.search\n 4.Delete \n";
cin>>ch;
switch(ch)
{
case 1:
h1.input();
case 2:
h1.display();
break;
 case 3:
 h1.search();
 break;
 case 4:
 h1.Delete();
 break;
}
cout<<"Do you want to continue ?(y/n) \n";
cin>>c;
}while(c=='y'|| c=='Y');
 return 0;
 }
 