filename = "file.txt"

with open(filename, "r", encoding="utf8") as f:
    for line in f.readlines():
        if "#" in line:
            # print(line)
            formattedFile = open(f"{line[1:-1]}.txt", "w+", encoding="utf8")
        elif len(line) > 1:
            print(len(line))

            fData = []
            temp = line.split("–")
            [fData.append(data) for data in temp[0].split(" ") if len(data) > 0]
            if temp and len(temp) > 0:
                fData.append(temp[1][:-1])

            if formattedFile is not None:
                formattedFile.write(f"{fData[0]}-{fData[1]}\n{fData[2]}\n\n")
    formattedFile.close()

