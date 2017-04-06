fherb = open('..\..\\output\\topic_model\herbPLSA\\result\\herb.topic13')
fsym = open('..\..\\output\\topic_model\herbPLSA\\result\\symptom.topic13')
fout = open('..\..\\output\\herb_symptom\herbPLSA\\herb_symptom','w')
d = 20
for i in range(d):
    fherb.readline()
    herb_line = fherb.readline()
    fsym.readline()
    sym_line = fsym.readline()
    sym_line = sym_line.strip().replace('  ',',')
    herb_line = herb_line.strip().replace('  ',',')
    fout.write(sym_line+'\t'+herb_line+'\n')
fout.close()
    
