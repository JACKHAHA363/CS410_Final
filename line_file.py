import pickle
outf = open("x_line_file", "w")
outf.truncate()
stop_words = pickle.load(open("stop_words.dat"))
for letter in ["x"]:
    filename = letter + "_songs.dat"
    f1 = open(filename, "rb")
    data1 = pickle.load(f1)
    for song_entry in data1:
        for line_entry in song_entry.lyrics:
            line_entry = line_entry.encode("ascii", "ignore")
            line_entry = line_entry.lower()
            line_entry = line_entry.replace("<s>", " ")
            line_entry = line_entry.replace("</s>", " ")
            for ascii in [i for i in range(33,65)] + [i for i in range(91,97)] + [i for i in range(123,127)]:
                if ascii == 39:
                    continue
                c = chr(ascii)
                line_entry = line_entry.replace(c, " ")
            for sw in stop_words:
                line_entry = line_entry.replace(' ' + sw + ' ', ' ')
            outf.write(line_entry + " ")
   	outf.write("\n")
    f1.close()
outf.close()
