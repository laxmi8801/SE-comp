#include<iostream>
#include<string.h>
using namespace std;

class bank_account
{
    public:
    char name[20];
    int act_no , deposite;
    char type[15];
    float balance, withdraw_amt;


    int getdata()
    {
        cout<<"Enter name and balance";
        cin>>name>>balance;
    }

    int dep_amt()
    {
        cout<<"Enter amt to deposite";
        cin>>deposite;
        balance += deposite;
    }

    int withdraw()
    {
        cout<<"Enter amt to withdraw";
        cin>> withdraw_amt;
        if (withdraw_amt > balance)
        {
            cout<<"withdrawal is not possible \n";
        }
        else
        {
            cout<<"Transaction sucessful \n You have " << balance - withdraw_amt << "rupees in your account \n";
        }
    }

    int display()
    {
        cout<<"Current accout details\n";
        cout<<"Name : "<< name << "\n";
        cout<<"Balance : " << balance<<"\n";
    }

};

int main()
{
    int choice;
    cout<<"Welcome \n";
    bank_account b1;
    b1.getdata();
    cout<<"How we can help you? \n";
    cout<<"Enter your choice \n"<<"1. Despite money \n";
    cout<<"2. Withdrawal \n";
    cout<<"3. Check balance \n ";
    cin >> choice;
    switch (choice)
    {
    case 1:
        b1.dep_amt();
        b1.display();
        break;
    case 2:
        b1.withdraw();
        b1.display();
        break;
    case 3:
        b1.display();
        break;

    default:
        break;
    
    }
    return 0;
}