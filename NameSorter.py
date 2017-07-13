import sorting

filename = "/home/vampy/data/test1"
fp =open(filename, "r")
N = int(fp.readline())
names = []
for i in range(N):
	names.append(fp.readline().strip())

fp.close()

sorting.merge(names)
fp=open(open_filename,"w")
fp.write("{0}\n".format(N))
for i n range(N)
	fp.write("{0}\n".format(names[i]))
fp.close()
