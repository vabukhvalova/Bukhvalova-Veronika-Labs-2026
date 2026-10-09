#include <iostream>
#include <cmath>
using namespace std;

class U {
public:
    double a, b, c;

    void vvod() {
        cout << "Введите A: ";
        cin >> a;
        cout << "Введите B: ";
        cin >> b;
        cout << "Введите C: ";
        cin >> c;
    }

    void reshenie() {
        if (a == 0) {
            reshenie_a_0();
            return;
        }

        double D = b * b - 4 * a * c;
        cout << "D = " << D << endl;

        if (D < 0) {
            cout << "Корней нет" << endl;
            return;
        }

        if (D == 0) {
            double t = -b / (2 * a);
            kor(t);
            return;
        }

        double t1 = (-b + sqrt(D)) / (2 * a);
        double t2 = (-b - sqrt(D)) / (2 * a);
        kor(t1);
        kor(t2);
    }

    void reshenie_a_0() {

        if (b == 0) {
            if (c == 0) {
                cout << "Уравнение 0 = 0, любое x является решением" << endl;
            } else {
                cout << "Уравнение не имеет решений" << endl;
            }
            return;
        }

        double t = -c / b;
        kor(t);
    }

    void kor(double t) {
        if (t < 0) return;
        if (t == 0) {
            cout << "x = 0" << endl;
        } else {
            cout << "x = " << sqrt(t) << endl;
            cout << "x = " << -sqrt(t) << endl;
        }
    }
};

int main() {
    setlocale(LC_ALL, "ru_RU.UTF-8");
    U u;
    u.vvod();
    u.reshenie();
    return 0;
}