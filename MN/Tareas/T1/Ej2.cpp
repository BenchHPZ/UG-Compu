#include<iostream> //Biblioteca donde se encuentra la función cout

using namespace std;  //uso del espacio de nombre std


float epsilonFloat( void ){

	float epsilon, unidad, valor;

	epsilon = 1.0;
	unidad = 1.0;
	valor = unidad + epsilon;

	while (valor > unidad){
		epsilon = epsilon/2;
		valor = unidad + epsilon;
	}

	return epsilon*2;
}

double epsilonDouble( void ){

	double epsilon, unidad, valor;

	epsilon = 1.0;
	unidad = 1.0;
	valor = unidad + epsilon;

	while (valor > unidad){
		epsilon = epsilon/2;
		valor = unidad + epsilon;
	}

	return epsilon*2;
}


int main( ){

	cout << "Para 32 bits obtuvimos: epsilon= " 
	     << epsilonFloat() << endl;
	
	cout << "Para 64 bits obtuvimos: epsilon= " 
	     << epsilonDouble() << endl;

	return 0;
}