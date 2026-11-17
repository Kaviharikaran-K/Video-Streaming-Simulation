# Video Streaming Page Replacement – FIFO

## Aim
To implement the First-In First-Out (FIFO) page replacement algorithm using
Python and display the memory frame contents after every page reference.

## Description
A video streaming application accesses pages while playing a video. Since
main memory has a limited number of frames, a page that is not already in
memory causes a **page fault**.

FIFO replaces the page that entered memory first (the oldest page). A page
already present in memory causes a **page hit**, so no replacement is made.

## Requirements
- Python 3.x
- No external libraries are required.

## How to Run
1. Save the source file as `fifo_page_replacement.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python fifo_page_replacement.py
   ```

4. Enter the page-reference string using spaces or commas.
5. Enter a positive number of memory frames.

## Sample Input
```text
Enter page reference string (e.g., 7 0 1 2 0 3 0 4): 7 0 1 2 0 3 0 4
Enter number of memory frames: 3
```

## Sample Output
```text
================================================
 VIDEO STREAMING - FIFO PAGE REPLACEMENT
================================================

FIFO PAGE REPLACEMENT
--------------------------------------------------------------------
Page    Frame contents                    Status      Faults  Hits
--------------------------------------------------------------------
7       7  -  -                           FAULT       1       0
0       7  0  -                           FAULT       2       0
1       7  0  1                           FAULT       3       0
2       2  0  1                           FAULT       4       0
0       2  0  1                           HIT         4       1
3       2  3  1                           FAULT       5       1
0       2  3  0                           FAULT       6       1
4       4  3  0                           FAULT       7       1
--------------------------------------------------------------------
RESULT
Total page references : 8
Total page faults     : 7
Total page hits       : 1
Page fault ratio      : 87.50%
Page hit ratio        : 12.50%
```

## Algorithm
1. Create the memory frames as empty slots.
2. Set the FIFO replacement pointer to the first frame.
3. Read each page in the reference string.
4. If the page is already in a frame, count a page hit.
5. Otherwise, count a page fault and place the page in the frame pointed
   to by the FIFO pointer.
6. Move the pointer to the next frame. If it passes the last frame, return
   it to the first frame.
7. Display the frame contents and status after each page reference.
8. Display the total page faults, page hits, and their ratios.

## Key Terms
- **Page:** A block of a program or data loaded into memory.
- **Frame:** A fixed-size slot in physical memory that can hold one page.
- **Page fault:** The requested page is not currently in memory.
- **Page hit:** The requested page is already in memory.
- **FIFO:** The oldest loaded page is replaced first.

## Complexity
Let `n` be the number of page references and `f` be the number of frames.
- Time complexity: `O(n × f)` because each page may be checked against all frames.
- Space complexity: `O(f)` for the memory frames.

## Expected Result
The FIFO page replacement algorithm is implemented successfully. The program
shows the frame contents after every page reference and calculates the total
number of page faults and page hits.
