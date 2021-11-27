try:
	file1=open('mailbox.txt')
except:
	print("File cannot be opened or doesn't exist")
	exit()

lines=file1.readlines()
file2=open("output.txt","w")
count=0
for line in lines:
	if line.startswith("Subject:"):
		if "gradebook" in line:
			file2.write(line[8:-1])
			file2.write("\n")


file1.close()
file2.close()

