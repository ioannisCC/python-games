#include <iostream>

using namespace std;

class mage{
    public:
        mage();
        void fireball();
        void lightning();
        void wait();
    private:
        int age;
        string beard;
        int magic;
};

int main()
{
    mage gandalf;
    
    gandalf.fireball();
    gandalf.wait();
    gandalf.lightning();
    gandalf.wait();
    gandalf.wait();
    gandalf.fireball();
    return 0;
}

mage::mage()
{
    age = 2019;
    beard = "grey";
    magic = 100;
}

void mage::fireball()
{
    magic-=30; 
    cout<<"fireball spell"<<endl;
    cout<<"magic is: "<<magic<<endl;
}

void mage::lightning()
{
    magic-=90;
    cout<<"lightning spell"<<endl;
    cout<<"magic is: "<<magic<<endl;
}

void mage::wait()
{
    magic+=10;
    cout<<"waiting..."<<endl;
    cout<<"magic is: "<<magic<<endl;
}

