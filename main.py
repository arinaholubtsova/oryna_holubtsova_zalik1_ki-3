if __name__ == '__main__':

    current_paragraph = []
    paragraphs = []

    search_word = input("Please enter text for search: ")
    file_name = input("Please enter file name to search in: ")

    try:
        with open(file_name) as file:
            for row in file:
                row = row.strip()
                if not row and len(current_paragraph) > 0:
                    paragraphs.append(current_paragraph)
                    current_paragraph = []
                elif row:
                    current_paragraph.append(row)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

    if len(current_paragraph) > 0:
        paragraphs.append(current_paragraph)

    nothingFoundFlag = True

    for lines in paragraphs:
        for line in lines:
            if search_word in line:
                nothingFoundFlag = False
                for ln in lines:
                    print(ln)
                print()
                break

    if nothingFoundFlag:
        print("Nothing found...")

