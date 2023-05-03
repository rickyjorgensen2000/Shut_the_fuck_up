import os 
#401.bzip2

directory = "./458.sjeng"

for file in os.listdir(directory):

    f = os.path.join(directory,file)

    if os.path.isfile(f):
        with open(f) as filee:

            for line in filee:
                #L1D cache
                if line.startswith('system.cpu.dcache.overall_hits::total'):
                    l1_dhits = line.split()[1]
                if line.startswith('system.cpu.dcache.overall_accesses::total'):
                    l1_doverall = line.split()[1]

                #L1I Cache
                if line.startswith('system.cpu.icache.overall_hits::total'):
                    l1_ihits = line.split()[1]
                if line.startswith('system.cpu.icache.overall_accesses::total'):
                    l1_ioverall = line.split()[1]


                #l2 cache
                if line.startswith('system.l2.overall_hits::total'):
                    l2_hits = line.split()[1]
                if line.startswith('system.l2.overall_accesses::total'):
                    l2_overall = line.split()[1]

                #CPI
                if line.startswith('system.cpu.icache.overall_misses::total'):
                    i_cache_miss_num = float(line.split()[1])
                if line.startswith('system.cpu.dcache.overall_misses::total'):
                    d_cache_miss_num = float(line.split()[1])
                if line.startswith('system.l2.overall_misses::total'):
                    l2_misses = float(line.split()[1])
                if line.startswith('sim_insts'):
                    total = float(line.split()[1])



            L1_dhit_rate = float(l1_dhits)/float(l1_doverall)

            L1_ihit_rate = float(l1_ihits)/float(l1_ioverall)

            L2_hit_rate = float(l2_hits)/float(l2_overall)

            CPI = 1 + (((i_cache_miss_num + d_cache_miss_num) * 6)  + (l2_misses * 50)) / total

            with open(directory + "final.txt","a") as final_file:
                final_file.write(str(f)+ "\n")
                final_file.write(f"L1 Dcache: {L1_dhit_rate}\n")
                final_file.write(f"L1 Icache: {L1_ihit_rate}\n")
                final_file.write(f"L2 cache: {L2_hit_rate} \n")
                final_file.write(f"CPI: {CPI}\n \n")







