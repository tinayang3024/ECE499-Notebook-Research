
# generate sql
string = "when totalvotes between {} and {} then '({}, {})'\n"

long_str = string
with open("./sql_cmd", 'w') as f:
    # f.write("select case ")
    for i in range(0, 1700, 100):
        f.write(string.format(str(i), str(i+100), str(i), str(i+100)))
    # f.write("        else '66450+'\n\
    # end as grps, \n\
    #     count(*) \n\
    # from \n\
    # (\n\
    #     select \n\
    #     versionnumber\n\
    #     from \n\
    #     kernels k inner join kernelversions kv on k.currentkernelversionid = kv.id\n\
    # ) as dt\n\
    # group by 1;")


