    pc_mem = psutil.virtual_memory()
    div_gb_factor = (1024.0 ** 3)
    free = pc_mem.used/pc_mem.total

    print("内存占用【%2f%】\n 剩余可用【%fGB】" %(free,float(pc_mem.available/div_gb_factor)))