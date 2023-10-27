bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int left = 0, right = matrixSize * *matrixColSize - 1;
    int mid, row, col;
    while (left <= right) {
        mid = left + (right - left) / 2;
        row = mid / *matrixColSize;
        col = mid % *matrixColSize;
        if (matrix[row][col] > target) right = mid - 1;
        else if (matrix[row][col] < target) left = mid + 1;
        else return true;
    }
    return false;
}