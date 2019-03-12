import matplotlib.pyplot as plt
import numpy as np

f = open("instagramlikes.txt", 'r')
lines = f.readlines()
post_nums = []
likes = []
for line in lines:
	thing = line.split(",")
	post_num = float(thing[0])
	like = float(thing[1])
	post_nums.append(post_num)
	likes.append(like)


plt.figure(1)
fig, ax = plt.subplots()
#plt.plot(post_nums, likes, 'b')
plt.bar(post_nums,likes, width=0.8, tick_label=None, color='midnightblue')
plt.xlabel("Post number (increasing in chronological order)")
plt.ylabel("Likes")
plt.title("Big Mike's Instagram Likes")
plt.savefig("instagramlol.png")