# gemini-trulens


# data

Data downloaded from pubmed

```
esearch -db pubmed -query "uveal melanoma" | efetch -format abstract > out-um.txt

esearch -db pubmed -query "lung AND carcinoma AND 2023/01/01:3000[Date - Publication]" | efetch -format abstract > out-lc.txt

esearch -db pubmed -query "ovarian AND carcinoma AND 2020/01/01:3000[Date - Publication]" | efetch -format abstract > out-oc.txt\n
```

# doctorai-trulens
trulens for doctorai


```
for i in edirect-um/*; python3 test-trulens.py $i | tee -a log0.txt
```

# edirect-um

The edirect-um directory has papers about uveal melanoma before 2000.

```
for PMID in $(esearch -db pubmed -query "uveal melanoma AND 1980:2000[Date - Publication]" | efetch -format uid); do echo $PMID && \n    efetch -db pubmed -id $PMID -format abstract > "$PMID.txt"\ndone\n
```

