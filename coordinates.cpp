
#include <iostream>

using namespace std;

class point{
    public:
        point();
        point(int new_x,int new_y);
        void show();
    private:
        int x,y;
};

int main()
{
    int new_y,new_x;
    
    cout<<"give an integer x coordinate: "<<endl;
    cin>>new_x;
    cout<<"give an integer y coordinate: "<<endl;
    cin>>new_y;

    point point1(new_x,new_y),point2(2,3),point3(5,3);
    point1.show();
    point2.show();
    point3.show();
    return 0;
}

point::point()
{
    x = 0;
    y = 0;
}

point::point(int new_x,int new_y)
{
    x = new_x;
    y = new_y;
}

void point::show()
{
    cout<<"("<<x<<","<<y<<")"<<endl;
}



