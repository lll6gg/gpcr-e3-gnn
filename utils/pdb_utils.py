import pandas as pd
import pymol
def fetch_sele():
    data = pd.read_json('response.txt')
    
    data.set_index('pdb_code', inplace=True)
    
    filtered_data = data[data['species'] == 'Homo sapiens']
    
    min_resolution_data = filtered_data.groupby('family')['resolution'].idxmin()
    
    pdb_codes = min_resolution_data.values
    
    print(len(pdb_codes))
    print(pdb_codes)
    
    filtered_data = data[data.index.isin(pdb_codes)]
    
    # pymol.finish_launching()
    for index,row in filtered_data.iterrows():
        # print(index)
        # print(row)
        # pymol.cmd.reinitialize()  # 重新初始化PyMOL
        print(index)
        
        # pymol.cmd.fetch(index)
        # if row[4] == 'A':
        print(row[4])
        print(index)
    
        pymol.cmd.fetch(index)
        # pymol.cmd.load(f'{index}.cif', f'{index}_object')
        # pymol.cmd.select("not chain {row[4]}")
        chains = pymol.cmd.get_chains()
        if row[4] in chains:
        # pymol.cmd.remove("sele")
        # 选择链A和残基0到600
            pymol.cmd.select('selection', f'chain {row[4]} and resi 0-600')
    
            # 删除剩下的部分
            pymol.cmd.remove('not selection')
            # pymol.cmd.remove(f'not chain {row[4]}')
            object_name = pymol.cmd.get_object_list()[0]
            pymol.cmd.save(f'./result/result_{index}.pdb',object_name)
