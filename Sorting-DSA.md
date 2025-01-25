Sorting Algorithms in DSA
Sorting algorithms are used to arrange elements in a specific order (ascending or descending) within a data structure, typically an array or list. Sorting is a fundamental operation in computer science with various use cases, such as organizing data for search, preparing data for efficient access, or even making other algorithms (like binary search) more effective.

Let’s go through some of the important sorting algorithms, their time complexities, and provide example code for each:

1. Bubble Sort
Bubble Sort is a simple comparison-based sorting algorithm. It works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

Time Complexity:
Best: O(n)
Average: O(n²)
Worst: O(n²)
Example Code:
java
Copy
void bubbleSort(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap the elements
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
2. Selection Sort
Selection Sort works by selecting the smallest (or largest) element from the unsorted part of the list and swapping it with the first unsorted element. This process repeats until the entire list is sorted.

Time Complexity:
Best: O(n²)
Average: O(n²)
Worst: O(n²)
Example Code:
java
Copy
void selectionSort(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n-1; i++) {
        int minIdx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        // Swap the found minimum element with the first element
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}
3. Insertion Sort
Insertion Sort builds the final sorted array one element at a time. It assumes that the first element is already sorted, and it inserts the next element into the sorted part of the list, moving the elements as necessary.

Time Complexity:
Best: O(n)
Average: O(n²)
Worst: O(n²)
Example Code:
java
Copy
void insertionSort(int arr[]) {
    int n = arr.length;
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
4. Merge Sort
Merge Sort is a Divide and Conquer algorithm. It divides the array into two halves, recursively sorts them, and then merges the sorted halves.

Time Complexity:
Best: O(n log n)
Average: O(n log n)
Worst: O(n log n)
Example Code:
java
Copy
void mergeSort(int arr[]) {
    if (arr.length < 2) return;
    
    int mid = arr.length / 2;
    int[] left = Arrays.copyOfRange(arr, 0, mid);
    int[] right = Arrays.copyOfRange(arr, mid, arr.length);
    
    mergeSort(left);
    mergeSort(right);
    
    merge(arr, left, right);
}

void merge(int[] arr, int[] left, int[] right) {
    int i = 0, j = 0, k = 0;
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        } else {
            arr[k++] = right[j++];
        }
    }
    while (i < left.length) arr[k++] = left[i++];
    while (j < right.length) arr[k++] = right[j++];
}
5. Quick Sort
Quick Sort is also a Divide and Conquer algorithm. It picks a pivot element, partitions the array into two sub-arrays (elements smaller than the pivot and elements larger than the pivot), and then recursively sorts the sub-arrays.

Time Complexity:
Best: O(n log n)
Average: O(n log n)
Worst: O(n²) (though it can be optimized)
Example Code:
java
Copy
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        // Partitioning index
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1); // Recursively sort left subarray
        quickSort(arr, pi + 1, high); // Recursively sort right subarray
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Taking the last element as the pivot
    int i = (low - 1); // index of smaller element

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    // Swap arr[i + 1] and arr[high] (pivot element)
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1; // Return partition index
}
6. Heap Sort
Heap Sort is a comparison-based sorting algorithm that uses a binary heap to build a heap structure and repeatedly extracts the largest or smallest element from the heap to place it in the sorted array.

Time Complexity:
Best: O(n log n)
Average: O(n log n)
Worst: O(n log n)
Example Code:
java
Copy
void heapSort(int arr[]) {
    int n = arr.length;
    
    // Build a max-heap
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    
    // One by one extract elements from the heap
    for (int i = n - 1; i > 0; i--) {
        // Swap the root (maximum element) with the last element
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;

        // Heapify the root element
        heapify(arr, i, 0);
    }
}

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }
    if (largest != i) {
        // Swap
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}
7. Radix Sort
Radix Sort is a non-comparative sorting algorithm that works by sorting numbers digit by digit, from the least significant digit to the most significant. It uses a stable sub-sort (like counting sort) to sort each digit.

Time Complexity:
Best: O(nk)
Average: O(nk)
Worst: O(nk)
where n is the number of elements and k is the number of digits in the largest number.
Example Code:
java
Copy
void radixSort(int arr[]) {
    int max = Arrays.stream(arr).max().getAsInt();
    
    // Apply counting sort for every digit.
    for (int exp = 1; max / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

void countingSort(int arr[], int exp) {
    int n = arr.length;
    int[] output = new int[n];
    int[] count = new int[10]; // For digits 0 to 9
    
    // Store count of occurrences
    for (int i = 0; i < n; i++) {
        count[(arr[i] / exp) % 10]++;
    }
    
    // Change count[i] to contain the actual position of the digit in output[]
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }
    
    // Build the output array
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    
    // Copy the sorted elements into the original array
    System.arraycopy(output, 0, arr, 0, n);
}
Conclusion
These are some of the most common sorting algorithms in DSA. Depending on the input size, data characteristics, and specific requirements, each algorithm has different advantages and trade-offs. For large datasets, algorithms like Merge Sort and Quick Sort are often preferred due to their O(n log n) time complexity, while for smaller datasets, simpler algorithms like Bubble Sort or Insertion Sort might be more efficient due to their O(n²) time complexity.

Understanding these algorithms and their time complexities will help you choose the right sorting technique for different problem scenarios.



