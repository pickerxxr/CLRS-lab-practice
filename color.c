#include <stdio.h>
int main(){
   int arr[6] = {2,0,2,1,1,0};
   int arr_cnt[3] = {0,0,0};
   int arr_new[6];
   for (int i = 0; i < 6; i++){
        arr_cnt[arr[i]] ++;
   }
   for (int i = 1; i < 3; i++){
        arr_cnt[i] = arr_cnt[i - 1] + arr_cnt[i];
   }

   for (int i = 0; i < 6; i++){
        arr_new[arr_cnt[arr[i]] - 1] = arr[i];
        arr_cnt[arr[i]]--;
   }

   for (int i = 0; i < 6; i++){
        printf("%d", arr_new[i]);
   }
   return 0;
}

