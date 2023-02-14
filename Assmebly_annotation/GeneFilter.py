###Filter the gene with the specified ID in the fasta file

with open('id.txt', 'r') as f:
    data = f.read().split('\n')
print(data)
with open('MD_CDS.fasta', 'r') as g:
    fasta = g.read().split('\n')
    
for index, i in enumerate(fasta):
    if i.startswith('>'):
        _id = i[1:]
        if _id in data:
            pass
        else:
            newID = '>' + _id + '\n'
            f = fasta[index + 1] + '\n'
            with open('newAfterDel.fasta', 'a+') as file:
                file.write(newID)
                file.write(f)