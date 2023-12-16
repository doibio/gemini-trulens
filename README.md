# gemini-trulens


# data

Data downloaded from pubmed

```
esearch -db pubmed -query "uveal melanoma" | efetch -format abstract > out-um.txt

esearch -db pubmed -query "lung AND carcinoma AND 2023/01/01:3000[Date - Publication]" | efetch -format abstract > out-lc.txt

esearch -db pubmed -query "ovarian AND carcinoma AND 2020/01/01:3000[Date - Publication]" | efetch -format abstract > out-oc.txt\n
```

