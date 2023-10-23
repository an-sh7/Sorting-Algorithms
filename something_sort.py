import multiprocessing

def parallel_sort(arr):
    # Split the input array into sub-arrays for parallel processing
    num_processes = multiprocessing.cpu_count()
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    # Function to sort each chunk
    def sort_chunk(chunk):
        return sorted(chunk)

    # Create a pool of worker processes for parallel sorting
    with multiprocessing.Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(sort_chunk, chunks)

    # Merge the sorted chunks to obtain the final sorted array
    sorted_arr = merge(sorted_chunks)

    return sorted_arr

def merge(sorted_chunks):
    # Merge sorted sub-arrays into a single sorted array
    result = []
    while len(sorted_chunks) > 1:
        a, b = sorted_chunks.pop(0), sorted_chunks.pop(0)
        result.append(merge_arrays(a, b))
    if sorted_chunks:
        result.append(sorted_chunks[0])
    return result[0]

def merge_arrays(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

if __name__ == "__main__":
    unsorted_array = [8, 4, 7, 1, 3, 9, 2, 6, 5]
    sorted_array = parallel_sort(unsorted_array)
    print("Sorted Array:", sorted_array)
