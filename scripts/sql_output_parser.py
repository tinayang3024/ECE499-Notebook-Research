import os

fp = "/mnt/e/School/ECE499/ECE499-new-research/ECE499-Notebook-Research/text/query_output/sentiment_output.txt"
out = "/mnt/e/School/ECE499/ECE499-new-research/ECE499-Notebook-Research/scripts/new_sample_list/sentiment_list.csv"
file_name = os.path.basename(fp).split('.')[0]
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