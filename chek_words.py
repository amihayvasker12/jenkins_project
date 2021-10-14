def word_count():
    count = 0

    with open("C:\\Users\\admin\\jenkins_1\\jenkins_project\\file.txt") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            for word in words:
                if word == "Amihay":
                    count += 1
    return count
