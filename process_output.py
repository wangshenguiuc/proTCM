import sys
if len(sys.argv<4):
    print 'wrong argument.'
    print 'please input: process_output.py herb_file symptom_file output_file'
    
#fherb = open('..\..\\output\\topic_model\herbPLSA\\result\\herb.topic13')
#fsym = open('..\..\\output\\topic_model\herbPLSA\\result\\symptom.topic13')
#fout = open('..\..\\output\\herb_symptom\herbPLSA\\herb_symptom','w')
    
fherb = open(sys.argv[1])
fsym = open(sys.argv[2])
fout = open(sys.argv[3],'w')
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
    
