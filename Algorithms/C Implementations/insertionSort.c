// Online C compiler to run C program online

//  Insertion Sort

// START

//   step1: repeat for 1 to N

//   step2: temp = arr[i]

//   step3: j = i-1

//   step4: while (j>=0 && temp < arr[j])

//              arr[j+1] = arr[j]

//              j -= 1

//   step5: j-=1

//   step6: arr[j+1] = temp

//   step7: repeat from step 1

// END

#include <stdio.h>

int arr[10] = {5, 6, 1, 7, 8, 2, 3, 4, 9, 0};

int length = sizeof(arr) / sizeof(arr[0]);

int main() {

    int i, j, temp=0;

   for (i=1; i<length; i++) {

       j = i-1;

       temp = arr[i];

       while (j>=0 && temp < arr[j]) {

           arr[j+1] = arr[j];

           j -= 1;

       }

       arr[j+1] = temp;

   }

   

   for (i=0; i<length; i++) {

       printf("%d ", arr[i]);

   }

}
