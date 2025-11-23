with open("image_segmentation\\img4\\text_files\\labeling.txt", "r") as f1:
    with open("image_segmentation\\img4\\text_files\\clr__labeling.txt", "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        total_labels = 0
        matching_labels = 0

        min_lines = min(len(lines1), len(lines2))  # Get the minimum number of lines
        for i in range(min_lines):
            total_labels += 1
            elements1 = lines1[i].split()  # Split the line into elements
            elements2 = lines2[i].split() 
            last_element1 = elements1[-1] 
            last_element2 = elements2[-1] 

            if last_element1 == last_element2:
                matching_labels += 1
        percentage_matching = (matching_labels / total_labels) * 100
        print("Percentage of matching labels:", percentage_matching)
