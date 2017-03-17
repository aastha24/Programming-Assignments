#include <iostream>
using namespace std;
int main()
{
	int A[] = {5,2,4,6,1,3};
	int i,j,key;
	int len = (sizeof(A)/sizeof(A[0]));
	for (j=1;j<len;j++)
	{
		key = A[j];
		i = j-1;
		while (i>=0 && (A[i]>key))
		{
			A[i+1] = A[i];
			i=i-1;
		}
		A[i+1]=key;

	}
	for (i=0;i<len;i++)
	{
		cout<<A[i]<<endl;
	}
}