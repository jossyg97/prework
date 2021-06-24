names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
longest_name = ''
longest = 0 
for name in names_list:
    if len(name)>(longest):
        longest = len(name)
        longest_name = name
        
print (longest_name)
