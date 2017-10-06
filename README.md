# proTCM
###Author: Sheng Wang
A graphical model for mining symptom-herb relationship from electronic medical record

## inference
```bash
$ python herbPLSA.py
```
the result will be written to  "..\..\output\result\"
input tuple should be put at: "..\..\data\HIS_tuple.txt"
the input file format follows the most widely used topic model input format (e.g., the one used in LDA model)
For example: s1:s2:s3:...:sx\th1:h2:h3:...:hy


## Postprocessing
Converts the graphical model distribution into human readable word distribution. 
Input: herb_file and symptom_file are the output of herbPLSA.py
Output: output will be written to output_file

```bash
$ python process_output.py herb_file symptom_file output_file
```

##contact: 
swang141@illinois.edu

##related papers:
Sheng Wang, Edward Huang, Runshun Zhang, Xiaoping Zhang, Baoyan Liu, Xuezhong Zhou, ChengXiang Zhai. 
A Conditional Probabilistic Model for Joint Analysis of Symptoms, Diagnoses, and Herbs in Traditional Chinese Medicine Patient Records.
IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2017

Sheng Wang, Edward Huang, Bingxue Li, Ran Zhang, Xiaoping Zhang, Baoyan Liu, Jie Liu, Runshun Zhang, Xuezhong Zhou, ChengXiang Zhai. 
proTCM: An Asymmetric Probabilistic Model for the Joint Analysis of Symptoms, Diseases, and Herbs in Traditional Chinese Medicine Clinical Data.
To appear in BMC Medical Informatics and Decision Making. (extended journal version of BIBM paper)
