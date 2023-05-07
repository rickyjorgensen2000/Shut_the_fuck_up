import os 

directory = "./stat_files/458.sjeng/"

for file in os.listdir(directory):
    old = directory + file
    
    if file.startswith('param1'):
        new_name = file.replace('param1','L1_Data_Memory_Cache_Size')
        new = directory + new_name
        os.rename(old,new)


    if file.startswith('param2'):
        new_name = file.replace('param2','L2_Cache_Size')
        new = directory + new_name
        os.rename(old,new)

    if file.startswith('param3'):
        new_name = file.replace('param3','L2_Associativity')
        new = directory + new_name
        os.rename(old,new)

    if file.startswith('param4'):
        new_name = file.replace('param4','L1_Instruction_Memory_Associativity')
        new = directory + new_name
        os.rename(old,new)

    if file.startswith('param5'):
        new_name = file.replace('param5','Block_Size')
        new = directory + new_name
        os.rename(old,new)
