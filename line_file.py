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
            for sw in stop_words:
                line_entry = line_entry.replace(' ' + sw + ' ', ' ')
                #line_entry = line_entry.replace(sw + '.', '')
                #line_entry = line_entry.replace(sw + ',', '')
                #line_entry = line_entry.replace(sw + '?', '')
            outf.write(line_entry + " ")
   	outf.write("\n")
    f1.close()
outf.close()
