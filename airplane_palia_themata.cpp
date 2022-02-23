#include <iostream>
#include <string>

using namespace std;

class Karta{
    
    public:
        Karta(string new_code,int new_pontoi,int new_km);
        string getCode();
        int getPontoi();
        int getKm();
        void setPontoi(int pontoi2);
        void setKm(int km2);
        void print();
        void agora(int xrhmata);
        
    private:
        string code;
        int pontoi;
        int km;
};

int main()
{
    string cod="ab123";
    
    Karta aeromiles(cod,2000,2000);
    aeromiles.agora(1000);
    aeromiles.print();
    
    return 0;
}

Karta::Karta(string new_code,int new_pontoi,int new_km)
{
    code = "";
    km = 0;
    pontoi = 0;
    code = new_code;
    km = new_km;
    pontoi = new_pontoi;
    
}

string Karta::getCode()
{
    return code;
}

int Karta::getPontoi()
{
    return pontoi;
}

int Karta::getKm()
{
    return km;
}

void Karta::setPontoi(int pontoi2)
{
    pontoi = pontoi2;
}

void Karta::setKm(int km2)
{
    km = km2;
}

void Karta::print()
{
    if (pontoi<5000)
    {
        cout<<"Den dikaiouste akomh dwro"<<endl;
    }
    else if (pontoi>=5000 & pontoi<10000)
    {
        cout<<"Anavathmish theshs"<<endl;
    }
    else
    {
        cout<<"Dwrean taksidi"<<endl;
    }
}

void Karta::agora(int xrhmata)
{
    int pontoi_plus;
    pontoi_plus = 10*xrhmata;
    pontoi = pontoi + pontoi_plus;
    cout<<"Agorasate "<<pontoi_plus<<" pontous"<<endl;
}









