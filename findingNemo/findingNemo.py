# message = "hello"
# index = 0
# for i in message : 
#     print ("Message[", index,"] = ", i )
#     index += 1

# string = "Divya is a good boy"
# subStr = "boi"
# print (string.find(subStr))

print ("Finding Nemo")
def check (subs,stri) :
    print (subs)
    if stri.find(subs) == -1 :
        print (subs," is not in the story")
    else :
        print (subs,"is their in the story at the index number ",stri.find(subs))    


string ="""Nemo is a young clownfish who lives with his father Marlin in an anemone in the Great Barrier Reef. Nemo,
despite being hampered by a lame right fin, is eager to explore life around the ocean. Marlin
, however, is overprotective of him, having lost his wife Coral and all their other eggs in a barracuda attack,
leaving Nemo as his only child. On Nemo's first day of school, Marlin unintentionally embarrasses him, and while Marlin
is distracted with the teacher, Mr. Ray, Nemo defiantly sneaks away from the reef toward a speedboat, where he is captured
by a pair of scuba divers. Marlin tries to chase the boat and meets Dory, a blue tang who suffers from acute short-term memory
loss, who offers her help. During an encounter with three sharks who have sworn to abstain from eating other fish, Marlin
notices a diver's mask that fell from the boat that took Nemo. Marlin and Dory fight over the mask, giving Dory a
nose bleed, which sends one of the sharks into a feeding frenzy, and Marlin and Dory narrowly escape, but are knocked
unconscious when the sharks accidentally set off a ring of old naval mines."""
substr = "divya"

check(substr,string)
