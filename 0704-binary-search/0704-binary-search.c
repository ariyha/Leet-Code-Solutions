int search(int* nums, int n, int target) {
    int high = n-1;
    int low=0;
    int mid;

    while(low<=high){
        mid = high-low/2;
        if (nums[mid]==target){
            return mid;
        }
        if(nums[mid]>target){
            high=mid-1;
            continue;
        }
        else{
            low=mid+1;
        }
    }
    return -1;
}
