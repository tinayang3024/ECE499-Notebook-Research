import os


fp = "/mnt/e/School/ECE499/ECE499-research/samples_NLP.txt"
file_name = os.path.basename(fp).split('.')[0]
out = os.path.join("/mnt/e/School/ECE499/ECE499-research/samples", file_name + ".csv")
with open(fp, 'r') as f:
    with open(out, 'w') as f_out:
        for line in f:
            if "----------------------" in line:
                continue
            tokens = line.split("|")[1:-1]
            print(tokens)
            line = ""
            for token in tokens:
                line += token.strip(" ") + ", "
            f_out.write(line[:-1] + "\n")