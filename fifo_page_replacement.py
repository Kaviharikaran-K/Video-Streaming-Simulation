"""
Video Streaming Page Replacement - FIFO Algorithm

This program simulates how an operating system replaces pages in memory
using the First-In First-Out (FIFO) page replacement algorithm.
"""

def read_page_reference():
    """Read page numbers separated by spaces or commas."""
    while True:
        raw = input("Enter page reference string (e.g., 7 0 1 2 0 3 0 4): ").strip()
        try:
            pages = [int(item) for item in raw.replace(",", " ").split()]
            if not pages:
                print("Please enter at least one page number.")
                continue
            if any(page < 0 for page in pages):
                print("Page numbers must be zero or positive.")
                continue
            return pages
        except ValueError:
            print("Invalid input. Enter only whole numbers separated by spaces or commas.")


def read_frame_count():
    """Read a positive number of memory frames."""
    while True:
        try:
            count = int(input("Enter number of memory frames: "))
            if count > 0:
                return count
            print("Frame count must be greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")


def fifo_page_replacement(pages, frame_count):
    """Run FIFO and print the frame state after every page reference."""
    frames = [None] * frame_count
    next_to_replace = 0
    page_faults = 0
    page_hits = 0

    print("\nFIFO PAGE REPLACEMENT")
    print("-" * 68)
    print(f"{'Page':<8}{'Frame contents':<34}{'Status':<12}{'Faults':<8}{'Hits'}")
    print("-" * 68)

    for page in pages:
        if page in frames:
            page_hits += 1
            status = "HIT"
        else:
            page_faults += 1
            frames[next_to_replace] = page
            next_to_replace = (next_to_replace + 1) % frame_count
            status = "FAULT"

        frame_text = "  ".join("-" if value is None else str(value) for value in frames)
        print(f"{page:<8}{frame_text:<34}{status:<12}{page_faults:<8}{page_hits}")

    print("-" * 68)
    print("RESULT")
    print(f"Total page references : {len(pages)}")
    print(f"Total page faults     : {page_faults}")
    print(f"Total page hits       : {page_hits}")
    print(f"Page fault ratio      : {page_faults / len(pages):.2%}")
    print(f"Page hit ratio        : {page_hits / len(pages):.2%}")


def main():
    print("=" * 48)
    print(" VIDEO STREAMING - FIFO PAGE REPLACEMENT ")
    print("=" * 48)

    pages = read_page_reference()
    frame_count = read_frame_count()
    fifo_page_replacement(pages, frame_count)


if __name__ == "__main__":
    main()
